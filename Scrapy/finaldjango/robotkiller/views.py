import redis
from django.shortcuts import render

# Create your views here.


from django.utils import timezone

# from redis import Redis

from .models import RobotKiller

# red = Redis(host='192.168.127.11',port=8000)
pool = redis.ConnectionPool(host='192.168.43.9', port=7000, db=0, decode_responses=True)  # 选择直接输出 str
red = redis.StrictRedis(connection_pool=pool)

max_visits = 60
min_seconds = 60


def filterIP(request):
    domain = request.META.get('REMOTE_HOST')
    white_list = ['googlebot.com', 'crawl.baidu.com', 'sogou.com', 'bing.com', 'yahoo.com']
    for bot_domain in white_list:
        if domain.find(bot_domain) > 0:
            return bot_domain

    user_ip = request.META['REMOTE_ADDR']  # 获取请求的ip

    try:
        record = RobotKiller.objects.get(t_ip=user_ip)  # 空或者多个  会报错
    except RobotKiller.DoesNotExist:
        RobotKiller(t_ip=user_ip, visits=1, t_time=timezone.now()).save()
        red.set('ip'+user_ip, user_ip, ex=600, px=60000)  # 存入reids缓存  ex  秒   px  毫秒
        return

    passed_seconds = (timezone.now() - record.time).seconds

    if record.visits > max_visits and passed_seconds < min_seconds:
        raise Exception('user ip banned.')
    else:
        if passed_seconds < min_seconds:
            record.visits = record.visits + 1
            red.set('visits'+user_ip, record.visits, ex=60, px=6000)  # 存入redis
            record.save()
        else:
            record.visits = 1
            record.time = timezone.now()
            record.save()
