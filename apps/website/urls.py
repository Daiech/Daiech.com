from django.conf.urls import url, patterns

urlpatterns = patterns('apps.website.views',
    url(r'^$', 'home', name="home"),
    url(r'^pitch$', 'pitch', name="pitch"),
    url(r'^d-page$', 'dpage', name="d-page"),
)