# -*-coding:UTF-8-*-
import pandas as pd
import csv
#http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=%s1
#~
#http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=%s178
#fourth table [3]

#http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=i
# 再注意一下其他参数：
# a：表示A股，把a替换为h，表示港股；把a替换为xsb，则表示新三板。那么，在网址分页for循环外部再加一个for循环，就可以爬取这三个股市的股票了。

for i in range(1, 179):
    url = 'http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=%s' % (str(i))
    tb = pd.read_html(url)[3]  #
    tb.to_csv(r'1.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
    print('di'+str(i)+'page done')
