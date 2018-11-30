#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 20:53
# @Author  : 海心
# @Site    : 
# @File    : hbase_data.py
# @Software: PyCharm
# @descri
import happybase
from django.db.models import Model, QuerySet

from userapp.models import ZPInfo

conn = happybase.Connection(host='192.168.43.195', port=9090, autoconnect=True)
conn.open()
table = conn.table('finalitems_zp')
datas = table.scan()



def get_hbase_data(num):
    """从hbase拿到数据  进行封装称models对象"""
    if int(num) == 11:
        for k1, data in datas:
            city = data.get(b'common:city').decode('utf-8')
            education = data.get(b'common:education').decode('utf-8')
            positionName = data.get(b'common:positionName').decode('utf-8')
            companyFullName = data.get(b'common:companyFullName').decode('utf-8')
            salary = data.get(b'common:salary').decode('utf-8')
            workYear = data.get(b'common:workYear').decode('utf-8')
            jobNature = data.get(b'common:jobNature').decode('utf-8')
            companySize = data.get(b'uncommon:companySize').decode('utf-8')
            # positionAdvantage = data.get(b'uncommon:positionAdvantage').decode('utf-8')


            ZPInfo(education=education, city=city, positionName=positionName, companyFullName=companyFullName,
                        salary=salary, workYear=workYear, jobNature=jobNature, company_size=companySize).save()
    return



