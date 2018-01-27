# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:56:17 2018

@author: crist
"""

from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.utils import timezone


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
       return Post.objects.filter(pub_date__lte=timezone.now())
 
    def lastmod(self, item): 
       return item.last_update