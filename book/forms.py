# -*-coding:utf-8-*-
#! /user/bin/env python
# Author: jiucheng
# Date: 2018/4/12

from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

