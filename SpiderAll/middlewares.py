# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy import exceptions
import pymysql

'''
CHE300
'''

class Che300ProxyMiddleware(object):

    def __init__(self, proxies):
        # 此处匹配代理池与cookie池的二维数组
        self.proxies = proxies
        self.length = len(proxies)
        self.count = 0


    # 从setting读取指定数据
    @classmethod
    def from_settings(cls, settings):
        proxies = settings['AAA_CHE300']
        return cls(proxies)


    def process_request(self, request, spider):
        self.count += 1
        self.count = self.count % self.length
        temp = self.proxies[self.count]
        ip = temp[0]
        port = temp[1]
        # token = temp[2]
        request.meta['proxy'] = 'http://%s:%s' %(ip, port)
        # request.headers['Cookie'] = token

class Che300FilterMiddleware(object):

    def __init__(self, dbparams):
        conn = pymysql.connect(**dbparams)
        cursor = conn.cursor()
        cursor.execute('select url from spider_www_che300')

        data = cursor.fetchall()
        self.filter = set()
        for d in data:
            self.filter.add(d[0])
        cursor.close()
        conn.close()


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

    def process_request(self, request, spider):
        url = request.url
        if url in self.filter:
            raise exceptions.IgnoreRequest
        else:
            self.filter.add(url)



'''
TAOCHE
'''

class TaocheMiddleware(object):
    
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        # 从settings文件中加载User-Agent
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        # 设置请求user-agent
        request.headers.setdefault('User-Agent', random.choice(self.agents))
        # 设置代理
        r = requests.get('http://localhost:8080/?protocol!=1&count=3&country=%E5%9B%BD%E5%86%85')
        r.encoding = chardet.detect(r.content)['encoding']
        proxylist = json.loads(r.text)
        proxy = random.choice(proxylist)
        ip = proxy[0]
        port = proxy[1]
        request.meta['proxy'] = 'http://%s:%s' % (ip, port)

class TaocheFilterMiddleware(object):

    def __init__(self, dbparams):
        conn = pymysql.connect(**dbparams)
        cursor = conn.cursor()
        cursor.execute('select url from spider_www_taoche')
        data = cursor.fetchall()
        self.filter = set()
        for d in data:
            self.filter.add(d[0])
        cursor.close()
        conn.close()

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

    def process_request(self, request, spider):
        url = request.url
        if url in self.filter:
            raise exceptions.IgnoreRequest
        else:
            self.filter.add(url)

class SpiderallSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
