import pandas as pd
import numpy as np
from Fundamentals import Fundamentals
from Universe import Universe
from CharlieCode import Data

data = Data()
prices = data.get_universe_prices(Universe,100)

last_price = prices[prices.index[-1]:].T
last_price.columns = ['LastClose']
last_price.reset_index(inplace=True)
last_price.columns = ['Symbol','LastClose']
last_price

# Read in Fundamentals and compare

Fundamentals



