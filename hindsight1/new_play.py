# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:13:07 2017

@author: crist
"""

import datetime
import numpy as np
from pandas.tseries.offsets import BDay
import pandas as pd
import os



#Read downloaded prices from csv
directory = 'C:\\Users\\crist\\mysite\\hindsight1\\static\\hindsight1'
file='sp100_prices.csv'
fileDir=os.path.join(directory,file)
prices=pd.read_csv(fileDir)


file='sp100_info.csv'
fileDir=os.path.join(directory,file)
df_sp=pd.read_csv(fileDir, encoding='latin1')

class NewPlay: 
    
    play_id=0
    date_pool=pd.Series(prices.date.unique())
    companies=pd.Series(df_sp['ticker'].unique())
    max_date=datetime.datetime.strptime(date_pool.iloc[date_pool.size-1], "%Y-%m-%d").date()    
    min_date=datetime.datetime.strptime(date_pool.iloc[0], "%Y-%m-%d").date()
    
    #unstack prices and sort by date
    df_p=prices.pivot(index='date', columns='ticker', values='price')
    df_p.reset_index(inplace=True)
    df_p['pydate']=pd.to_datetime(df_p['date'])
    df_p.drop(['date'], axis=1, inplace=True)
    df_p.set_index('pydate', inplace=True)
    df_p.sort_index(inplace=True, ascending=True)

    #Initialize a new play, increase play count by 1       
    def __init__(self):        
        NewPlay.play_id += 1
    
    #start date of play
    def rand_date(self, date_pool=date_pool, min_date=min_date, max_date=max_date):
        checks=True
        while checks==True:
            rand_date_loc = np.random.randint(date_pool.size)
            rand_date_str=date_pool.iloc[rand_date_loc]
            rand_date=datetime.datetime.strptime(rand_date_str, "%Y-%m-%d").date()
            #Check date has 6M of forward and backwards history
            ret_start=(rand_date-BDay(130)).date()
            ret_end=(rand_date+BDay(130)).date()
            if ret_start>=min_date and ret_end<=max_date:
                checks=False  
        return rand_date
        
    #6 month prior date
    def start_date(self, rand_date):
        ret_start=rand_date-BDay(130)
        return ret_start
        
    #6 month forward date
    def end_date(self, rand_date):
        ret_start=rand_date+BDay(130)
        return ret_start
            
    #pick 10 random companies
    def get_companies(self, companies=companies):
        #5 item array of random numbers 0 through 100
        rand_companies=np.floor(np.random.rand(5)*101)
        #3 draw the random tickers
        tickers=list(companies.iloc[rand_companies])
        return tickers
    
    def trailing_prices(self, tickers, rand_date, df_p=df_p):
        start_date=self.start_date(rand_date)
        rand_prices_t=df_p.loc[start_date:rand_date,tickers]
        return rand_prices_t

    def forward_prices(self, tickers, rand_date, df_p=df_p):
        end_date=self.end_date(rand_date)
        rand_prices_f=df_p.loc[rand_date:end_date,tickers]
        return rand_prices_f
    
    def calc_ror(self, tickers, rand_date, trailing=True):
        if trailing:
            prices=self.trailing_prices(tickers, rand_date)
        else:
            prices=self.forward_prices(tickers, rand_date)
        df_ror=prices.pct_change(periods=1)
        df_ror.fillna(value=0, inplace=True)        
        return df_ror
            
    #calculate cum return (later create return charts here)
    def calc_cum_ror(self, tickers, rand_date, trailing=True):
        if trailing:
            prices=self.trailing_prices(tickers, rand_date)
        else:
            prices=self.forward_prices(tickers, rand_date)
        df_ror=prices.pct_change(periods=1)
        df_ror.fillna(value=0, inplace=True)
        df_cum=pd.DataFrame(columns=prices.columns)
        for col in df_cum.columns:   
            df_cum_aux= pd.DataFrame((1 + df_ror[col]).cumprod()*100)
            df_cum[col]=df_cum_aux[col]
        return df_cum

if __name__=='__main__':
        
    p1=NewPlay()
    date1=p1.rand_date()
    tickers=p1.get_companies()
    print(tickers)
    prices_t=p1.trailing_prices(tickers, date1)
    prices_f=p1.forward_prices(tickers, date1)
    print(date1)
    print(p1.play_id)
    df_cum_t=p1.calc_cum_ror(tickers, date1)
    df_cum_f=p1.calc_cum_ror(tickers, date1,trailing=False)
    df_ror=p1.calc_ror(tickers, date1)         
    



