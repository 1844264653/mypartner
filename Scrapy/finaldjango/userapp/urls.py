from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('checkIP/', views.checkIP, name='checkIP'),

    path('regist/', TemplateView.as_view(template_name='register.html'), name='regist'),

    path('regist_logic/', views.regist_logic, name='regist_logic'),

    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),

    path('login_logic/', views.ligin_logic, name='login_logic'),
    path('main/', views.main_page, name='main'),
    path('menu/', views.menu_page, name='menu'),

    path('echarts/', TemplateView.as_view(template_name='echarts.html'), name='echarts-url'),
    path('api/echarts/', views.show_tables, name='api-echarts'),
    path('api/echarts1/', views.show_bin, name='api-echarts1'),
    path('api/echarts2/', views.show_maps, name='api-echarts1'),

]
