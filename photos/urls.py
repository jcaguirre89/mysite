# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 18:47:00 2017

@author: crist
"""

from django.conf.urls import url

from . import views

#this tells django these urls belong to the 'photos' app, when referencing
#from a template with the {%url%} tag. 
app_name = 'photos'

"""
This version works with specific views functions, while the new one uses the
generic view clases. 

urlpatterns = [
    #ex: /photos/
    url(r'^$', views.index, name='index'),
    #ex: /photos/5/
    url(r'^(?P<question_id>[0-9]+)/$',views.detail, name='detail'),
    #ex: /photos/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='results'),
    #ex: /photos/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote, name='vote'),
]

"""


urlpatterns = [
    #ex: /photos/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #ex: /photos/5/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
    #ex: /photos/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(), name='results'),
    #ex: /photos/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote, name='vote'),
]