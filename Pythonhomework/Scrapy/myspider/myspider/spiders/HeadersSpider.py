#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 9:38
# @Author  : 海心
# @Site    : Headers处理
# @File    : HeadersSpider.py
# @Software: PyCharm
# @descri    处理请求头

import scrapy


class HeadersSpider(scrapy.Spider):
    name = 'headers'

    # start_urls = ["http://httpbin.org/headers"]

    def start_requests(self):
        yield scrapy.Request('http://httpbin.org/headers',headers={'User-Agent':'headersSpider'})

    def parse(self, response):
        print(response.text)
