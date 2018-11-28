#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 9:47
# @Author  : 海心
# @Site    : 
# @File    : ProxySpider.py
# @Software: PyCharm
# @descri  : 代理IP

import scrapy


class ProxySpiders(scrapy.Spider):
    name = 'proxy'

    # {
    #     "origin": "61.158.149.202"
    # }

    def start_requests(self):
        # scrapy 的 IP  我无法直接丢在请求中  只能丢在Mmeta属性中！！

        # yield scrapy.Request('http://httpbin.org/ip')
        req = scrapy.Request('http://httpbin.org/ip')
        # meta   类字典结构  #ip  必须绑定到meta['proxy'] = 'http://ip:port'!!!
        req.meta['proxy'] = 'http://119.183.121.126:8118'
        yield req
    def parse(self, response):
        print(response.text)
