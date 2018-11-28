import json
import random
import time

import scrapy

from ..items import FinalitemItem
from ..settings import IPS



class LagouSpider(scrapy.Spider):
    name = 'lg'

    def start_requests(self):
        # citys = ['%E5%8C%97%E4%BA%AC', '%E4%B8%8A%E6%B5%B7', '%E6%B7%B1%E5%9C%B3', '%E5%B9%BF%E5%B7%9E']
        jobs = ['python', 'python web', '爬虫', 'AI']
        # for city in citys:
        url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': '_ga=GA1.2.933299604.1542897027; _gid=GA1.2.788367443.1542897027; user_trace_token=20181122223028-28bc3167-ee63-11e8-8adb-5254005c3644; LGUID=20181122223028-28bc3542-ee63-11e8-8adb-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGFABEF53DF3AB8571140915EE9E256D19A31DC; TG-TRACK-CODE=index_search; LGSID=20181123211848-4ff8f3d1-ef22-11e8-b78d-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D-uLgZFW3bZOsNEzCvHPiDW9ratUJLcloz4fo9hlsOPa%26ck%3D2610.1.60.231.156.226.144.253%26shh%3Dwww.baidu.com%26sht%3Dbaidu%26wd%3D%26eqid%3Da715324e0001fa30000000025bf7fe30; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gat=1; SEARCH_ID=b2dfac9ae4eb4bec8e486e8c4b6236b9; LGRID=20181123213048-fd6d1931-ef23-11e8-8b1c-5254005c3644',
            'Referer': 'https://www.lagou.com/jobs/list_python%20web?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
            'User-Agent': random.choice(IPS),
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With': 'XMLHttpRequest',
        }
        for job in jobs:
            i = 1
            while True:
                formdata = {
                    'first': 'false',
                    'pn': str(i),
                    'kd': job,
                }
                i += 1
                time.sleep(1)
                yield scrapy.FormRequest(url=url, formdata=formdata, headers=headers)

    def parse(self, response):
        data = json.loads(response.text)
        item = FinalitemItem()
        print(data['content']['positionResult']['result'])  # 字典列表
        for detailinfo in data['content']['positionResult']['result']:
            # positionName = detailinfo['positionName']  # 职位
            # companyFullName = detailinfo['companyFullName']  # 公司名字
            # salary = detailinfo['salary']  # 薪水
            # jobNature = detailinfo['jobNature']  # 任职要求
            # workYear = detailinfo['workYear']  # 经验要求
            # education = detailinfo['education']  # 学历要求
            # city = detailinfo['city']  # 城市
            # positionAdvantage = detailinfo['positionAdvantage']  # 公司福利
            # companySize = detailinfo['companySize']  # 公司规模
            # district = detailinfo['district']  # 街区
            businessZones = ''
            try:
                for area in detailinfo['businessZones']:
                    businessZones = businessZones + area
            except:
                businessZones = '还没做好呢'

            # print(locals())

            item['positionName'] = detailinfo['positionName']
            item['companyFullName'] = detailinfo['companyFullName']
            item['salary'] = detailinfo['salary']
            item['jobNature'] = detailinfo['jobNature']
            item['workYear'] = detailinfo['workYear']
            item['education'] = detailinfo['education']
            item['city'] = detailinfo['city']
            item['positionAdvantage'] = detailinfo['positionAdvantage']
            item['companySize'] = detailinfo['companySize']
            item['district'] = detailinfo['district']
            item['businessZones'] = detailinfo['businessZones']
            yield item
