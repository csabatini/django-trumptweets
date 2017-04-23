from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       url(r'^$', 'trumptweets.views.index', name='home'),
                       url(r'^tag/(?P<tag_id>[0-9]+)/$', 'trumptweets.views.tag', name='tag')
                       )
