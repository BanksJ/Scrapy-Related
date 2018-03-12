# -*- coding: utf-8 -*-
import scrapy, random
from lxml import etree
import sys, logging, os
from SpiderAll.items import Che300Item

class Che300Spider(scrapy.Spider):
    name = 'che300'
    allowed_domains = ['che300.com']
    # start_urls = ['http://che300.com/']

    # 统计抓取情况
    success = 0
    fail = 0


    # 统计抓取情况
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {'SpiderAll.middlewares.Che300FilterMiddleware': 543,'SpiderAll.middlewares.Che300ProxyMiddleware': 544},
        'ITEM_PIPELINES': {'SpiderAll.pipelines.Che300Pipeline': 300,'SpiderAll.pipelines.Che300MySQLPipeline': 310},
        'DOWNLOAD_DELAY': 3,
        'REDIRECT_ENABLED': False,
        'LOG_FILE': os.path.dirname(__file__) + r'\\log\\che300.log',
        # 'LOG_LEVEL': 'WARNING',        
    }



    # 以各大城市分别为入口发送请求
    def start_requests(self):
        strs = '---------->>>>>>>>>STARTING CHE300...'
        sys.stdout.write(strs + '\r\n')
        sys.stdout.flush()
        random.shuffle(self.settings['INIT_CHE300'])
        city = self.settings['INIT_CHE300']
        for zone in city:
            url = 'https://www.che300.com/buycar/?city=' + zone
            yield scrapy.Request(url, method='get', dont_filter=True, callback=self.parse)


    # 解析各大城市发布页面，提取车辆详细信息地址，并发起详细信息请求
    def parse(self, response):
        res = response.body.decode(response.encoding)
        root = etree.HTML(res)
        # 解析列表页面
        links = root.xpath('//div[@class="list-wrap"]//ul/li/a/@href')
        for link in links:
            url = link
            yield scrapy.Request(url, method='get', meta={'page':url}, dont_filter=True, callback=self.parse_detail)
        # 翻页器
        next_page = root.xpath('//ul[@class="page_index"]/li[last()]/a/@href')
        if next_page:
            nxt_url = next_page[0]
            yield scrapy.Request(nxt_url, method='get', dont_filter=True, callback=self.parse)



    # 按照需求，解析详细页面，抓取指定字段数据，生成item
    def parse_detail(self, response):
        item = Che300Item()
        res = response.body.decode(response.encoding)
        root = etree.HTML(res)

        url = response.meta['page']
        item['url'] = url

        strs = '--------->>>>>>>>>che300: success:%d,fail:%d, url:%s' %(self.success, self.fail, url)

        try:
            # 车300车型id
            item['model_id'] = root.xpath('//input[@id="modelId"]/@value')[0]

            # 当前报价
            item['quotes'] = root.xpath('//div[@class="dtir-price clearfix"]/strong/text()')[0]
            # 新车最低价
            try:
                item['new_price'] = root.xpath('//span[@id="lowestNewPrice"]/text()')[0]
            except:
                 item['new_price'] = root.xpath('//span[@id="newPrice"]/text()')[0]

            # 推荐指数
            try:
                item['recommended'] = root.xpath('//div[@class="dtir-price clearfix"]/p/i/text()')[0]
            except IndexError as e:
                item['recommended'] = None


            # 上牌日期
            item['regDate'] = root.xpath('//ul[@class="dtir-4in clearfix"]/li[1]/span/text()')[0]
            # 公里数
            item['mile'] = root.xpath('//ul[@class="dtir-4in clearfix"]/li[2]/span/text()')[0]
            # 所在地
            item['address'] = root.xpath('//ul[@class="dtir-4in clearfix"]/li[3]/span/text()')[0]
            # 排放标准
            item['emission'] = root.xpath('//li[@class="discharge-standand"]/span/text()')[0]
            # 来源平台
            item['platform'] = root.xpath('//ul[@class="dtir-4in clearfix"]/li[5]/a/text()')[0].strip()
            # 来源商家/个人
            item['source'] = root.xpath('//div[@class="dtil-symbol"]/span/text()')[0].strip()


            # 车身颜色
            item['color'] = root.xpath('//div[@class="dt-base"]/ul/li[2]/text()')[0]
            # 年检到期时间
            item['annual'] = root.xpath('//div[@class="dt-base"]/ul/li[4]/text()')[0]
            # 首次上牌时间
            item['first_regdate'] = root.xpath('//div[@class="dt-base"]/ul/li[6]/text()')[0]
            # 变速箱
            item['gearbox'] = root.xpath('//div[@class="dt-base"]/ul/li[8]/text()')[0]
            # 交强险到期时间
            item['high_insure'] = root.xpath('//div[@class="dt-base"]/ul/li[10]/text()')[0]
            # 估值
            item['valuation_300'] = root.xpath('//div[@class="dt-base"]/ul/li[12]/text()')[0]
            # 排量
            item['displacement'] = root.xpath('//div[@class="dt-base"]/ul/li[14]/text()')[0]
            # 商业险到期时间
            item['commercial_insure'] = root.xpath('//div[@class="dt-base"]/ul/li[16]/text()')[0]
            # 下一年估值
            item['next_valuation_300'] = root.xpath('//div[@class="dt-base"]/ul/li[18]/text()')[0]

            # 车辆描述
            try:
                item['description'] = root.xpath('//p[@class="dt-para"]/text()')[0]
            except IndexError as e:
                item['description'] = None

            # 统计
            self.success += 1
            sys.stdout.write(strs + '\r\n')
            sys.stdout.flush()

            # 抛出数据
            yield item

        except Exception as e:
            # 异常记录
            logging.warning(e)
            logging.warning('爬虫抓取错误:' + url)
            self.fail += 1
            sys.stdout.write(strs + '\r\n')
            sys.stdout.flush()