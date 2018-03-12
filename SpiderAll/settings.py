# -*- coding: utf-8 -*-

# Scrapy settings for SpiderAll project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os, json

BOT_NAME = 'SpiderAll'

SPIDER_MODULES = ['SpiderAll.spiders']
NEWSPIDER_MODULE = 'SpiderAll.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'SpiderAll (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  # 'Accept-Language': 'zh-CN,zh;q=0.9',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
}


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'SpiderAll.middlewares.SpiderallSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'SpiderAll.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'SpiderAll.pipelines.SpiderallPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


'''
CHE300
'''
def load_other(path):
    with open(path, 'r') as f:
        aaa = json.load(f)        
    return aaa

AAA_CHE300 = load_other(os.path.dirname(__file__) + r'\\other\\che300.json')

INIT_CHE300 = ['13', '43', '71', '99', '127', '155', '182', '209', '235', '259', '281', '299', '316', '330', '343', '353', '363', '1', '4', '14', '44', '72', '100', '128', '156', '183', '210', '236', '28', '58', '86', '114', '142', '170', '197', '224', '249', '271', '292', '309', '326', '340', '23', '53', '81', '109', '137', '165', '192', '219', '245', '21', '51', '79', '107', '135', '163', '190', '217', '243', '266', '288', '305', '322', '336', '20', '50', '78', '106', '134', '162', '189', '216', '242', '265', '287', '304', '321', '335', '347', '357', '367', '373', '378', '382', '386', '24', '54', '82', '110', '138', '166', '193', '220', '246', '268', '290', '307', '324', '338', '349', '359', '369', '375', '396', '19', '49', '77', '105', '133', '161', '188', '215', '241', '264', '286', '303', '320', '334', '18', '48', '76', '104', '132', '160', '187', '214', '240', '263', '285', '302', '319', '333', '346', '356', '366', '17', '47', '75', '103', '131', '159', '186', '213', '239', '262', '284', '301', '318', '332', '345', '355', '365', '372', '10', '40', '68', '96', '124', '152', '179', '206', '232', '256', '278', '297', '314', '5', '35', '63', '91', '119', '147', '174', '201', '227', '252', '274', '15', '45', '73', '101', '129', '157', '184', '211', '237', '260', '282', '11', '41', '69', '97', '125', '153', '180', '207', '233', '257', '279', '298', '315', '9', '39', '67', '95', '123', '151', '178', '205', '231', '8', '38', '66', '94', '122', '150', '177', '204', '230', '255', '277', '296', '313', '329', '32', '62', '90', '118', '146', '173', '200', '226', '251', '273', '294', '311', '30', '60', '88', '116', '144', '26', '56', '84', '112', '140', '168', '195', '222', '22', '52', '80', '108', '136', '164', '191', '218', '244', '267', '289', '306', '323', '337', '348', '358', '368', '374', '379', '383', '387', '6', '36', '64', '92', '120', '148', '175', '202', '228', '253', '275', '3', '27', '57', '85', '113', '141', '169', '196', '223', '248', '270', '16', '46', '74', '102', '130', '158', '185', '212', '238', '261', '283', '300', '317', '331', '344', '354', '364', '2', '29', '59', '87', '115', '143', '171', '198', '31', '61', '89', '117', '145', '172', '199', '225', '250', '272', '293', '310', '327', '341', '351', '361', '370', '376', '380', '384', '388', '390', '392', '393', '395', '397', '25', '55', '83', '111', '139', '167', '194', '221', '247', '269', '291', '308', '325', '339', '350', '360', '12', '42', '70', '98', '126', '154', '181', '208', '234', '258', '280']

