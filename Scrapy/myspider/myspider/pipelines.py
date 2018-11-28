# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import uuid

import MySQLdb
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from sqlalchemy import create_engine
import pandas as pd


# class MyspiderPipeline(object):
#     """用来u处理数据，接收item  配置文件中有优先级
#         编写完pipeline需要在pipeline进行配置权限定名——从根目录到类的路劲
#         和这个pipeline对应的优先级，是一个数字
#         数字越小优先级高——可以配置储存到数据库、hbase、redis等不同的权限
#         写不同的pipeline"""
#     def process_item(self, item, spider):
#         return item

# class MyspiderPipeline(object):
#     """用来u处理数据，接收item  配置文件中有优先级
#         编写完pipeline需要在pipeline进行配置权限定名——从根目录到类的路劲
#         和这个pipeline对应的优先级，是一个数字
#         数字越小优先级高——可以配置储存到数据库、hbase、redis等不同的权限
#         写不同的pipeline"""
#
#     def __init__(self):
#         # #########################写出数据到mysql#########################################
#         # self.connect = create_engine('mysql+mysqldb://root:123456@localhost:3306/spider?charset=utf8')
#         # pd.io.sql.to_sql(datas, 't_shixin', connect, schema='spider', if_exists='append', index=False)
#         self.conn = MySQLdb.connect(
#             host='127.0.0.1', port=3306,
#             user='root', password='123456', charset='utf8', db='spider'
#         )
#
#     def process_item(self, item, spider):
#         # 可以拓展过滤
#         self.save(item)
#         return item
#
#     def save(self, item):
#         # item.get('title'),item.get('salary')
#         # 将数据组织成数据框
#         # item = {'title':item['title'],'salary':item['salary']}
#         # item = pd.DataFrame(item)
#         # 去重  这里没必要
#         # item = item.drop_duplicates()
#         # 入库
#         # pd.io.sql.to_sql(item, 'zlzhaopin', self.connect, schema='spider', if_exists='append', index=False)
#         sql = 'insert into zlzhaopin(title,salary)VALUES (%s,%s)'
#         self.conn.cursor().execute(sql, [item['title'], item['salary']])
#         self.conn.commit()
#         return item

# class MyspiderPipeline(object):
#
#     def __init__(self):
#         self.conn = MySQLdb.connect(
#             host='127.0.0.1', port=3306,
#             user='root', password='123456', charset='utf8', db='spider'
#         )
#
#     def process_item(self, item, spider):
#         self.save(item)
#         return item
#
#     def save(self, item):
#         iname = item['iname']
#         cardNum = item['cardNum']
#         courtName = item['courtName']
#         areaName = item['areaName']
#         caseCode = item['caseCode']
#         duty = item['duty']
#         performance = item['performance']
#         disruptTypeName = item['disruptTypeName']
#         publishDate = item['publishDate']
#         print([iname, cardNum, courtName, areaName, caseCode, duty, performance, disruptTypeName, publishDate])
#         sql = "insert into shixinren(name,cardNum,courtName,areaName,caseCode,duty,performance,disruptTypeName,publishDate)values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#         self.conn.cursor().execute(sql,
#                                    [iname, cardNum, courtName, areaName, caseCode, duty, performance, disruptTypeName,
#                                     publishDate])
#         self.conn.commit()
#         return item



class MyImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [scrapy.Request(x,meta={'item':item}) for x in item.get(self.images_urls_field, [])]
    def file_path(self, request, response=None, info=None):
        filepath=request.meta['item']['image_store']+'/'+str(uuid.uuid4())+'.jpg'
        print(filepath)
        return filepath