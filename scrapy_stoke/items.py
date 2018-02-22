# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyStokeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DimensionItem(scrapy.Item):
    市场 = scrapy.Field()
    日期 = scrapy.Field()
    指标名称 = scrapy.Field()
    本日数值 = scrapy.Field()
    比上日增减 = scrapy.Field()
    幅度pct = scrapy.Field()
    本年最高 = scrapy.Field()
    最高值日期 = scrapy.Field()
