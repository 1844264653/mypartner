#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 22:04
# @Author  : 海心
# @Site    : 
# @File    : ZLZhaopinSpider.py
# @Software: PyCharm
# @descri   爬取智联
# import json
#
# import scrapy
# from ..items import MyspiderItem
#
#
# class ZLSpider(scrapy.Spider):
#     name = 'zl'
#
#     # 另一种创建起始链接方式
#     def start_requests(self):
#         city_ids = ['530', '538', '765', '763']
#         kws = ['AI', '爬虫', '大数据', 'python web']
#         for city_id in city_ids:
#             for kw in kws:
#                 yield scrapy.Request(url='https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=' +
#                                          city_id + '&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=' + \
#                                          kw + '&kt=3&_v=0.32069266&x-zp-page-request-id=3f968250f3c34bb684f49471e62bcad0-1542178189207-705386&start=0')
#
#     def parse(self, response):
#         # 抽取三级url
#         datas = json.loads(response.text)['data']
#         for data in datas['results']:
#             yield scrapy.Request(data['positionURL'], callback=self.detail)
#             # 构造二级链接
#         num = datas['numFound']
#         strs = response.url.split('start=')
#         number = int(strs[1]) + 60
#         if number < num:
#             url = strs[0] + 'start=' + str(number)
#             yield scrapy.Request(url)
#
#         # print(json.loads(response.text))
#
#     def detail(self, resp):
#         item = MyspiderItem()  # 导入item  入库准备
#         item['title'] = resp.xpath('//h1/text()')[0].extract()
#         item['salary'] = resp.xpath('//li[@class="info-money"]/strong/text()')[0].extract()
#         # print(title)
#         # print(salary)
#         # 交给引擎   #不能忘记去打开配置信息！~！！！
#         yield item
