from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


# Create your views here.


def index(request):
    return HttpResponse('hello to the book index!')

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
    else:
        form = NameForm()
    return render(request, 'book/index.html', {'form':form})


def show_name(request):
    if request.method == 'POST':
        form = request.POST
        return  render(request, 'book/index.html', {'form':form})