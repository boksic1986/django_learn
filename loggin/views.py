from django.http import HttpResponse
from django.shortcuts import render

from . import models


# Create your views here.

def index(request):
    return HttpResponse("hello, world. You\'re at the polls index")


def indexs(request):
    last_question = models.Question.objects.order_by('-pub_date')[0]
    context = {'lsq':last_question}
    return render(request, 'index/index2.html', context)
    # return HttpResponse("hello, world. You\'re at the polls indexssssss  %s" % last_question)