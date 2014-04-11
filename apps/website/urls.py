from django.conf.urls import url, patterns

urlpatterns = patterns('apps.website.views',
    url(r'^$', 'home', name="home"),
)