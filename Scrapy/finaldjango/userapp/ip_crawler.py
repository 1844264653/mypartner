#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 20:23
# @Author  : 海心
# @Site    : ip_crawler
# @File    : ip_crawler.py
# @Software: PyCharm
# @descri  :  爬取ip数据
import json

import redis
import requests

pool = redis.ConnectionPool(host='192.168.43.9', port=7000, db=0, decode_responses=True)  # 选择直接输出 str
red = redis.StrictRedis(connection_pool=pool)


def get_ip_addr(user_ip):
    url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?&co=&resource_id=6006&t=1543321547838&ie=utf8&oe=gbk&format=json&tn=baidu'
    params = {
        'query': user_ip
    }
    headers = {
        'Referer': 'https://www.baidu.com/s?ie=utf-8&f=3',
        # 'Cookie':'BAIDUID=C770D61F15B4A3FF4E70F5ABDCFE884C:FG=1; BIDUPSID=C770D61F15B4A3FF4E70F5ABDCFE884C; PSTM=1539594963; H_PS_PSSID=1437_21098_26350_27508; delPer=0; PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'sp0.baidu.com',
    }
    cookies = {
        'Cookie': 'BAIDUID=C770D61F15B4A3FF4E70F5ABDCFE884C:FG=1; BIDUPSID=C770D61F15B4A3FF4E70F5ABDCFE884C; PSTM=1539594963; H_PS_PSSID=1437_21098_26350_27508; delPer=0; PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598'
    }
    data = requests.get(url=url, params=params, headers=headers, cookies=cookies).text
    data = json.loads(data)
    print(data.get('data')[0].get('location'))
    location = data.get('data')[0].get('location')
    return {'location': location}


def outer(func):
    print('+++++++++++++')

    def my_decorate(user_ip='', city='', job='', numpage='', location=''):
        # 获得信息存入 redis
        try:
            red.set('user_ip' + user_ip, user_ip)
            print(user_ip)
        except:
            pass
        try:
            red.set('city' + city, city)
            print(city)
        except:
            pass
        try:
            red.set('job' + job, job)
            print(job)
        except:
            pass
        try:
            red.set('numpage' + numpage, numpage)
            print(numpage)
        except:
            pass
        try:
            red.set('location' + location, location)
            print(location)
        except:
            pass
        return func()

    return my_decorate


@outer
def get_params(user_ip, city, job, numpage, location):
    red.set('user_ip' + user_ip, user_ip)
    print(user_ip)
    red.set('city' + city, city)
    print(city)
    red.set('job' + job, job)
    print(job)
    red.set('numpage' + numpage, numpage)
    print(numpage)
    red.set('location' + location, location)
    print(location)
    return
