import os.path
import os
import pandas as pd
import numpy as np
from tabulate import tabulate
from market_cap_data import run
from filter_stocks import pretty_table

x = pd.read_csv(os.path.expanduser("~/Desktop/TopTechStocks.csv"))
pretty_table(x)


