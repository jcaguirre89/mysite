# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:39:05 2017

@author: crist
"""


import numpy as np
import pandas as pd
import datetime
import os
#from .new_play import NewPlay

"""
#Read downloaded prices from csv
directory = 'C:\\Users\\crist\\mysite\\hindsight1\\static\\hindsight1'
file='sp100_prices.csv'
fileDir=os.path.join(directory,file)
prices=pd.read_csv(fileDir)
"""

def compute_ror(weights, df_ror):
    """
    Calculates strategy return)
    """
    port_ror_aux = weights * df_ror
    port_ror_ts = port_ror_aux.sum(axis=1)
    port_ror_cum = pd.DataFrame((1 + port_ror_ts).cumprod()*100)
    port_ror_cum.columns=['strategy']
    strategy_ror=port_ror_cum.iat[port_ror_cum.shape[0]-1,0]/100-1
    return strategy_ror


if __name__ == '__main__':
    print('running as main')
    