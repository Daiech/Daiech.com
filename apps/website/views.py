# Create your views here.
from django.shortcuts import render
from django.template import RequestContext
from django.utils import translation
from django.conf import settings


def home(request):
    if request.method == "GET" and 'lang' in request.GET:
        try:
            lang_available = False
            for l in settings.LANGUAGES:
                if request.GET.get("lang") in l:
                    lang_available = True
            if lang_available:
                request.session['django_language'] = request.GET.get("lang")
                translation.activate(request.GET.get("lang"))
            else:
                ctx["no_supported"] = True
        except Exception, e:
            print e
    return render(request, 'website/index.html', locals())


def pitch(request):
    return render(request, 'website/pitch.html', locals())


def dpage(request):
    return render(request, 'website/dpage.html', locals())


def log_in(request):
    return render(request, 'website/login.html', {})
