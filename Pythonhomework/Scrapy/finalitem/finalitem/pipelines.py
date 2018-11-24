# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

from .spiders.lagou import req_count
import happybase


class FinalitemPipeline(object):
    def __init__(self):
        if req_count <= 1000:
            self.conn1 = MySQLdb.connect(
                host='127.0.0.1', port=3306,
                user='root', password='123456', charset='utf8', db='spider'
            )
        else:
            self.conn2 = happybase.Connection(host="???", port=9090)
            self.conn2.open()
            self.table = self.conn2.table('baizhi125:user')

    def process_item(self, item, spider):
        self.save(item)

        return item

    def save(self, item):
        if req_count <= 1000:
            sql = 'insert into finalitems(positionName,companyFullName,salary,jobNature,workYear,education,city,positionAdvantage,companySize,district,businessZones)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            self.conn1.cursor().execute(sql, [item['positionName'], item['companyFullName'], item['salary'],
                                             item['jobNature'], item['workYear'], item['education'], item['city'],
                                             item['positionAdvantage'], item['companySize'], item['district'],
                                             item['businessZones']])
            self.conn1.commit()
        else:
            self.table.put("rowkey:",{"base:name":'value'})#等待编辑字段！  很可能不用写。因为爬不了那么多哈哈哈