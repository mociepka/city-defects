from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('citydefects.views',
    url(r'^$', 'home', name='home'),
    url(r'^api/streets/$', 'street_cache', name='streets'),
    url(r'^api/', include('defect.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }),
    )
