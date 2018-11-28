# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class MyspiderItem(scrapy.Item):#  继承scrapy的Item
#     """一般继承的需要重写方法，不继承的需要进行配置"""
#     # define the fields for your item here like:
#     # name = scrapy.Field()#当字符串处理
#     # title = scrapy.Field()
#     # salary = scrapy.Field()
#     # pass
#     #百度失信人字段
#     iname = scrapy.Field()
#     cardNum = scrapy.Field()
#     courtName = scrapy.Field()
#     areaName = scrapy.Field()
#     caseCode = scrapy.Field()
#     duty = scrapy.Field()
#     performance = scrapy.Field()
#     disruptTypeName = scrapy.Field()
#     publishDate = scrapy.Field()


class MyImageItem(scrapy.Item):
    image_urls=scrapy.Field()
    image_store=scrapy.Field()