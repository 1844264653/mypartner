

from django.urls import path

from . import views

urlpatterns = [

    path('filter/', views.filterIP, name='filter'),  # 介绍   #暂时无用

]