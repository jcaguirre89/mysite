# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:12:18 2017

@author: crist
"""

from django.conf.urls import url


from . import views

app_name = 'blog'

urlpatterns = [
        url(r'^index/$', views.index, name='index'),
        url(r'^search/$', views.search, name='search'),
        url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),    
        url(r'^topic/(?P<topic>[\w\-]+)/$', views.topic, name='topic'),
        url(r'^tag/(?P<tag>[\w\-]+)/$', views.tags, name='tags'),
        ]