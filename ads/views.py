#encoding:utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request, id_ads):
    ctx = {}
    return render_to_response('ads/banner1.html', ctx, context_instance=RequestContext(request))
