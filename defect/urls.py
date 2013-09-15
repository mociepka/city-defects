from django.conf.urls import patterns, include, url

from .api import router

urlpatterns = patterns('',
    url(r'defects/(?P<defect_id>[0-9]+)/addimage/', 'defect.views.addimage'),
    url(r'', include(router.urls)),
)
