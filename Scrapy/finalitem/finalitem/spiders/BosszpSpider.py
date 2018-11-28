import random

import scrapy
from lxml import etree
from ..settings import USER_AGENT


class BosszpSpider(scrapy.Spider):
    name = 'boss'

    def start_requests(self):
        citys = ['c101280600', 'c101010100', 'c101020100', 'c101280100']
        jobs = ['python', 'python+web', '爬虫', 'AI']
        headers = {
            'referer': 'https://www.zhipin.com/job_detail/?query=ai&scity=101280100&industry=&position=',
            'upgrade-insecure-requests': '1',
            'user-agent': random.choice([USER_AGENT])

        }
        for city in citys:
            page = 1
            for job in jobs:
                url = 'https://www.zhipin.com/' + city + '/?query=' + job + '&page=' + str(page) + '&ka=page-' + str(
                    page)
                yield scrapy.Request(url=url, headers=headers)

    def parse(self, response):
        resp = response.text
        cookies = {

        }
        # print(resp)
        html = etree.HTML(resp)
        detai_urls = html.xpath('//div[@class="info-primary"]/descendant::a/@href')
        # print(detai_urls,len(detai_urls),'++++++++++++++++++++++++++')#  16页
        for url in detai_urls:
            real_url = 'https://www.zhipin.com' + url
            yield scrapy.Request(url=real_url, callback=self.detai_parse, cookies=cookies)

    def detai_parse(self, response):
        resp = response.text
        html = etree.HTML(resp)
        print(html)
