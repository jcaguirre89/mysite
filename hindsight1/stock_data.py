# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:00:39 2017

@author: crist
"""
import urllib.request
import json
from pandas_datareader import data
import datetime
import pandas as pd
import numpy as np
import os

def get_data(ticker):
    fin_data_url = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{0}?formatted=true&lang=en-US&region=US&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CcalendarEvents&corsDomain=finance.yahoo.com".format(ticker)
    with urllib.request.urlopen(fin_data_url) as url:
        data = json.loads(url.read().decode())
    
    main_data = data['quoteSummary']['result'][0]['financialData']
    
    try:
        debt_to_equity = main_data['debtToEquity']['raw']
    except:
        debt_to_equity='N/A'
    try:
        earnings_growth = main_data['earningsGrowth']['raw']
    except:
        earnings_growth='N/A'
    try:
        profit_margin = main_data['profitMargins']['raw']
    except:
        profit_margin='N/A'
    try:
        roe = main_data['returnOnEquity']['raw']
    except:
        roe='N/A'
    try:
        rev_growth =  main_data['revenueGrowth']['raw']
    except:
        rev_growth='N/A'
    try:
       eps_t = data['quoteSummary']['result'][0]['defaultKeyStatistics']['trailingEps']['raw']
    except:
        eps_t='N/A'
    try:
        price_book = data['quoteSummary']['result'][0]['defaultKeyStatistics']['priceToBook']['raw']
    except:
        price_book='N/A'        
        
    ret_dict = {
            'debt_to_equity': debt_to_equity,
            'earnings_growth': earnings_growth,
            'profit_margin': profit_margin,
            'roe': roe,
            'rev_growth': rev_growth,
            'eps_t': eps_t,
            'price_book': price_book,
            }
    return ret_dict

def get_price(ticker, start, end):
    prices = data.DataReader(ticker, 'google', start, end)
    #prices.name = 'price'
    prices['ticker']=ticker
    return prices

def price_db(tickers, start, end):
    prices = pd.DataFrame()
    for ticker in tickers:
        price = get_price(ticker, start, end)
        prices = pd.concat([prices, price], axis=0)
    return prices


#read csv with list of tickers
filename = 'sp100_info.csv'
directory = 'C:\\Users\\crist\\mysite\\hindsight1\\static\\hindsight1'
stocks = pd.read_csv(os.path.join(directory,filename), encoding='latin1')


start = datetime.date(2000,1,1)
end = datetime.datetime.today().date()

tickers = list(stocks['ticker'])
#prices = price_db(tickers, start, end)


if __name__ == '__main__':
    ticker = 'aapl'
    start = datetime.date(2000,1,1)
    end = datetime.datetime.today().date()
    prices = get_price(ticker, start, end)
    print(prices.head())
    
    tickers = ['aapl', 'googl', 'ge']
    prices = price_db(tickers, start, end)
    print(prices.head())

