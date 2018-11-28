from django.db import models

# Create your models here.

class Spider_user(models.Model):
    user = models.CharField(max_length=200,db_column='t_user')
    tel = models.CharField(max_length=200,default='暂无')
    emailaddr = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    registtime = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=1)
    to_set = models.CharField(default=None,max_length=200)

    class Meta:
        db_table = 'spideruser'



class ZPInfo(models.Model):  # 拿智联的备用信息
    positionName = models.CharField(max_length=200)   # 职位
    companyFullName = models.CharField(max_length=200)  #  公司全名
    businessZones = models.CharField(max_length=200)  #公司详细地址
    salary = models.CharField(max_length=200)  #月薪
    workYear = models.CharField(max_length=200)  #工作经验
    education = models.CharField(max_length=200)  #教育经历
    renshu = models.CharField(max_length=200)   #招聘人数
    jobNature = models.CharField(max_length=200)  #工作要求  例如 计算机软件  计算机硬件
    xingzhi = models.CharField(max_length=200)   #  公司性质
    company_size = models.CharField(max_length=200)  #公司规模
    guanwang = models.CharField(max_length=200)  #公司官网
    # date_time = models.DateField()  #数据填充时间
    status = models.BooleanField(default=1)
    city = models.CharField(max_length=200)  #城市

    class Meta:
        db_table = 'zlzp'

