#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 9:07
# @Author  : 海心
# @Site    : 
# @File    : zhipinhuiSpider.py
# @Software: PyCharm
# @descri
import scrapy as scrapy


class ZPHSpider(scrapy.Spider):
    name = 'zph'
    # start_urls =   需要传参数   所以这个方法不合适
    def start_requests(self):
        """用来发送post请求"""
        url = 'http://www.honestcareer.com/hr/dologin'
        formdata = {
            'type': '1',
            'username': '18501279410',
            'password': 'hbw123'
        }
        yield scrapy.FormRequest(url=url,formdata=formdata)
    def parse(self, response):
        yield scrapy.Request('http://www.honestcareer.com/hr/index', callback=self.parse1)
        # print(response.text)
    def parse1(self,resp):
        print(resp.text)