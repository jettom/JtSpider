from MetaTrader5 import *
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

# 初始化 MT5 连接
MT5Initialize()
MT5WaitForTerminal()

print(MT5TerminalInfo())
print(MT5Version())

# 为需要绘制相关矩阵的货币创建清单
sym = ['EURUSD','GBPUSD','USDJPY','USDCHF','AUDUSD','GBPJPY']

# 将数据复制到数据帧
d = pd.DataFrame()
for i in sym:
     rates = MT5CopyRatesFromPos(i, MT5_TIMEFRAME_M1, 0, 1000)
     d[i] = [y.close for y in rates]

# 逆初始化 MT5 连接
MT5Shutdown()

# 比较百分比变化
rets = d.pct_change()

# 计算相关性
corr = rets.corr()

# 绘制相关性矩阵
plt.figure(figsize=(10, 10))
plt.imshow(corr, cmap='RdYlGn', interpolation='none', aspect='auto')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns, rotation='vertical')
plt.yticks(range(len(corr)), corr.columns);
plt.suptitle('FOREX Correlations Heat Map', fontsize=15, fontweight='bold')
plt.show()


# 导入 statsmodels 进行协整检验
import statsmodels
from statsmodels.tsa.stattools import coint

x = d['GBPUSD']
y = d['GBPJPY']
x = (x-min(x))/(max(x)-min(x))
y = (y-min(y))/(max(y)-min(y))

score = coint(x, y)
print('t-statistic: ', score[0], ' p-value: ', score[1])

# 绘制 z-分值变换
diff_series = (x - y)
zscore = (diff_series - diff_series.mean()) / diff_series.std()

plt.plot(zscore)
plt.axhline(2.0, color='red', linestyle='--')
plt.axhline(-2.0, color='green', linestyle='--')

plt.show()

