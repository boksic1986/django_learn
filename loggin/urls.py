# -*-coding:utf-8-*-
#! /user/bin/env python
# Author: jiucheng
# Date: 2018/4/10

from django.urls import path

from . import views

app_name = 'loggin'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('i/', views.indexs, name='indexs')
]