import os.path
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from numpy.polynomial.polynomial import polyfit
import seaborn as sns
import csv
import datetime as dt
import glob
#Distribute $1,000,000 across 20 stocks to minimize risk and maximize portfolio growth over 5 years
import pandas_datareader as web
import datetime


dataset = pd.read_csv(os.path.expanduser("~/Desktop/constituents_csv.csv"))
dataset = dataset[dataset['Sector'] == 'Information Technology']
print(dataset)
tickers = list(dataset['Symbol'].values)
tickers = tickers



def strictly_increasing(input):
    return all(a < b for a, b in zip(input, input[1:]))


def increasing(ticker):
    years = list(range(2012, 2017))
    yearly_highs = []
    formatted = []
    for year in years:
        try:
            if ticker != 'CSRA':
                date = datetime.datetime(year, 1, 5)
                df = web.DataReader(ticker, 'yahoo', date, date)
                price = df['High'].values   #adding .values   will return true numers
                yearly_highs.append(price)

        except KeyError:
            pass
    for item in yearly_highs:
        y = item[0]
        formatted.append(y)
    #if formatted is monotonically increasing: Return True
    x = strictly_increasing(formatted)
    return x

filtered_tickers = []
xxx = ['mu']

def price_parser(stocks):
    try:
        for tick in stocks:
            if increasing(tick) == True:
                filtered_tickers.append(tick)
                print('appended')
        return filtered_tickers
    except KeyError:
        pass
    return filtered_tickers


x = price_parser(tickers)
print(x)
df = pd.DataFrame({'Symbol': x})
export_csv = df.to_csv(os.path.expanduser("~/Desktop/Worthy_Stocks.csv"), index=None, header=True)
print('xd')


