import os.path
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import seaborn as sns
import csv
import datetime as dt
import pandas_datareader as web
import datetime
import pandas_datareader as web
import quandl
import requests
from pprint import pprint as pp



stocks = pd.read_csv(os.path.expanduser("~/Desktop/Worthy_Stocks.csv"))
list_symbols = list(stocks['Symbol'].values)
stocks.set_index('Symbol', inplace=True)

def scraper(stocks):

    stock_columns = ['Symbol', 'Price', 'Current Ratio', 'ROE',
               'Revenue Growth', 'Earnings Growth']

    df = pd.DataFrame(columns = stock_columns)

    i = 0
    for stock in stocks:
        try:
            params = {"formatted": "true",
                "crumb": "AKV/cl0TOgz", # works without so not sure of significance
                "lang": "en-US",
                "region": "US",
                "modules": "defaultKeyStatistics,financialData,calendarEvents",
                "corsDomain": "finance.yahoo.com"}


            link = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/" + str(stock)
            link_2 = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/" + str(stock)
            r = requests.get(link, params=params)
            data = r.json()[u'quoteSummary']["result"][0][u'financialData']



            currentPrice = data[u'currentPrice']['fmt']
            currentRatio = data[u'currentRatio']['fmt']
            returnOnEquity = data[u'returnOnEquity']['fmt']
            revenueGrowth = data[u'revenueGrowth']['fmt']
            earningsGrowth = data[u'earningsGrowth']['fmt']
            profitMargin = data[u'profitMargins']['fmt']

            metric_dict = {'Symbol': stock,
                           'Price': currentPrice,
                           'Current Ratio': currentRatio,
                           'ROE': returnOnEquity,
                           'Revenue Growth': revenueGrowth,
                           'Earnings Growth': earningsGrowth,
                           'Profit Margin': profitMargin
                            }

            stock_df = pd.DataFrame([metric_dict], columns=metric_dict.keys())
            df = pd.concat([df, stock_df], axis=0)

        except (KeyError, TypeError):
            pass

    return df

data_set = scraper(list_symbols)
symbol = data_set['Symbol']
data_set.drop(labels=['Symbol'], axis=1, inplace=True)
data_set.insert(0, 'Symbol', symbol)
print(data_set)
export_csv = data_set.to_csv(os.path.expanduser("~/Desktop/Tech_Stocks.csv"), index=None, header=True)


