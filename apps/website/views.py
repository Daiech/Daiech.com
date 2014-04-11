# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from Daiech_com import settings

def home(request):
    ctx = {'TITLE':"Bienvenido a Daiech","URL_BASE":settings.URL_BASE}
    return render_to_response('website/index.html', ctx, context_instance = RequestContext(request))


def log_in(request):
    return render_to_response('website/login.html', {}, context_instance = RequestContext(request))
