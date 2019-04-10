# -*- coding: utf-8 -*-
"""
创建于 Thu Mar 14 16:13:03 2019

@author: dmitrievsky
"""
from MetaTrader5 import *
from datetime import datetime
import pandas as pd
# 初始化 MT5 连接
MT5Initialize()
MT5WaitForTerminal()

print(MT5TerminalInfo())
print(MT5Version())

# 将数据复制到 pandas 数据帧
stockdata = pd.DataFrame()
rates = MT5CopyRatesFromPos("EURUSD", MT5_TIMEFRAME_M1, 0, 5000)
# 逆初始化 MT5 连接
MT5Shutdown()

stockdata['Open'] = [y.open for y in rates]
stockdata['Close'] = [y.close for y in rates]
stockdata['High'] = [y.high for y in rates]
stockdata['Low'] = [y.low for y in rates]
stockdata['Date'] = [y.time for y in rates]

import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

trace = go.Ohlc(x=stockdata['Date'],
                open=stockdata['Open'],
                high=stockdata['High'],
                low=stockdata['Low'],
                close=stockdata['Close'])

data = [trace]
plot(data)