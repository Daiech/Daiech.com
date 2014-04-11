# def gloval_vars_url(request):
#     from apps.website.views import getGlobalVar
#     return {"URL_PRIVACY": getGlobalVar("URL_PRIVACY"), "URL_TERMS": getGlobalVar("URL_TERMS")}


def is_debug(request):
    from django.conf import settings
    return {"DEBUG": settings.DEBUG}

