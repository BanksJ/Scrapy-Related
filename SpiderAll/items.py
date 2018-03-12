# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Che300Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    model_id = scrapy.Field()
    quotes = scrapy.Field()
    new_price = scrapy.Field()
    recommended = scrapy.Field()
    regDate = scrapy.Field()
    mile = scrapy.Field()
    address = scrapy.Field()
    emission = scrapy.Field()
    source = scrapy.Field()
    platform = scrapy.Field()
    color = scrapy.Field()
    annual = scrapy.Field()
    first_regdate = scrapy.Field()
    gearbox = scrapy.Field()
    high_insure = scrapy.Field()
    valuation_300 = scrapy.Field()
    displacement = scrapy.Field()
    commercial_insure = scrapy.Field()
    next_valuation_300 = scrapy.Field()
    description = scrapy.Field()
    add_time = scrapy.Field()
    update_time = scrapy.Field()


class TaocheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    brand = scrapy.Field()
    series = scrapy.Field()
    model = scrapy.Field()
    location = scrapy.Field()
    quotes = scrapy.Field()
    trans_fee = scrapy.Field()
    msrp = scrapy.Field()
    tax = scrapy.Field()
    refer_lower = scrapy.Field()
    refer_upper = scrapy.Field()
    regDate = scrapy.Field()
    mile = scrapy.Field()
    address = scrapy.Field()
    public_time = scrapy.Field()
    maintain = scrapy.Field()
    nature = scrapy.Field()
    annual = scrapy.Field()
    source = scrapy.Field()
    insure = scrapy.Field()
    car_picture = scrapy.Field()
    displacement = scrapy.Field()
    gearbox = scrapy.Field()
    add_time = scrapy.Field()
    update_time = scrapy.Field()