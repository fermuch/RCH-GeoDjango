# -*- coding: utf-8 -*-
# Import django modules
from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('mapas.views',
    url(r'^$', 'index', name='mapas-index'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^media/(?P<path>.*)$',
        'serve', {
        'document_root': 'media/',
        'show_indexes': True }))