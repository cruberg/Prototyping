import pandas as pd
import numpy as np
from Alpaca import Data
from Fundamentals import Fundamentals
from Universe import Universe

data = Data()

prices = data.get_universe_prices(755)



