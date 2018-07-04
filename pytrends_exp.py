import pandas as pd
import matplotlib as mp
import lxml
import requests

from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["TEPPCO"]
# pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
# pytrends.build_payload(kw_list, timeframe='2013-4-28T0 2013-4-28T4')

 # pytrends.interest_over_time()
results = pytrends.get_historical_interest(kw_list, year_start = 2010, year_end = 2011)
print(results)
