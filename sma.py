# Moving Averages Code

# Load the necessary packages and modules
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import [binance exchange data]
import pandas as pd

# Simple Moving Average 
def SMA(data, ndays): 
 SMA = pd.Series(pd.rolling_mean(data['Close'], ndays), name = 'SMA') 
 data = data.join(SMA) 
 return data

# Retrieve the binance data:

# Compute the 50-day SMA for NIFTY
n = 50
SMA_ETHEUR = SMA(data,n)
SMA_ETHEUR = SMA_ETH.dropna()
SMA = SMA_ETHEU['SMA']

# Plotting the Price Series chart and Moving Averages below
plt.figure(figsize=(9,5))
plt.plot(data['Close'],lw=1, label='NSE Prices')
plt.plot(SMA,'g',lw=1, label='50-day SMA (green)')
plt.legend(loc=2,prop={'size':11})
plt.grid(True)
plt.setp(plt.gca().get_xticklabels(), rotation=30)
