# Create your views here.
from django.shortcuts import render
from django.template import RequestContext


def home(request):
    return render(request, 'website/index.html', locals())


def log_in(request):
    return render(request, 'website/login.html', {})
