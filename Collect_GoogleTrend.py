import pandas as pd
from pytrends.request import TrendReq
import numpy as np
import time

class Collect_GoogleTrend():
    def __init__(self):
        self.pytrend = TrendReq()
        
    def Collect(self, keywords, startdate, enddate):
        total_df = pd.DataFrame()
        
        for keyword in keywords:
            
            if keyword in total_df.columns:
                continue
            else:
                dt = self.interest_processing(keyword, startdate, enddate)
                period = dt.index.values
                vals = dt[keyword].values
                total_df['period'] = period
                total_df[keyword] = vals
                total_df[keyword+'_change'] = np.zeros(len(dt))
                total_df.loc[1:, keyword+'_change'] = (total_df[keyword][1:].values - total_df[keyword][:-1].values) / total_df[keyword][1:].values
            time.sleep(1)
        total_df.to_csv('data/trend_csvs/'+startdate+'_'+enddate+'.csv', index=False)
        
        print('CSV SAVED')
        return total_df
        
    def interest_processing(self, keyword, startdate, enddate):
        keyword= [keyword]
        timerange = startdate +' '+ enddate
        self.pytrend.build_payload(kw_list= keyword, timeframe = timerange)
        dt = self.pytrend.interest_over_time()
        try:
            del dt['isPartial']
            return dt
        except:
            pass
        
        