import os.path
import os
import pandas as pd
import numpy as np
from tabulate import tabulate
from market_cap_data import run


data_set = pd.read_csv(os.path.expanduser("~/Desktop/Tech_Stocks.csv"))
data_set['ROE'] = data_set['ROE'].str[:-1].astype(np.float)
data_set['Profit Margin'] = data_set['Profit Margin'].str[:-1].astype(np.float)




def pretty_table(df):
    #make ROE values have percents again
    print(tabulate(df, headers='keys', tablefmt='psql'))


def filter(df):
    df = df[df['Current Ratio'] >= 1.5]
    filtered_data = df[df['ROE'] >= 3]
    pm = filtered_data[filtered_data['Profit Margin']>=10]
    pm = pm.drop(labels=['ROE', 'Current Ratio', 'Earnings Growth', 'Profit Margin'], axis=1)
    return pm

data_frame = run(filter(data_set))
data_frame['Market Cap'] = data_frame['Market Cap'].str[:-1].astype(np.float)
data_frame['Revenue Growth'] = data_frame['Revenue Growth'].str[:-1].astype(np.float)
pm = data_frame[data_frame['Revenue Growth'] >= 15]
pm = pm.drop(labels=['Revenue Growth'], axis=1)


export_csv = pm.to_csv(os.path.expanduser("~/Desktop/TopTechStocks.csv"), index=None, header=True)



#A good current ratio is > 1.5
#currently 14, want to pick top 5 winners
