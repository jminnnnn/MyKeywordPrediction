from Collect_GoogleTrend import *
import yfinance as yf
import datetime

def build_gtrend_dataset():
    CGT = Collect_GoogleTrend()
    
    market_related_keys = ['debt','stocks','color','restaurant','portfolio','inflation','housing','dow jones','revenue','economics']
    print(len(market_related_keys))
    
    gtrend_dataset = CGT.Collect(market_related_keys, '2012-01-01', '2022-07-31')

    return gtrend_dataset

def get_snp500_price():
    snp500=yf.download('^GSPC', start='2012-01-01', end='2022-07-31')
    snp500['Date'] = snp500.index.values
    # print(snp500)
    return snp500

def detach_avg_price_from_data(dataset):
    years, months = [], []
    
    
    for i in range(2012, 2023):
        years.append(i)
    for i in range(1,12):
        months.append(i)
    
    
    for d in dataset['Date']:
        d = str(d).split(' ')[0]
        _d=datetime.datetime.strptime(d, '%Y-%m-%d')
        
    
        
        if _d.year == 2012:
            if _d.month ==1:
                
                
    
# build_gtrend_dataset()
snp500 = get_snp500_price()
detach_avg_price_from_data(snp500)