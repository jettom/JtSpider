def get_all_today_cap_from_163():
    """
    从网易财经，获取每支股票当日的流通市值和总市值，与新浪财经获取的数据进行合并

    :return: df['SYMBOL', 'MCAP', 'TCAP']
    """
    def deal_content(count):
        """
        从网易财经获取数据，并进行处理，形成dict

        :param count:股票数量
        :return:
        """
        # 网易财经的“神奇网址”，
        # 对应的浏览器用网是:http://quotes.money.163.com/old/#query=EQA&DataType=HS_RANK&sort=PERCENT&order=desc&count=24&page=0
        url = r'http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2' \
              r'Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQA&fields=NO%2CSYMBOL%2CNAME%2CPRICE%2CPE' \
              r'RCENT%2CUPDOWN%2CFIVE_MINUTE%2COPEN%2CYESTCLOSE%2CHIGH%2CLOW%2CVOLUME%2CTURNOVER%2CHS%2CLB%' \
              r'2CWB%2CZF%2CPE%2CMCAP%2CTCAP%2CMFSUM%2CMFRATIO.MFRATIO2%2CMFRATIO.MFRATIO10%2CSNAME%2CCODE%' \
              rf'2CANNOUNMT%2CUVSNEWS&sort=SYMBOL&order=asc&count={count}&type=query'
        ctn = get_content_from_internet(url)  # 原始信息，是bytes类型，需要转换成str
        ctn = ctn.decode('gbk')  # decode，bytes转str；encode，str转bytes类型
        ctn = ctn.strip()  # 去掉文本前后的空格、回车等
		# 将内容是dict的字符串，转换为dict（loads会自动转换为最适合的python数据类型）
        ctn = json.loads(ctn)  # ********形成dict的数据具体内容见本帖后“附2”的说明
        return ctn

    page_count = deal_content(count=2)['total']  # 只取2条记录，获取共有多少支股票
    time.sleep(1)
    content = deal_content(page_count)			# 一次性获取全部股票，4000+支股票日线数据

    k_lines = content['list']
    df = pd.DataFrame(k_lines)
    # ********只取了三列数据,学友可以修改本行代码,选择更多的数据留存
    # --------若要使用更多数据，请修改些处-----，开始处-------------------------------------------
    df = df[['SYMBOL', 'MCAP', 'TCAP']]  # 股票代码、流通市值、总市值
    rename_dict = {'SYMBOL': '股票代码_m', 'MCAP': '流通市值', 'TCAP': '总市值'}
    # --------若要使用更多数据，请修改些处-----，结束处-------------------------------------------
    
    df.rename(columns=rename_dict, inplace=True)

    return df

# 主程序
if __name__ == '__main__':
    if is_today_trading_day() is False:
        print('今天不是交易日，不需要更新股票数据，退出程序')
        exit()

    # 判断当前时间是否超过15点
    if datetime.now().hour < 16:  # 保险起见可以小于16点
        print('今天股票尚未收盘，不更新股票数据，退出程序')
        exit()

    df_sina = get_all_today_stock_data_from_sina_marketcenter()	# 课程代码
    df_sina['股票代码_m'] = df_sina['股票代码'].str[2:]
    df_163 = get_all_today_cap_from_163()
    # 合并表
    df = pd.merge(left=df_sina, right=df_163, on='股票代码_m', how='left', indicator=True, sort=True)
    df.drop(['股票代码_m', '_merge'], axis=1, inplace=True)

    # 对数据进行存储
    for i in df.index:
        t = df.iloc[i:i+1, :]
        stock_code = t.iloc[0]['股票代码']

        # 构建存储文件路径
        path = r'e:\data\stockDB\D_candles\\' + stock_code + '.csv'
        # 文件存在，不是新股
        if os.path.exists(path):
            t.to_csv(path, header=None, index=False, mode='a')
        # 文件不存在，说明是新股
        else:
            # 先将头文件输出
            t.to_csv(path, index=False, mode='a')
        print(stock_code)

'''
{'count': 2,
 'list': [{'CODE': '1000001',
           'FIVE_MINUTE': 0.0028360748723767,
           'HIGH': 18.34,
           'HS': 0.0049360011082477,
           'LB': 0.94584803647406,
           'LOW': 17.7,
           'MCAP': 348527486471.88,
           'MFRATIO': {'MFRATIO10': 116564000000, 'MFRATIO2': 22398000000},
           'MFSUM': 1.33,
           'NAME': '平安银行',
           'NO': 1,
           'OPEN': 17.71,
           'PE': 13.503759398496,
           'PERCENT': 0.018718,
           'PRICE': 17.96,
           'SNAME': '平安银行',
           'SYMBOL': '000001',
           'TCAP': 348530290836.08,
           'TURNOVER': 1727488481.5,
           'UPDOWN': 0.33,
           'VOLUME': 95786863,
           'WB': -0.4374377768793,
           'YESTCLOSE': 17.63,
           'ZF': 0.036301758366421},
          {'CODE': '1000002',
           'FIVE_MINUTE': 0.00035778175313065,
           'HIGH': 28.15,
           'HS': 0.0063518461181229,
           'LB': 0.82576904894833,
           'LOW': 27.81,
           'MCAP': 272569228819.99,
           'MFRATIO': {'MFRATIO10': 241491467190.53,
                       'MFRATIO2': 19862827129.73},
           'MFSUM': 3.58,
           'NAME': '万  科Ａ',
           'NO': 2,
           'OPEN': 28,
           'PE': 7.8296089385475,
           'PERCENT': 0.002862,
           'PRICE': 28.03,
           'SNAME': '万科A',
           'SYMBOL': '000002',
           'TCAP': 325645033594.03,
           'TURNOVER': 1728820912.73,
           'UPDOWN': 0.08,
           'VOLUME': 61766600,
           'WB': -0.26104545492617,
           'YESTCLOSE': 27.95,
           'ZF': 0.01216457960644}],
 'order': 'asc',
 'page': 0,
 'pagecount': 2042,
 'time': '2020-11-03 23:10:46',
 'total': 4083}
 '''

