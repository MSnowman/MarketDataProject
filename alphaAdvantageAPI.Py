#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 20:30:11 2018

@author: Snowman

Requires you to go to https://www.alphavantage.co and get an API Key

"""

import json
import requests


apiKey = "&apikey=" + 'Enter Your Key Here'
intervalTypes = ['1min','5min','15min','30min','60min']
sizes = ['full', 'compact']


def intervalTypeTest(interval):
    try:
        assert interval in intervalTypes
    except AssertionError:
        return print("Internval entered is not a valid internval.  Choose '1min','5min','15min','30min','60min'")
    
def sizeTest(size):
    try:
        assert size in sizes
    except AssertionError:
        return print("Defaulted to 'compact' size because sized entered is not a valid size.  Choose 'full' or 'compact' ")
    

def timeSeriesIntraday(symbol, interval, size='compact'):
    """
    Get the intraday value of a stock or ETF.
    
    symbol as tring
    interval: 1min, 5min, 15min, 30min, 60min
    size:
        compact = latest 100 calls
        full = all for the day
    
    """
    
    apiFunction = 'TIME_SERIES_INTRADAY'
    
    intervalTypeTest(interval)
    sizeTest(size)

    urlCreate ="https://www.alphavantage.co/query?function=" + apiFunction + "&symbol="  + symbol + "&interval=" + interval + "&outputsize=" + size + apiKey


    page = requests.get(urlCreate)
    json_data = json.loads(page.text)


    print(json_data)
    
    
def timeSeriesDaily(symbol, size='compact'):
    """
    Get the value of a stock or ETF or past 100 days or max 20 years.
    Returns Open, High, Low, Close, Volume
    
    symbol as tring
    size: 
        compact = last 100 days
        full = all up to 20 years
    
    """
    
    apiFunction = 'TIME_SERIES_DAILY'
    sizeTest(size)


    urlCreate ="https://www.alphavantage.co/query?function=" + apiFunction + "&symbol="  + symbol + "&outputsize=" + size + apiKey


    page = requests.get(urlCreate)
    json_data = json.loads(page.text)


    print(json_data)

def timeSeriesDailyAdj(symbol, size='compact'):
    """
    Get the adjusted value of a stock or ETF or past 100 days or max 20 years.
    Returns Open, High, Low, Close, Volume, Daily Adj Close, Split/Dividend Events
    
    symbol as tring
    size: 
        compact = last 100 days
        full = all up to 20 years
    
    """
    
    apiFunction = 'TIME_SERIES_DAILY_ADJUSTED'
    sizeTest(size)


    urlCreate ="https://www.alphavantage.co/query?function=" + apiFunction + "&symbol="  + symbol + "&outputsize=" + size + apiKey


    page = requests.get(urlCreate)
    json_data = json.loads(page.text)


    print(json_data)

def batchStockQuotes(symbols):
    """
    Receive multiple stock quotes for different Symbols
    
    """
    
    apiFunction = 'BATCH_STOCK_QUOTES'

    urlCreate ="https://www.alphavantage.co/query?function=" + apiFunction + "&symbol="  + symbols + apiKey


    page = requests.get(urlCreate)
    json_data = json.loads(page.text)


    print(json_data)




