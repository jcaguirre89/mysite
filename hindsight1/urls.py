# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:12:18 2017

@author: crist
"""

from django.conf.urls import url

from . import views

#this tells django these urls belong to the 'hindsight1' app, when referencing
#from a template with the {%url%} tag. 
app_name = 'hindsight1'

urlpatterns = [url(r'^game/$', views.ranking, name='ranking'),
              url(r'^result/$', views.result, name='result'),
              url(r'^earnings/$', views.earnings, name='earnings'),
              url(r'^performance/$', views.performance, name='performance'),
              url(r'^play/$', views.play, name='play'),
              url(r'^ranking/$', views.ranking, name='ranking'),
              url(r'^dashboard/$', views.perf_dashboard, name='dashboard'),
              
              
              
              ]