# -*- coding: utf-8 -*-
from scrapy import cmdline
import os

if __name__ == '__main__':
    cmdline.execute('scrapy crawl taoche'.split())
    os.system("pause")