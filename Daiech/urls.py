from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Daiech.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('apps.website.urls')),
    url(r'^update', 'apps.github.views.update'),
    url(r'^ads/(?P<id_ads>[-\w]+)$', 'apps.ads.views.home'),

    url(r'^admin/', include(admin.site.urls)),
)
