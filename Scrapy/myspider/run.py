#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 21:34
# @Author  : 海心
# @Site    : 运行文件
# @File    : run.py
# @Software: PyCharm
# @descri

from scrapy import cmdline

# cmdline.execute(['scrapy', 'crawl', 'bd'])
# cmdline.execute('scrapy crawl bd'.split())
# cmdline.execute(['scrapy', 'crawl', 'zl'])
# cmdline.execute(['scrapy', 'crawl', 'zph'])
# cmdline.execute(['scrapy', 'crawl', 'headers'])
# cmdline.execute(['scrapy', 'crawl', 'proxy'])
# cmdline.execute(['scrapy', 'crawl', 'shr'])
cmdline.execute(['scrapy', 'crawl', 'img'])
