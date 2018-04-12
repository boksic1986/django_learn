# -*-coding:utf-8-*-
#! /user/bin/env python
# Author: jiucheng
# Date: 2018/4/10

from django import forms


class TestQuestion(forms.Form):
    a = forms.CharField(max_length=100)