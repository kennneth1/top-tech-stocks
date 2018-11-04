import requests
import pandas as pd

stocks = ['ADBE','AVGO','EA','FB','MA', 'MSFT','NVDA','SWKS','TXN','TSS','V']
market_caps = []


def get_market(stocks):
    for stock in stocks:
        try:
            params = {"formatted": "true",
            "crumb": "AKV/cl0TOgz",
            "lang": "en-US",
            "region": "US",
            "modules": "summaryDetail",
            "corsDomain": "finance.yahoo.com"}

            link = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/" + str(stock)
            r = requests.get(link, params=params)
            data = r.json()[u'quoteSummary']["result"][0]
            marketCap = data["summaryDetail"]["marketCap"]['fmt']
            market_caps.append((marketCap))
        except TypeError:
            print("error")
    return market_caps

def run(df):
    x = get_market(stocks)
    df['Market Cap'] = x
    return df




#marketcap is in billions
