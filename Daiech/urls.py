from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('apps.website.urls')),
    url(r'^update', 'apps.github.views.update'),
    url(r'^ads/(?P<id_ads>[-\w]+)$', 'apps.ads.views.home'),

    url(r'^admin/', include(admin.site.urls)),
)
