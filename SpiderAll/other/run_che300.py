# -*- coding: utf-8 -*-
from scrapy import cmdline
import os

if __name__ == '__main__':
    cmdline.execute('scrapy crawl che300'.split())
    os.system("pause")