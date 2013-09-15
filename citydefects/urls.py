from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('citydefects.views',
    url(r'^$', 'home', name='home'),
    url(r'^api/streets/$', 'street_cache', name='streets'),
    url(r'^api/', include('defect.urls')),
)
