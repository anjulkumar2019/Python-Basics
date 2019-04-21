#  Date time 
"""
Pandas combine datetime and dateutil to provide Timestamp object with efficient storage and vectorized interface
of numpy.datetime64. Pandas can create a DatetimeIndex that can be used to index data in a series or DataFrame
"""
import pandas as pd
date=pd.to_datetime('20th April, 2019')
print(date)

"""
output
2019-04-20 00:00:00
"""
date.strftime('%A')
#output : 'Saturday'

index=pd.to_datetime(['2016-04-20','2017-04-20','2018-04-20','2019-04-20'])
data=pd.DataFrame([10,11,12,13], index=index)
data
"""
Output
             0
2016-04-20  10
2017-04-20  11
2018-04-20  12
2019-04-20  13

"""
data['2016']
"""
            0
2016-04-20  10
"""
index-index[0]
"""
Output
Out[11]: TimedeltaIndex(['0 days', '365 days', '730 days', '1095 days'], dtype='timedelta64[ns]', freq=None)
"""

pd.date_range('2019-04-10','2019-04-20')
"""
DatetimeIndex(['2019-04-10', '2019-04-11', '2019-04-12', '2019-04-13',
               '2019-04-14', '2019-04-15', '2019-04-16', '2019-04-17',
               '2019-04-18', '2019-04-19', '2019-04-20'],
              dtype='datetime64[ns]', freq='D')
"""


pd.date_range('2019-04-01','2019-04-20',freq='W')
"""
Out[19]: DatetimeIndex(['2019-04-07', '2019-04-14'], dtype='datetime64[ns]', freq='W-SUN')
"""
