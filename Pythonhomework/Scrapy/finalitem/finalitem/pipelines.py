# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

import happybase


class FinalitemPipeline(object):

    def __init__(self):

        self.conn1 = MySQLdb.connect(
            host='127.0.0.1', port=3306,
            user='root', password='123456', charset='utf8', db='spider'
        )  # mysql  连接

        pool = happybase.ConnectionPool(size=5, host='hadoop1.hxd.com', table_prefix='myproject_wh')  # 设置连接池
        # self.conn2 = happybase.Connection(host="hadoop1.hxd.com", port=50070,  autoconnect=True)
        with pool.connection() as self.conn2:  # 建立网络连接
            families = {
                "commmon": dict(),
                "uncommon": dict(),
            }
            self.conn2.create_table('zp', families)  # 建表
            self.table = self.conn2.table('zp')  # 创建表实例

    def process_item(self, item, spider):
        self.save(item)
        return item

    def save(self, item):

        # 从mysql数据库查询条数[目前只能想到这个笨方法]
        req_count = 'select count(id) from finalitems'
        if int(req_count) <= 1000:
            print(req_count, '+++++++++++++++++++++++++++++++')
            sql = 'insert into finalitems(positionName,companyFullName,salary,jobNature,workYear,education,city,positionAdvantage,companySize,district,businessZones)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            self.conn1.cursor().execute(sql, [item['positionName'], item['companyFullName'], item['salary'],
                                              item['jobNature'], item['workYear'], item['education'], item['city'],
                                              item['positionAdvantage'], item['companySize'], item['district'],
                                              item['businessZones']])
            self.conn1.commit()
        else:
            print(req_count, '+++++++++++++++++++++++++++++')
            with self.table.batch(batch_size=10)as bat:
                bat.put(item['ctiy'] + str(req_count), {'common:' + item['positionName']: item['positionName'],
                                                        'common:' + item['companyFullName']: item['companyFullName'],
                                                        'common:' + item['salary']: item['salary'],
                                                        'common:' + item['jobNature']: item['jobNature'],
                                                        'common:' + item['workYear']: item['workYear'],
                                                        'common:' + item['education']: item['education'],
                                                        'common:' + item['city']: item['city'],  # # common 展示的数据
                                                        'uncommon:' + item['positionAdvantage']: item[
                                                            'positionAdvantage'],
                                                        'uncommon:' + item['companySize']: item['companySize'],
                                                        'uncommon:' + item['businessZones']: item['businessZones'],
                                                        })  # uncommon  非展示的数据入库
                req_count = int(req_count) + 1
