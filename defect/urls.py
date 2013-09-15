from django.conf.urls import patterns, include, url

from .api import router

urlpatterns = patterns('',
    url(r'', include(router.urls)),
)
