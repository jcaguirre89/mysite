# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 15:44:31 2017

@author: crist
"""

from hindsight1.models import Prices
from django.core.management.base import BaseCommand
import os

#flip directory in production
directory = 'C:\\Users\\crist\\mysite\\hindsight1\\static\\hindsight1'
#directory = 'home/cristobal/mysite/hindsight1/static/hindsight1'

filename = 'sp100_prices.csv'
fileDir=os.path.join(directory,filename)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path
        Prices.objects.from_csv(fileDir)