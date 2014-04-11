# Create your views here.
from django.shortcuts import render
from django.template import RequestContext


def home(request):
    ctx = {'title':"Bienvenido a Daiech"}
    return render(request, 'website/index.html')


def log_in(request):
    return render(request, 'website/login.html', {})
