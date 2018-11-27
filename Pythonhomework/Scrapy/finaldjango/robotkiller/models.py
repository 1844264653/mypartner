from django.db import models

# Create your models here.


class RobotKiller(models.Model):
    id = models.IntegerField(primary_key=True)
    t_ip = models.CharField(max_length=200)    #IP地址
    visits = models.IntegerField()          #请求次数
    t_time = models.DateTimeField()           #第一次发起请求的时间
    class Meta:
        db_table = 'robotkiller'