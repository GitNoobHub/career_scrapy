# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CareerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    region = scrapy.Field()
    identify = scrapy.Field()
    name = scrapy.Field()
    school_url = scrapy.Field()
    
    level = scrapy.Field()
    cate = scrapy.Field()
    sub = scrapy.Field()
    skill = scrapy.Field()