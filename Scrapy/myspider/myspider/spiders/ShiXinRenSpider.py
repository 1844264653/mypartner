#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 21:06
# @Author  : 海心
# @Site    : 
# @File    : ShiXinRenSpider.py
# @Software: PyCharm
# @descri
# import json
#
# import scrapy
#
# from ..items import MyspiderItem
#
#
# class SXRSpider(scrapy.Spider):
#     name = 'shr'
#     headers = {
#         'Referer': 'Referer: https://www.baidu.com/s?wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA&rsv_spt=1&rsv_iqid=0xd609bc53000007a2&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=%25E4%25BA%25BA%25E4%25BA%25BA%25E7%25BD%2591&inputT=4103&rsv_t=284b4GKK9AtCD7tiOTYP1zvlPucgiWINKuuwdhMhPwufPfGhspZJaAnNGqS4bjC9fL2e&rsv_sug3=29&rsv_sug1=27&rsv_sug7=100&rsv_pq=dadd35d50000105a&rsv_sug2=0&rsv_sug4=4817',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
#     }
#
#     def start_requests(self):
#         # names = '赵钱孙李周吴郑王'
#         for i in range(1, 102):
#             print('第'+ str(i) + '页++++++++++++++++++++++++++++++++++++++')
#             url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E8%80%81%E8%B5%96&pn=" + str(
#                 i * 10) + "&ie=utf-8&oe=utf-8&format=json"
#             yield scrapy.Request(url=url, headers=self.headers)
#
#     def parse(self, response):
#         # 抽取信息
#         # print(type(response.text))  # str
#         item = MyspiderItem()
#         datas = json.loads(response.text)['data'][0]
#         # print(datas)
#
#         for data in datas['result']:
#             print(data,'++++++++++++++')
#             item['iname'] = data['iname']
#             item['cardNum'] = data['cardNum']
#             item['courtName'] = data['courtName']
#             item['areaName'] = data['areaName']
#             item['caseCode'] = data['caseCode']
#             item['duty'] = data['duty']
#             item['performance'] = data['performance']
#             item['disruptTypeName'] = data['disruptTypeName']
#             item['publishDate'] = data['publishDate']
#         yield item
