
# coding: utf-8

# In[3]:

import datetime
from pandas.io import data as web
start = datetime.datetime(2015,11,1)
end = datetime.datetime(2015, 11, 10)
soil = web.DataReader("010950.KS", "yahoo", start, end)


# In[5]:

print soil


# In[6]:

ncsoft = web.DataReader('KRX:036570', data_source='google', start='01/01/2015', end='09/02/2015')
sds = web.DataReader('KRX:018260', data_source='google', start='11/01/2015', end='11/10/2015')

print sds

