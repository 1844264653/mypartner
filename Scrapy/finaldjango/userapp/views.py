from traceback import print_exc

from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from idna import unicode

from ..robotkiller.views import filterIP
from .models import Spider_user, ZPInfo
from .ip_crawler import get_ip_addr, get_params



def checkIP(request):
    try:
        filterIP(request)
    except Exception as e:
        if unicode(e) == 'user ip banned.':
            raise PermissionDenied()


# 注册
def regist(request):
    """展示到注册界面"""
    return render(request, 'register.html')


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


# 登录
def login(requset):
    """展示登录界面"""
    return render(requset, 'login.html')


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
    checkIP(request)  #  检测ip
    user_ip = request.META['REMOTE_ADDR']  # 获取请求的ip
    loction = get_ip_addr(user_ip=user_ip).get('location')

    user = request.session.get('user')
    # 收集参数
    num = request.GET.get('num')
    city = request.GET.get('city')
    positionName = request.GET.get('job')
    request.session['city'] = city
    request.session['positionName'] = positionName
    request.session['num'] = num
    city = request.session.get('city')
    positionName = request.session.get('positionName')
    if not num:
        num = 1
    zpxx = ZPInfo.objects.all()
    if city and positionName:
        zpxx = zpxx.filter(positionName__contains=positionName, city=city)
    zpxx = zpxx[0:2000]  # mysql 只要前1000条数据

    page_obj = Paginator(object_list=zpxx, per_page=100).page(int(num))
    print(user, num, city, positionName, '++++++++++++++++++++++++++++')

    #  收集request带过来的参数   存入redis作为临时数据缓存
    get_params(user_ip=user_ip, city=city, job=positionName, numpage=num, location=loction)
    if not user and int(num) > 10:  # 未登录 只能查看前十页的数据
        return redirect('indexs:login')
    else:
        return render(request, 'menu.html', {'page_obj': page_obj})
