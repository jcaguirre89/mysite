# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 15:44:31 2017

@author: crist
"""

from hindsight1.models import Sp100
from django.core.management.base import BaseCommand
import os

directory = 'C:\\Users\\crist\\mysite\\hindsight1\\static\\hindsight1'
filename = 'sp100_info.csv'
fileDir=os.path.join(directory,filename)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path
        Sp100.objects.from_csv(fileDir)