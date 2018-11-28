#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 8:31
# @Author  : 海心
# @Site    : 
# @File    : ImageSpider.py
# @Software: PyCharm
# @descri  : 爬取图片下载
import json

import scrapy

from ..items import MyImageItem


class ImgSpider(scrapy.Spider):
    name='img'
    index=0
    def start_requests(self):
        yield scrapy.Request(url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%96%97%E5%9B%BE%E8%A1%A8%E6%83%85%E5%8C%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E6%96%97%E5%9B%BE%E8%A1%A8%E6%83%85%E5%8C%85&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&pn=0&rn=30&gsm=1e&1542695319470=')
    def parse(self, response):
        if self.index<=100:
            item=MyImageItem()
            image_urls=[]
            for data in json.loads(response.text)['data']:
                try:
                    image_urls.append(data['thumbURL'])
                except:
                    pass
            item['image_urls']=image_urls
            item['image_store']='第'+str(int(self.index/30)+1)+'页'
            yield item
            self.index+=30
            yield scrapy.Request('https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%96%97%E5%9B%BE%E8%A1%A8%E6%83%85%E5%8C%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E6%96%97%E5%9B%BE%E8%A1%A8%E6%83%85%E5%8C%85&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&pn='+str(self.index)+'&rn=30&gsm=1e&1542695319470=',meta={'test':'1'})
