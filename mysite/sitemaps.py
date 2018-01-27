# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:31:58 2018

@author: crist
"""

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class MainSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about']

    def location(self, item):
        return reverse(item)
