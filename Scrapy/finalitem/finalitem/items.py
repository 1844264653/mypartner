# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FinalitemItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionName = scrapy.Field()  ## 职位
    companyFullName = scrapy.Field()  # 公司名字
    salary = scrapy.Field()  # 薪水
    jobNature = scrapy.Field()  # 任职要求
    workYear = scrapy.Field()  # 经验要求
    education = scrapy.Field()  # 学历要求
    city = scrapy.Field() # 城市
    positionAdvantage = scrapy.Field()  # 公司福利
    companySize = scrapy.Field()  # 公司规模
    district = scrapy.Field()  # 街区
    businessZones = scrapy.Field()  #地址




