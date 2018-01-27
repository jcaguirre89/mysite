# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 08:35:06 2018

@author: crist
"""
#%%

import os
import pandas as pd

#flip directory in production
directory = 'C:\\Users\\crist\\mysite\\hindsight1\\static\\hindsight1'
#directory = '/home/cristobal/mysite/hindsight1/static/hindsight1'

filename = 'sp100_info.csv'
fileDir=os.path.join(directory,filename)

df = pd.read_csv(fileDir, encoding='latin-1')

#df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1, inplace=True)


#out as utf8
#df.to_csv(fileDir, encoding='utf-8')