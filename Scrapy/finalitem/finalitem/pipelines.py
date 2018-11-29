# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

import happybase

req_count = 1000


class FinalitemPipeline(object):

    def __init__(self):
        # self.conn1 = MySQLdb.connect(
        #     host='127.0.0.1', port=3306,
        #     user='root', password='123456', charset='utf8', db='spider'
        # )  # mysql  连接

        self.conn2 = happybase.Connection(host='192.168.43.195', port=9090, autoconnect=True, table_prefix='finalitems')
        # pool = happybase.ConnectionPool(size=3, host='192.168.43.195', port=9090,
        #                                 table_prefix='myproject_hw')  # 设置连接池        # self.conn2 = happybase.Connection(host="hadoop1.hxd.com", port=50070,  autoconnect=True)
        # with pool.connection() as self.conn2:  # 建立网络连接
        self.conn2.open()
        families = {
            "common": dict(),
            "uncommon": dict(),
        }
        self.conn2.create_table('zp', families)  # 建表
        self.table = self.conn2.table('zp')  # 创建表实例

    def process_item(self, item, spider):
        self.save(item)
        return item

    def save(self, item):
        global req_count

        # 从mysql数据库查询条数[目前只能想到这个笨方法]
        # req_count = 'select count(id) from finalitems'
        # if int(req_count) <= 1000:
        #     print(req_count, '+++++++++++++++++++++++++++++++')
        #     sql = 'insert into finalitems(positionName,companyFullName,salary,jobNature,workYear,education,city,positionAdvantage,companySize,district,businessZones)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        #     self.conn1.cursor().execute(sql, [item['positionName'], item['companyFullName'], item['salary'],
        #                                       item['jobNature'], item['workYear'], item['education'], item['city'],
        #                                       item['positionAdvantage'], item['companySize'], item['district'],
        #                                       item['businessZones']])
        #     self.conn1.commit()
        # else:
        #     print(req_count, '+++++++++++++++++++++++++++++')

        print(req_count,item['city'], '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        self.table.put(item['city'] + item['positionName'] + str(req_count),  # rowkey
                                            {'common:positionName': item['positionName'],
                                             'common:companyFullName': item['companyFullName'],
                                             'common:salary': item['salary'],
                                             'common:jobNature': item['jobNature'],
                                             'common:workYear': item['workYear'],
                                             'common:education': item['education'],
                                             'common:city': item['city'],
                                # # common 展示的数据
                                             'uncommon:positionAdvantage': item['positionAdvantage'],
                                             'uncommon:companySize': item['companySize'],
                                             # 'uncommon:businessZones': item['businessZones'],
                                            })  # uncommon  非展示的数据入库
        print('haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        req_count = req_count + 1
        print('+++++ahhhhhhhhhhh++++++++++++')
