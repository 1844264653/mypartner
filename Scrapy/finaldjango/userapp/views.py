from traceback import print_exc

from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Model, Count
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from idna import unicode

from robotkiller.models import RobotKiller
from robotkiller.views import filterIP
from .models import Spider_user, ZPInfo
from .ip_crawler import get_ip_addr, get_params
from .hbase_data import get_hbase_data


# red = Redis(host='192.168.127.11',port=8000)
# pool = redis.ConnectionPool(host='192.168.43.9', port=7000, db=0, decode_responses=True)  # 选择直接输出 str
# red = redis.StrictRedis(connection_pool=pool)


def checkIP(request):
    try:
        filterIP(request)
    except Exception as e:
        if unicode(e) == 'user ip banned.':
            raise PermissionDenied()


# 注册  #    模板直接展示
# def regist(request):
#     """展示到注册界面"""
#     return render(request, 'register.html')

# 登录
# def login(requset):
#     """展示登录界面"""
#     return render(requset, 'login.html')


# 注册逻辑
def regist_logic(request):
    """如果注册 可以直接跳转到信息界面，自动登录即可？"""
    # 收集参数
    user = request.POST.get('userid')
    tel = request.POST.get('usrtel')
    email = request.POST.get('email')
    passwork = request.POST.get('psw')

    # 逻辑判断，用用户名是否存在
    # 存在
    if Spider_user.objects.filter(user=user):
        print('用户民已存在，请更换注册')
        message = '用户名那个已存在，请更换狂拽炫酷吊炸天的用户名.'
        return JsonResponse({'message': message})
    # JsonResponse   用户名已存在  做异步
    try:

        Spider_user(user=user, emailaddr=email, pwd=passwork, tel=tel).save()
        print('入库成功')
        request.session['user'] = user
        return render(request, 'main.html')
    except:
        print_exc()
        print('服务异常！')
    # 不存在即可注册  直接跳转到信息界面即可
    # 自动登录，用户信息保存session  如果登录课持续查看信息  否则只能查看前十页


# 登录逻辑
def ligin_logic(request):
    """
    处理登录逻辑  如果账户不存在则询问是否返回注册界面  成功登录跳转到信息界面
    :param requset: 请求
    :return:
    """
    # 收集参数
    user = request.POST.get('userid')
    password = request.POST.get('psw')
    # 数据库校验
    try:
        Spider_user.objects.get(uer=user, pwd=password)  # get 方法，数据为空或者有多个时会抛出异常
        print('可以登录')
        # 保存session
        request.session['user'] = user
        return render(request, 'main.html')
    except:
        print('登录失败，用户名密码不匹配')
        message = '登录失败，用户名密码不匹配'
        return JsonResponse({'message': message})


# 展示main页面
def main_page(request):
    checkIP(request)
    print(request.META.get('HTTP_HOST'))
    print(request.META.get('REMOTE_ADDR'))

    return render(request, 'main.html')


# 展示详情   需要分页
def menu_page(request):
    checkIP(request)  # 检测ip
    user_ip = request.META['REMOTE_ADDR']  # 获取请求的ip

    loction = get_ip_addr(user_ip=user_ip).get('location')  # 获取ip的位置信息
    # 收集参数
    user = request.session.get('user')
    num = request.GET.get('num')
    city = request.GET.get('city')
    positionName = request.GET.get('job')
    request.session['city'] = city
    request.session['positionName'] = positionName
    request.session['num'] = num
    city = request.session.get('city')
    positionName = request.session.get('positionName')
    if not num:  # 处理初始页码
        num = 1

    # mysql 拿数据
    zpxxs = ZPInfo.objects.all()
    zpxx = zpxxs.filter(pk__lt=10000)
    count = len(zpxxs)
    #  收集request带过来的参数   存入redis作为临时数据缓存
    try:
        get_params(user_ip=user_ip, city=city, job=positionName, numpage=num, location=loction)
    except:
        pass
    if int(num) > 10:
        get_hbase_data()
        restdata = ZPInfo.objects.filter(pk__gt=count)
        zpxx = zpxx.extend(restdata)
        if not user:  ## 未登录 只能查看前十页的数据
            return redirect('indexs:login')

    if city and positionName:
        zpxx = zpxx.filter(positionName__contains=positionName, city=city)
    # else:
    #     zpxx = zpxx.filter(positionName__contains='大数据',city='广州')

    page_obj = Paginator(object_list=zpxx, per_page=10).page(int(num))
    print(user, num, city, positionName, '++++++++++++++++++++++++++++')

    return render(request, 'menu.html', {'page_obj': page_obj})


# def filterIP(request):
#     domain = request.META.get('REMOTE_HOST')
#     white_list = ['googlebot.com', 'crawl.baidu.com', 'sogou.com', 'bing.com', 'yahoo.com']
#     for bot_domain in white_list:
#         if domain.find(bot_domain) > 0:
#             return bot_domain
#
#     user_ip = request.META['REMOTE_ADDR']  # 获取请求的ip
#
#     try:
#         record = RobotKiller.objects.get(t_ip=user_ip)  # 空或者多个  会报错
#     except RobotKiller.DoesNotExist:
#         RobotKiller(t_ip=user_ip, visits=1, t_time=timezone.now()).save()
#         red.set('ip'+user_ip, user_ip, ex=600, px=60000)  # 存入reids缓存  ex  秒   px  毫秒
#         return
#
#     passed_seconds = (timezone.now() - record.time).seconds
#
#     if record.visits > max_visits and passed_seconds < min_seconds:
#         raise Exception('user ip banned.')
#     else:
#         if passed_seconds < min_seconds:
#             record.visits = record.visits + 1
#             red.set('visits'+user_ip, record.visits, ex=60, px=6000)  # 存入redis
#             record.save()
#         else:
#             record.visits = 1
#             record.time = timezone.now()
#             record.save()


def show_tables(request):
    """数据整理可视化异步"""
    # cityinfos = ZPInfo.objects.values_list('city').annotate(Count('id')).order_by('-id')
    citys = ZPInfo.objects.values_list('city').annotate(Count('city'))  # <QuerySet [('广州', 1131), ('北京', 5100), ('上海', 4100), ('深圳', 1128)]>
    citydata = {
        'key': [i[0] for i in citys],
        'value': [i[1] for i in citys],
    }

    # jsondata = {'datas': {'citys': citydata, 'jobs': jobdata, 'ips': ips}}
    # return JsonResponse(jsondata,safe=False)
    return JsonResponse(citydata)


def show_bin(request):
    jobs = ZPInfo.objects.values_list('positionName').annotate(Count('positionName'))
    jobdata = {
        'key': [j[0] for j in jobs],
        'value': [j[1] for j in jobs],

    }
    return JsonResponse(jobdata)


def show_maps(request):
    ips = RobotKiller.objects.values_list('t_ip').annotate(Count('t_ip'))
    ipsdata = {
        'key':[k[0] for k in ips],
        'value':[k[1] for k in ips],
    }
    return JsonResponse(ipsdata)