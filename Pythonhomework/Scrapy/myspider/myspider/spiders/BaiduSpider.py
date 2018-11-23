#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 21:18
# @Author  : 海心
# @Site    : 
# @File    : BaiduSpider.py
# @Software: PyCharm
# @descri #必须继承scrapy

import scrapy
# from lxml import etree

class BDSpider(scrapy.Spider):
    # 给爬虫取名字  唯一  区分
    name = 'bd'
    # 必须要有一个起始的url

    start_urls = ['http://www.baidu.com']
# 必须有一个解析的方法
    def parse(self, response):
        # html = etree.HTML(response.text)
        # print(html.xpath('//a/text()'))
        #底层已经封装了lxml  可以直接使用xpath语法
        # print(response.xpath('//a/text()'))#返一个选择器
        #想要data   需要序列化
        print(response.xpath('//a/text()').extract())#返一个选择器后使用extract进行解析，可以自动获取到选择器内的文本信息！

