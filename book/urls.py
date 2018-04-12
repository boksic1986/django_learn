# -*-coding:utf-8-*-
#! /user/bin/env python
# Author: jiucheng
# Date: 2018/4/12

from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('', views.index, name='index'),
    path('name/', views.get_name, name='book'),
    path('your/', views.show_name)
]
