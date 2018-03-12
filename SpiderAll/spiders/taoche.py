# -*- coding: utf-8 -*-
from lxml import etree
import scrapy, re, sys, logging, os
from SpiderAll.items import TaocheItem

class TaocheSpider(scrapy.Spider):
    name = 'taoche'
    allowed_domains = ['taoche.com']
    # start_urls = ['http://taoche.com/']

    total,success,fail = 0,0,0

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {'SpiderAll.middlewares.TaocheFilterMiddleware': 543},
        'ITEM_PIPELINES': {'SpiderAll.pipelines.TaochePipeline': 300,'SpiderAll.pipelines.TaocheMySQLPipeline': 310},
        'DOWNLOAD_DELAY': 3,
        'REDIRECT_ENABLED': False,
        'LOG_FILE': os.path.dirname(__file__) + r'\\log\\taoche.log',
        # 'LOG_LEVEL': 'WARNING',        
        # 'DOWNLOADER_MIDDLEWARES': {'SpiderAll.middlewares.TaocheFilterMiddleware': 543,'SpiderAll.middlewares.TaocheMiddleware': 544},
    }

    def start_requests(self):
        strs = '---------->>>>>>>>>STARTING TAOCHE...'
        sys.stdout.write(strs + '\r\n')
        sys.stdout.flush()
        for url in self.settings['INIT_TAOCHE']:
            yield scrapy.Request(url, method='get', dont_filter=True, callback=self.parse)


    def parse(self, response):
        text = response.body.decode(response.encoding)
        root = etree.HTML(text)

        # 解析列表页面
        urls = root.xpath('//*[@id="container_base"]/div/div[2]/h2/a/@href')
        for url in urls:
            yield scrapy.Request(url, method='get', meta={'url':url}, dont_filter=True, callback=self.parse_detail)
        # 翻页器
        next_page = root.xpath('//div[@class="paging-box the-pages"]/div/a[last()]/@href')[0]
        pattern = re.compile(r'^http://(\w+)\.taoche\.com/all/\?page=(\d+)#pagetag$')
        flag = pattern.match(next_page)
        if flag is not None:
            yield scrapy.Request(next_page, method='get', dont_filter=True, callback=self.parse)


    def parse_detail(self, response):

        self.total += 1

        item = TaocheItem()
        text = response.body.decode(response.encoding)
        root = etree.HTML(text)

        url = response.meta['url']
        item['url'] = url

        try:
            item['brand'] = root.xpath('//div[@class="crumbs-c"]/a[4]/text()')[0].strip()
            item['series'] = root.xpath('//div[@class="crumbs-c"]/a[5]/text()')[0].strip()
            item['model'] = root.xpath('//div[@class="crumbs-c"]/a[6]/text()')[0]
            # 当前竞价
            item['quotes'] = root.xpath('//strong[@class="price-this"]/text()')[0]
            # 是否包含过户费
            item['trans_fee'] = root.xpath('//span[@class="price-note"]/text()')[0]
            # 新车指导价/税款
            msrp = root.xpath('//div[@class="price-ratio clearfix"]/span/text()')[0]
            # item['tax'] = root.xpath('//div[@class="summary-price-wrap "]/span[1]/text()')[0]
            # 参考价范围
            item['refer_lower'] = root.xpath('//div[@class="summary-price"]/div[2]/node()[3]')[0].strip()
            # item['refer_upper'] = root.xpath('//div[@class="summary-price-wrap "]/span[2]/text()')[0]
            # 上牌时间
            item['regDate'] = root.xpath('//div[@class="summary-attrs"]/dl[1]/dd/text()')[0]
            # 表显里程
            item['mile'] = root.xpath('//div[@class="summary-attrs"]/dl[2]/dd/text()')[0]
            # 排量/变速箱
            item['displacement'] = root.xpath('//div[@class="summary-attrs"]/dl[3]/dd/text()')[0]
            # item['gearbox'] = root.xpath('//div[@class="summary-attrs"]/dl[3]/dd/text()')[0]
            # 车辆所在地/销售城市
            item['address'] = root.xpath('//div[@class="summary-attrs"]/dl[4]/dd/text()')[0]

            # 保养方式
            margin_flag1 = root.xpath('//div[@class="row  details-information-list"]/div[2]/div/div[2]/div[1]/node()[3]')
            margin_flag2 = root.xpath('//div[@class="row   details-information-list"]/div[2]/div/div[2]/div[1]/node()[3]')
            if margin_flag1:
                item['maintain'] = root.xpath('//div[@class="row  details-information-list"]/div[2]/div/div[2]/div[1]/node()[3]')[0].strip()
                # 使用类型
                item['nature'] = root.xpath('//div[@class="row  details-information-list"]/div[2]/div/div[2]/div[2]/node()[3]')[0].strip()

                # 年检到期日
                item['annual'] = root.xpath('//div[@class="row  details-information-list"]/div[4]/div/div[2]/div[1]/node()[3]')[0].strip()
                # 保险到期日
                item['insure'] = root.xpath('//div[@class="row  details-information-list"]/div[4]/div/div[2]/div[2]/node()[3]')[0].strip()
            elif margin_flag2:
                item['maintain'] = root.xpath('//div[@class="row   details-information-list"]/div[2]/div/div[2]/div[1]/node()[3]')[0].strip()
                # 使用类型
                item['nature'] = root.xpath('//div[@class="row   details-information-list"]/div[2]/div/div[2]/div[2]/node()[3]')[0].strip()

                # 年检到期日
                item['annual'] = root.xpath('//div[@class="row   details-information-list"]/div[4]/div/div[2]/div[1]/node()[3]')[0].strip()
                # 保险到期日
                item['insure'] = root.xpath('//div[@class="row   details-information-list"]/div[4]/div/div[2]/div[2]/node()[3]')[0].strip()                
            else:
                item['maintain'] = root.xpath('//div[@class="row margin-md details-information-list"]/div[2]/div/div[2]/div[1]/node()[3]')[0].strip()
                # 使用类型
                item['nature'] = root.xpath('//div[@class="row margin-md details-information-list"]/div[2]/div/div[2]/div[2]/node()[3]')[0].strip()

                # 年检到期日
                item['annual'] = root.xpath('//div[@class="row margin-md details-information-list"]/div[4]/div/div[2]/div[1]/node()[3]')[0].strip()
                # 保险到期日
                item['insure'] = root.xpath('//div[@class="row margin-md details-information-list"]/div[4]/div/div[2]/div[2]/node()[3]')[0].strip()


            # 车辆来源
            item['source'] = root.xpath('//div[@class="hide-box"]/div[2]/div[1]/ul/li[2]/span/text()')[0]
            # 牌照所在地
            item['location'] = root.xpath('//div[@class="hide-box"]/div[2]/div[1]/ul/li[3]/span/a/text()')[0].strip()
            # 车身照片
            try:
                item['car_picture'] = root.xpath('//ul[@id="carSourceImgUl"]/li/img/@data-src')[0]
            except IndexError:
                item['car_picture'] = '数据缺失'
            # 发布时间
            menu_flag = root.xpath('//div[@id="tab-menu"]/span[last()]/text()')
            if menu_flag:
                item['public_time'] = root.xpath('//div[@id="tab-menu"]/span[last()]/text()')[0]
            else:
                item['public_time'] = root.xpath('//div[@class="detail-tabnav"]/span[last()]/text()')[0]

            # 修正
            if msrp=='新车价：不详':
                item['msrp'] = '0'
                item['tax'] = '0'
            else:
                pattern = re.compile(r'^([参|新].*?：)(?P<num1>\d+\.?\d+)(.*?[-|税])(?P<num2>\d+\.?\d+)(.*?[万|）])$')
                result = pattern.match(msrp)
                if result is not None:
                    item['tax'] = result.group('num2')
                    item['msrp'] = result.group('num1')
                else:
                    msrp = root.xpath('//div[@class="summary-price"]/div[2]/span/s/text()')[0]
                    tax = root.xpath('//div[@class="summary-price"]/div[2]/span/node()[last()]')[0]
                    item['msrp'] = re.match(r'^(\d+\.?\d+)万$', msrp).group(1)
                    item['tax'] = re.match(r'^（含税(\d+\.?\d+)万）$', tax).group(1)

            self.success += 1
            strs = '---------->>>>>>>>>taoche: total:%d,success:%d,fail:%d' %(self.total, self.success, self.fail)
            sys.stdout.write(strs + '\r')
            sys.stdout.flush()
            return item

        except Exception as e:
            self.fail += 1
            strs = '---------->>>>>>>>>taoche: total:%d,success:%d,fail:%d' %(self.total, self.success, self.fail)
            sys.stdout.write(strs + '\r')
            sys.stdout.flush()
            logging.warning(e)
            logging.warning('ERROR:' + url)
            return None