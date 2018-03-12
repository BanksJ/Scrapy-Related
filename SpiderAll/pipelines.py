# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import pymysql, re, decimal
import logging

'''
CHE300
'''
class Che300Pipeline(object):
    def process_item(self, item, spider):

        # 处理当前报价
        item['quotes'] = self.get_number(item['quotes'])
        # 处理新车最低价
        item['new_price'] = self.get_number(item['new_price'])
        # 处理公里数
        item['mile'] = self.get_number(item['mile'])
        # 处理车300估值
        item['valuation_300'] = self.get_number(item['valuation_300'])
        # 处理下一年车300估值
        item['next_valuation_300'] = self.get_number(item['next_valuation_300'])

        # 处理上牌时间
        item['regDate'] = datetime.strptime(item['regDate'], '%Y年%m月')
        # 处理首次上牌时间
        item['first_regdate'] = datetime.strptime(item['first_regdate'], '%Y-%m-%d')

        # 处理推荐指数
        if item['recommended'] is not None:
            item['recommended'] = re.search(r'\d+\.?\d*', item['recommended']).group()
            item['recommended'] = decimal.Decimal(float(item['recommended']))
        
        # 增加时间
        now = datetime.today()
        item['add_time'] = now
        item['update_time'] = now

        return item

    def get_number(self, strs):
        data = re.search(r'\d+\.?\d*', strs).group()
        data = int(float(data)*10000)
        return data

class Che300MySQLPipeline(object):

    def __init__(self, dbparams):
        self.conn = pymysql.connect(**dbparams)
        self.dbparams = dbparams

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host = settings['MYSQL_HOST'],
            port = settings['MYSQL_PORT'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWD'],
            db = settings['MYSQL_DBNAME'],
            charset = 'utf8',
            )
        return cls(dbparams)

    def process_item(self, item, spider):

        sql = 'insert into spider_www_che300 values (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )'

        data = list()

        keys = ['url', 'model_id', 'quotes', 'new_price', 'recommended', 'regDate', 'mile', 'address', 'emission',
                'source', 'platform', 'color', 'annual', 'first_regdate', 'gearbox', 'high_insure', 'valuation_300', 'displacement',
                'commercial_insure', 'next_valuation_300', 'description', 'add_time', 'update_time']

        for i in keys:
            data.append(item[i])
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, data)
            self.conn.commit()
            cursor.close()
        except Exception as e:
            logging.warning(e)
            logging.warning('database error')
            self.conn = pymysql.connect(**self.dbparams)

        return None

'''
TAOCHE
'''

class TaochePipeline(object):
    def process_item(self, item, spider):

        item['brand'] = item['brand'].split('二手')[1]
        item['series'] = item['series'].split('二手')[1]
        item['model'] = re.match(r'^(二手)?(?P<model>.*?)$', item['model']).group('model')

        car_condition = re.match(r'^(?P<displacement>\d+\.?\d+L)?/?(?P<gearbox>.*?)?$', item['displacement'])
        item['gearbox'] = car_condition.group('gearbox')
        item['displacement'] = car_condition.group('displacement')

        try:
            pattern = re.compile(r'^([参|新].*?：)(?P<num1>\d+\.?\d+)(.*?[-|税])(?P<num2>\d+\.?\d+)(.*?[万|）])$')
            item['refer_upper'] = pattern.match(item['refer_lower']).group('num2')
            item['refer_lower'] = pattern.match(item['refer_lower']).group('num1')
            item['refer_lower'] = self.str2int(item['refer_lower'])
            item['refer_upper'] = self.str2int(item['refer_upper'])
        except Exception:
            item['refer_lower'] = None
            item['refer_upper'] = None

        if item['mile']=='百公里内':
            item['mile'] = 100
        else:
            item['mile'] = re.match(r'^(\d+\.?\d+).*?里$', item['mile']).group(1)
            item['mile'] = self.str2int(item['mile'])

        
        item['public_time'] = re.match(r'^发.*?(\d+-\d+-\d+)$', item['public_time']).group(1)

        # 转换字符串到整数
        item['quotes'] = self.str2int(item['quotes'])
        item['msrp'] = self.str2int(item['msrp'])
        item['tax'] = self.str2int(item['tax'])
        

        # 转换字符串到日期
        if item['regDate']=='未上牌':
            item['regDate']=datetime.strptime('1880年8月', '%Y年%m月')
        else:
            item['regDate'] = datetime.strptime(item['regDate'], '%Y年%m月')
        item['public_time'] = datetime.strptime(item['public_time'], '%Y-%m-%d')

        # 编码部分字段
        item['trans_fee'] = self.standard_fee(item['trans_fee'])
        item['nature'] = self.standard_nature(item['nature'])
        item['maintain'] = self.standard_maintain(item['maintain'])

        return item

    def str2int(self, strs):
        r = float(strs)
        r = int(r*10000)
        return r

    def standard_fee(self, fee):
        if fee=='（含过户费）':
            return 1
        elif fee=='（不含过户费）':
            return 0
        else:
            return None

    def standard_maintain(self, maintain):
        if maintain=='4S店定期保养':
            return 1
        elif maintain=='非4S店定期保养':
            return 2
        elif maintain=='无定期保养':
            return 0
        else:
            return None

    def standard_nature(self, nature):
        if nature=='非营运车':
            return 1
        elif nature=='营转非':
            return 2
        elif nature=='营运车':
            return 3
        else:
            return None


class TaocheMySQLPipeline(object):

    def __init__(self, dbparams):
        self.conn = pymysql.connect(**dbparams)
        self.dbparams = dbparams

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host = settings['MYSQL_HOST'],
            port = settings['MYSQL_PORT'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWD'],
            db = settings['MYSQL_DBNAME'],
            charset = 'utf8',
            )
        return cls(dbparams)


    def process_item(self, item, spider):
        sql = 'insert into spider_www_taoche values (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        yiche = ['url', 'brand', 'series', 'model', 'quotes', 'mile', 'regDate', 'location', 'address', 'trans_fee', 'msrp', 'tax', 'refer_lower', 'refer_upper',
                 'public_time', 'gearbox', 'displacement', 'maintain', 'nature', 'annual', 'insure', 'source', 'car_picture', 'add_time', 'update_time']

        now = datetime.today()
        item['add_time'] = now
        item['update_time'] = now

        data = list()

        for i in yiche:
            data.append(item[i])

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, data)
            self.conn.commit()
            cursor.close()
        except Exception as e:
            print(e)
            self.conn = pymysql.connect(**self.dbparams)