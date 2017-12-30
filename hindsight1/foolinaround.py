# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 18:18:21 2017

@author: crist
"""
#%%

import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
import os
import numpy as np
from pandas.tseries.offsets import BDay


import quandl
quandl.ApiConfig.api_key = "6FKyrP9sYvvnkLne3sBx"


#base 100 cumulate returns
def calc_cum_ror(df, cols):   
    df_cum=pd.DataFrame(columns=cols)
    for ror in df_cum.columns:   
        df_cum_aux= pd.DataFrame((1 + df[ror]).cumprod()*100)
        df_cum[ror]=df_cum_aux[ror]
    return df_cum

directory='C:\\Users\\crist\\OneDrive\\Documents'
filename='sp100.xlsx'
fileDir=os.path.join(directory,filename)

#read sp100 companies
df_sp=pd.read_excel(fileDir, sheetname='sp100')

df_sp.set_index('Ticker', inplace=True)
#%%
#Download prices from Quandl
tickers=list(df_sp.index)

start = datetime.datetime(2010, 1, 1)

end = datetime.datetime(2017, 10, 31)

#Get prices from google finance
prices=pd.DataFrame()
for ticker in tickers:
    #f = web.DataReader(ticker, 'yahoo', start, end)['Close']
    f = quandl.get('WIKI/'+ticker, start_date=start, end_date=end)['Close']
    f.rename(ticker, inplace=True)
    prices=pd.concat([prices,f], axis=1)



#%%

#Read downloaded prices from excel
file='sp100_prices.xlsx'
fileDir=os.path.join(directory,file)
prices=pd.read_excel(fileDir)

prices.set_index('Date', inplace=True)

#%%
#1 pick a random date
rand_date_loc=np.random.randint(prices.shape[0])
rand_date=prices.index[rand_date_loc].to_pydatetime()

#2 pick 10 random companies
#10 item array of random numbers 0 through 40
rand_companies=np.floor(np.random.rand(10)*41)

#3 draw the random tickers and information
rand_companies_info=df_sp.iloc[rand_companies]

#4 get price time series for the 10 companies
tickers=list(rand_companies_info.index)

#start date for 6 month trailing
ret_start=rand_date-BDay(130)

#end date for 6 month forward
ret_end=rand_date+BDay(130)

#6 months trailing prices
rand_prices_t=prices.loc[ret_start:rand_date,tickers]

#6 months forward prices
rand_prices_f=prices.loc[rand_date:ret_end,tickers]


#%%

#6 months trailing and forward returns
ror_t=rand_prices_t.pct_change(periods=1)
ror_t.fillna(value=0, inplace=True)

#6 month forward
ror_f=rand_prices_f.pct_change(periods=1)
ror_f.fillna(value=0, inplace=True)



df_cum=calc_cum_ror(returns, returns.columns)






#%%

prices_stacked=prices.stack(level=-1)
prices_stacked=prices_stacked.reset_index()
prices_stacked.columns=['date', 'ticker', 'price']
prices_stacked.to_csv(os.path.join(directory,'sp100_prices.csv'), index=False)

#%%

sp_export=df_sp.drop(['HQ', 'Weight', 'Exchange', 'SEDOL'], axis=1)
sp_export.reset_index(inplace=True)
sp_export.columns=['ticker', 'security', 'sector', 'industry', 'isin']

sp_export.to_csv(os.path.join(directory,'sp100_info.csv'), index=False)


#%%

df1=pd.read_csv(os.path.join(directory,'sp100_info.csv'), encoding='latin1')
