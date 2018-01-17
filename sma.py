#import ta-lib - technical analysis library.
#https://github.com/mrjbq7/ta-lib/blob/master/README.md


import talib as ta
import numpy as np

#import [binance data] into pd.Dataframe

#output = talib.SMA(close)

# list of functions
print talib.get_functions()

# dict of functions by group
print talib.get_function_groups()

# generate random price numbers
close = numpy.random.random(100)

# calculate simple moving average of close
output = talib.SMA(close)
