#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  
from selenium.webdriver.common.proxy import ProxyType  
import requests, chardet, json, time
from tqdm import tqdm
import sys, os

class UpdateAAA(object):

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }

    config = {
        'che300': [os.path.dirname(__file__) + r'\\che300.json', 'https://www.guazi.com/sz/', 'antipas']
    }

    def __init__(self, flag):
        self.flag = flag

    def update_proxy(self):
        # 获取代理
        r = requests.get('http://localhost:8000/?types=0&protocol=2&count=5&country=%E5%9B%BD%E5%86%85')
        r.encoding = chardet.detect(r.content)['encoding']
        proxylist = json.loads(r.text)
        # 更新文件
        with open('D:/scrapy/proxypool.json', 'w') as f:
            json.dump(proxylist, f)

        return None

    def update_cookie(self,www):
        '''
        : param:
        : return:
        '''
        # 文件路径
        path = self.config[www][0]
        # 读取文件
        with open(path, 'r') as f:
            proxylist = json.load(f)
        # 封装结果列表
        result = list()
        # 获取代理对应cookie
        for proxy in tqdm(proxylist):
            ip = proxy[0]
            port = proxy[1]
            cookie = self.get_cookie(ip, port, www)
            result.append([ip,port,cookie])
        # 更新文件
        with open(path, 'w') as f:
            print(result)
            json.dump(result, f)

    def get_cookie(self, ip, port, www):

        # 设置代理能力
        proxy = webdriver.Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.http_proxy = '%s:%s' %(ip, port)

        # 个性化配置浏览器能力
        # copy初始能力
        desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
        # 伪装chrome浏览器
        desired_capabilities['phantomjs.page.settings.userAgent'] = self.headers['User-Agent']
        # 设定不载入图片
        desired_capabilities['phantomjs.page.settings.loadImages'] = False

        # 将代理添加到webdriver.DesiredCapabilities.PHANTOMJS中
        proxy.add_to_capabilities(desired_capabilities)
        # 打开浏览器操作符
        driver = webdriver.PhantomJS()
        # 使用个性化配置，打开会话
        driver.start_session(desired_capabilities)
        # 设定会话访问延时
        driver.set_page_load_timeout(20)
        # 访问页面
        url = self.config[www][1]
        driver.get(url)
        # 获取cookie
        cookies = driver.get_cookies()
        # 关闭浏览器
        driver.quit()

        # 抽取令牌信息
        for cookie in cookies:
            token = None
            # 取cookie名
            name = self.config[www][2]
            if cookie['name'] == name:
                # 储存访问令牌
                token = name + '=' + cookie['value']
                break

        return token

if __name__ == '__main__':

    str = 'start update....'
    sys.stdout.write(str + '\r\n')
    sys.stdout.flush()

    # 生成更新对象
    obj = UpdateAAA(0)
    # 更新代理文件
    if obj.flag==1:
        obj.update_proxy()
    # 更新cookie文件
    for www in obj.config.keys():        
        sys.stdout.write('start update ' + www + '\r\n')
        sys.stdout.flush()
        obj.update_cookie(www)
        sys.stdout.write('update done ' + www + '\r\n')
        sys.stdout.flush()

    sys.stdout.write('all done' + '\r\n')
    sys.stdout.flush()
    os.system("pause")