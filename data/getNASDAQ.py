import urllib.request, urllib.error, urllib.parse,csv,http.cookiejar

#site = "http://xueqiu.com/S/AAPL/historical.csv"
#site= "http://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol=JPASSOCIAT&fromDate=1-JAN-2012&toDate=1-AUG-2012&datePeriod=unselected&hiddDwnld=true"

#http://xueqiu.com/S/SH000001/historical.csv
#https://xueqiu.com/v4/stock/quote.json?code=SZ399001&_=1460380110118
'''
{"SZ399001":{"symbol":"SZ399001","exchange":"SZ","code":"399001","name":"深证成指","current":"10351.87","percentage":"-0.61","change":"-63.93","open":"10510.43","high":"10541.18","low":"10226.25","close":"10351.87","last_close":"10415.8","high52week":"10856.44","low52week":"7011.33","volume":"5.4494209904E10","lot_volume":"5.4494209904E8","volumeAverage":"34766300981","marketCapital":"1.4969816532086E13","eps":"0.0","pe_ttm":"","pe_lyr":"","beta":"0.0","totalShares":"1229521083","time":"Mon Apr 08 15:15:03 +0800 2019","afterHours":"0.0","afterHoursPct":"0.0","afterHoursChg":"0.0","afterHoursTime":"Wed Oct 19 21:59:01 -0400 2011","updateAt":"1548345625731","dividend":"0.0","yield":"0.0","turnover_rate":"","instOwn":"0.0","rise_stop":"999999.99","fall_stop":"0.01","currency_unit":"CNY","amount":"5.60604756906E11","net_assets":"0.0","hasexist":"","has_warrant":"0","type":"12","flag":"1","rest_day":"","amplitude":"3.02%","market_status":"已收盘","lot_size":"100","min_order_quantity":"0","max_order_quantity":"0","tick_size":"0.01","variable_tick_size":"","kzz_stock_symbol":"","kzz_stock_name":"","kzz_stock_current":"0.0","kzz_convert_price":"0.0","kzz_covert_value":"0.0","kzz_cpr":"0.0","kzz_putback_price":"0.0","kzz_convert_time":"","kzz_redempt_price":"0.0","kzz_straight_price":"0.0","kzz_stock_percent":"","pb":"0.0","benefit_before_tax":"0.0","benefit_after_tax":"0.0","convert_bond_ratio":"","totalissuescale":"","outstandingamt":"","maturitydate":"","remain_year":"","convertrate":"0.0","interestrtmemo":"","release_date":"","circulation":"0.0","par_value":"0.0","due_time":"0.0","value_date":"","due_date":"","publisher":"","redeem_type":"","issue_type":"","bond_type":"","warrant":"","sale_rrg":"","rate":"","after_hour_vol":"0","float_shares":"0","float_market_capital":"1.151924549646E13","disnext_pay_date":"","convert_rate":"0.0","volume_ratio":"1.07","percent5m":"0.0","pankou_ratio":"0.0%","psr":"","rise_count":"731","flat_count":"44","fall_count":"1420"}}
'''
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


#req = urllib2.Request(site, headers=hdr)
symbolTest = 'APPL'
Exchange = 'NASDAQ'


try:
    with open(Exchange +'.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print((row['Symbol'], row['Name']))
            symbol = row['Symbol'].strip()


            if '^' not in symbol:
                site = "http://xueqiu.com/S/" + symbol + "/historical.csv"
                req = urllib.request.Request(site, headers=hdr)
                page = urllib.request.urlopen(req)
                #content = page.read()
                with open(Exchange + '/'+symbol+'.csv','w') as symbolCSV:
                    symbolCSV.write(page.read())
            else:
                print('symbol contains ^, not valid, passed...')


except urllib.error.HTTPError as e:
    print(e.fp.read())
