from django.urls import path
from . import views

urlpatterns = [
    # path("index/",views.index,name='index'),#二级命名
    #     path('logout/', views.logout, name='logout') , # 登出功能
    #     path("category/",views.booklist,name='category'),#二级命名
    #     path('register/',views.register,name='register'),#二级命名
    path('checkIP/', views.checkIP, name='checkIP'),
    path('regist/', views.regist, name='regist'),
    path('regist_logic/', views.regist_logic, name='regist_logic'),
    path('login/', views.login, name='login'),
    path('login_logic/', views.ligin_logic, name='login_logic'),
    path('main/', views.main_page, name='main'),
    path('menu/', views.menu_page, name='menu'),

]