INIT_TAOCHE = ['http://hefei.taoche.com/all/', 'http://anqing.taoche.com/all/', 'http://bengbu.taoche.com/all/', 'http://chaohu.taoche.com/all/', 'http://chizhou.taoche.com/all/', 'http://fuyang.taoche.com/all/', 'http://huainan.taoche.com/all/', 'http://luan.taoche.com/all/', 'http://maanshan.taoche.com/all/', 'http://tongling.taoche.com/all/', 'http://wuhu.taoche.com/all/', 'http://xuancheng.taoche.com/all/', 'http://chuzhou.taoche.com/all/', 'http://sz.taoche.com/all/', 'http://bozhou.taoche.com/all/', 'http://huaibei.taoche.com/all/', 'http://huangshan.taoche.com/all/', 'http://beijing.taoche.com/all/', 'http://chongqing.taoche.com/all/', 'http://fuzhou.taoche.com/all/', 'http://xiamen.taoche.com/all/', 'http://longyan.taoche.com/all/', 'http://zhangzhou.taoche.com/all/', 'http://putian.taoche.com/all/', 'http://quanzhou.taoche.com/all/', 'http://nanping.taoche.com/all/', 'http://ningde.taoche.com/all/', 'http://sanming.taoche.com/all/', 'http://guangzhou.taoche.com/all/', 'http://shenzhen.taoche.com/all/', 'http://zhuhai.taoche.com/all/', 'http://dongguan.taoche.com/all/', 'http://zhongshan.taoche.com/all/', 'http://shantou.taoche.com/all/', 'http://shaoguan.taoche.com/all/', 'http://zhaoqing.taoche.com/all/', 'http://maoming.taoche.com/all/', 'http://foshan.taoche.com/all/', 'http://huizhou.taoche.com/all/', 'http://jiangmen.taoche.com/all/', 'http://qingyuan.taoche.com/all/', 'http://chaozhou.taoche.com/all/', 'http://zhanjiang.taoche.com/all/', 'http://meizhou.taoche.com/all/', 'http://jieyang.taoche.com/all/', 'http://yunfu.taoche.com/all/', 'http://yangjiang.taoche.com/all/', 'http://heyuan.taoche.com/all/', 'http://shanwei.taoche.com/all/', 'http://nanning.taoche.com/all/', 'http://liuzhou.taoche.com/all/', 'http://guilin.taoche.com/all/', 'http://beihai.taoche.com/all/', 'http://baise.taoche.com/all/', 'http://hezhou.taoche.com/all/', 'http://hechi.taoche.com/all/', 'http://guigang.taoche.com/all/', 'http://yulin.taoche.com/all/', 'http://qinzhou.taoche.com/all/', 'http://wuzhou.taoche.com/all/', 'http://fangchenggang.taoche.com/all/', 'http://laibin.taoche.com/all/', 'http://chongzuo.taoche.com/all/', 'http://guiyang.taoche.com/all/', 'http://zunyi.taoche.com/all/', 'http://anshun.taoche.com/all/', 'http://liupanshui.taoche.com/all/', 'http://tongrendiqu.taoche.com/all/', 'http://qiandongnan.taoche.com/all/', 'http://qiannan.taoche.com/all/', 'http://bijiediqu.taoche.com/all/', 'http://qianxinan.taoche.com/all/', 'http://lanzhou.taoche.com/all/', 'http://dingxi.taoche.com/all/', 'http://pingliang.taoche.com/all/', 'http://jiuquan.taoche.com/all/', 'http://qingyang.taoche.com/all/', 'http://baiyin.taoche.com/all/', 'http://zhangye.taoche.com/all/', 'http://wuwei.taoche.com/all/', 'http://tianshui.taoche.com/all/', 'http://jiayuguan.taoche.com/all/', 'http://jinchang.taoche.com/all/', 'http://linxia.taoche.com/all/', 'http://longnan.taoche.com/all/', 'http://gannan.taoche.com/all/', 'http://haikou.taoche.com/all/', 'http://sanya.taoche.com/all/', 'http://qiongbeidiqu.taoche.com/all/', 'http://qiongnandiqu.taoche.com/all/', 'http://wuhan.taoche.com/all/', 'http://shiyan.taoche.com/all/', 'http://xiangfan.taoche.com/all/', 'http://suizhou.taoche.com/all/', 'http://yichang.taoche.com/all/', 'http://huangshi.taoche.com/all/', 'http://jingmen.taoche.com/all/', 'http://jingzhou.taoche.com/all/', 'http://ezhou.taoche.com/all/', 'http://xianning.taoche.com/all/', 'http://xiaogan.taoche.com/all/', 'http://huanggang.taoche.com/all/', 'http://enshi.taoche.com/all/', 'http://hubeizhixiaxian.taoche.com/all/', 'http://changsha.taoche.com/all/', 'http://chenzhou.taoche.com/all/', 'http://changde.taoche.com/all/', 'http://hengyang.taoche.com/all/', 'http://huaihua.taoche.com/all/', 'http://loudi.taoche.com/all/', 'http://zhuzhou.taoche.com/all/', 'http://yueyang.taoche.com/all/', 'http://xiangtan.taoche.com/all/', 'http://shaoyang.taoche.com/all/', 'http://yongzhou.taoche.com/all/', 'http://yiyang.taoche.com/all/', 'http://zhangjiajie.taoche.com/all/', 'http://xiangxi.taoche.com/all/', 'http://zhengzhou.taoche.com/all/', 'http://luoyang.taoche.com/all/', 'http://zhoukou.taoche.com/all/', 'http://xinyang.taoche.com/all/', 'http://xinxiang.taoche.com/all/', 'http://shangqiu.taoche.com/all/', 'http://sanmenxia.taoche.com/all/', 'http://puyang.taoche.com/all/', 'http://nanyang.taoche.com/all/', 'http://luohe.taoche.com/all/', 'http://jiaozuo.taoche.com/all/', 'http://kaifeng.taoche.com/all/', 'http://anyang.taoche.com/all/', 'http://hebi.taoche.com/all/', 'http://pingdingshan.taoche.com/all/', 'http://zhumadian.taoche.com/all/', 'http://xuchang.taoche.com/all/', 'http://henanzhixiaxian.taoche.com/all/', 'http://shijiazhuang.taoche.com/all/', 'http://tangshan.taoche.com/all/', 'http://xingtai.taoche.com/all/', 'http://qinhuangdao.taoche.com/all/', 'http://langfang.taoche.com/all/', 'http://handan.taoche.com/all/', 'http://hengshui.taoche.com/all/', 'http://cangzhou.taoche.com/all/', 'http://baoding.taoche.com/all/', 'http://zhangjiakou.taoche.com/all/', 'http://chengde.taoche.com/all/', 'http://haerbin.taoche.com/all/', 'http://daqing.taoche.com/all/', 'http://qiqihaer.taoche.com/all/', 'http://jiamusi.taoche.com/all/', 'http://mudanjiang.taoche.com/all/', 'http://jixi.taoche.com/all/', 'http://qitaihe.taoche.com/all/', 'http://yc.taoche.com/all/', 'http://heihe.taoche.com/all/', 'http://shuangyashan.taoche.com/all/', 'http://suihua.taoche.com/all/', 'http://daxinganlingdiqu.taoche.com/all/', 'http://nanjing.taoche.com/all/', 'http://suzhou.taoche.com/all/', 'http://wuxi.taoche.com/all/', 'http://changzhou.taoche.com/all/', 'http://huaian.taoche.com/all/', 'http://lianyungang.taoche.com/all/', 'http://nantong.taoche.com/all/', 'http://yancheng.taoche.com/all/', 'http://yangzhou.taoche.com/all/', 'http://zhenjiang.taoche.com/all/', 'http://taizhou.taoche.com/all/', 'http://xuzhou.taoche.com/all/', 'http://suqian.taoche.com/all/', 'http://nanchang.taoche.com/all/', 'http://shangrao.taoche.com/all/', 'http://pingxiang.taoche.com/all/', 'http://xinyu.taoche.com/all/', 'http://yichun.taoche.com/all/', 'http://jiujiang.taoche.com/all/', 'http://ganzhou.taoche.com/all/', 'http://jian.taoche.com/all/', 'http://jingdezhen.taoche.com/all/', 'http://jxfz.taoche.com/all/', 'http://yingtan.taoche.com/all/', 'http://changchun.taoche.com/all/', 'http://jl.taoche.com/all/', 'http://tonghua.taoche.com/all/', 'http://liaoyuan.taoche.com/all/', 'http://songyuan.taoche.com/all/', 'http://yanbian.taoche.com/all/', 'http://siping.taoche.com/all/', 'http://baishan.taoche.com/all/', 'http://baicheng.taoche.com/all/', 'http://shenyang.taoche.com/all/', 'http://dalian.taoche.com/all/', 'http://dandong.taoche.com/all/', 'http://fushun.taoche.com/all/', 'http://fuxin.taoche.com/all/', 'http://huludao.taoche.com/all/', 'http://chaoyang.taoche.com/all/', 'http://benxi.taoche.com/all/', 'http://anshan.taoche.com/all/', 'http://jinzhou.taoche.com/all/', 'http://liaoyang.taoche.com/all/', 'http://yingkou.taoche.com/all/', 'http://panjin.taoche.com/all/', 'http://tieling.taoche.com/all/', 'http://huhehaote.taoche.com/all/', 'http://baotou.taoche.com/all/', 'http://chifeng.taoche.com/all/', 'http://tongliao.taoche.com/all/', 'http://wuhai.taoche.com/all/', 'http://eerduosi.taoche.com/all/', 'http://bayannaoer.taoche.com/all/', 'http://wulanchabu.taoche.com/all/', 'http://xilinguolemeng.taoche.com/all/', 'http://hulunbeier.taoche.com/all/', 'http://xinganmeng.taoche.com/all/', 'http://alashanmeng.taoche.com/all/', 'http://yinchuan.taoche.com/all/', 'http://zhongwei.taoche.com/all/', 'http://wuzhong.taoche.com/all/', 'http://guyuan.taoche.com/all/', 'http://shizuishan.taoche.com/all/', 'http://xining.taoche.com/all/', 'http://haibei.taoche.com/all/', 'http://huangnan.taoche.com/all/', 'http://guoluo.taoche.com/all/', 'http://yushu.taoche.com/all/', 'http://haixi.taoche.com/all/', 'http://haidongdiqu.taoche.com/all/', 'http://hainan.taoche.com/all/', 'http://xian.taoche.com/all/', 'http://xianyang.taoche.com/all/', 'http://weinan.taoche.com/all/', 'http://yl.taoche.com/all/', 'http://baoji.taoche.com/all/', 'http://hanzhong.taoche.com/all/', 'http://yanan.taoche.com/all/', 'http://tongchuan.taoche.com/all/', 'http://shangluo.taoche.com/all/', 'http://ankang.taoche.com/all/', 'http://shanghai.taoche.com/all/', 'http://taiyuan.taoche.com/all/', 'http://datong.taoche.com/all/', 'http://jincheng.taoche.com/all/', 'http://linfen.taoche.com/all/', 'http://changzhi.taoche.com/all/', 'http://yuncheng.taoche.com/all/', 'http://xinzhou.taoche.com/all/', 'http://shuozhou.taoche.com/all/', 'http://lvliang.taoche.com/all/', 'http://jinzhong.taoche.com/all/', 'http://yangquan.taoche.com/all/', 'http://chengdu.taoche.com/all/', 'http://mianyang.taoche.com/all/', 'http://suining.taoche.com/all/', 'http://panzhihua.taoche.com/all/', 'http://yibin.taoche.com/all/', 'http://zigong.taoche.com/all/', 'http://ziyang.taoche.com/all/', 'http://deyang.taoche.com/all/', 'http://leshan.taoche.com/all/', 'http://nanchong.taoche.com/all/', 'http://meishan.taoche.com/all/', 'http://bazhong.taoche.com/all/', 'http://luzhou.taoche.com/all/', 'http://neijiang.taoche.com/all/', 'http://dazhou.taoche.com/all/', 'http://yaan.taoche.com/all/', 'http://guangyuan.taoche.com/all/', 'http://guangan.taoche.com/all/', 'http://aba.taoche.com/all/', 'http://ganzi.taoche.com/all/', 'http://liangshan.taoche.com/all/', 'http://jinan.taoche.com/all/', 'http://dezhou.taoche.com/all/', 'http://qingdao.taoche.com/all/', 'http://yantai.taoche.com/all/', 'http://weihai.taoche.com/all/', 'http://weifang.taoche.com/all/', 'http://taian.taoche.com/all/', 'http://zaozhuang.taoche.com/all/', 'http://zibo.taoche.com/all/', 'http://dongying.taoche.com/all/', 'http://heze.taoche.com/all/', 'http://binzhou.taoche.com/all/', 'http://liaocheng.taoche.com/all/', 'http://linyi.taoche.com/all/', 'http://jining.taoche.com/all/', 'http://rizhao.taoche.com/all/', 'http://laiwu.taoche.com/all/', 'http://dezhou.taoche.com/all/', 'http://tianjin.taoche.com/all/', 'http://wulumuqi.taoche.com/all/', 'http://kelamayi.taoche.com/all/', 'http://bazhou.taoche.com/all/', 'http://yili.taoche.com/all/', 'http://kashidiqu.taoche.com/all/', 'http://akesudiqu.taoche.com/all/', 'http://hetiandiqu.taoche.com/all/', 'http://tachengdiqu.taoche.com/all/', 'http://tulufandiqu.taoche.com/all/', 'http://hamidiqu.taoche.com/all/', 'http://aletaidiqu.taoche.com/all/', 'http://xinjiangkezhou.taoche.com/all/', 'http://changji.taoche.com/all/', 'http://xinjiangzhixiaxian.taoche.com/all/', 'http://lasa.taoche.com/all/', 'http://rikazediqu.taoche.com/all/', 'http://shannan.taoche.com/all/', 'http://kunming.taoche.com/all/', 'http://qujing.taoche.com/all/', 'http://baoshan.taoche.com/all/', 'http://xishuangbanna.taoche.com/all/', 'http://honghe.taoche.com/all/', 'http://dali.taoche.com/all/', 'http://yuxi.taoche.com/all/', 'http://lincang.taoche.com/all/', 'http://wenshan.taoche.com/all/', 'http://zhaotong.taoche.com/all/', 'http://lijiang.taoche.com/all/', 'http://dehong.taoche.com/all/', 'http://nujiang.taoche.com/all/', 'http://diqing.taoche.com/all/', 'http://puer.taoche.com/all/', 'http://chuxiong.taoche.com/all/', 'http://hangzhou.taoche.com/all/', 'http://ningbo.taoche.com/all/', 'http://wenzhou.taoche.com/all/', 'http://jiaxing.taoche.com/all/', 'http://jinhua.taoche.com/all/', 'http://lishui.taoche.com/all/', 'http://huzhou.taoche.com/all/', 'http://quzhou.taoche.com/all/', 'http://tz.taoche.com/all/', 'http://shaoxing.taoche.com/all/', 'http://zhoushan.taoche.com/all/']




'''
MySQL settings
'''
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = '159723'
MYSQL_DBNAME = 'yck-data-center'


'''
USER_AGENTS
'''
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
] 