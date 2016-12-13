
# coding: utf-8

# In[1]:

import os
keyPath=os.path.join('C:/Users/ILLEN/Documents', 'src','key.properties')

f=open(keyPath, 'r')
lines=f.readlines()

key=dict()
for line in lines:
    row=line.split('=')
    row0=row[0]
    key[row0]=row[1].strip()


# In[2]:

import requests
import urlparse

KEY=str(key['dataseoul'])
TYPE='json'
SERVICE='RealtimeWeatherStation'
START_INDEX=str(1)
END_INDEX=str(5)
STN_NM=u'중구'


# In[5]:

url="http://openapi.seoul.go.kr:8088/"
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=str(START_INDEX)
url+='/'
url+=str(END_INDEX)
url+='/'
url+=STN_NM

print url


# In[7]:

myurl='http://openapi.seoul.go.kr:8088/77657243667369643133357a756f5350/json/RealtimeWeatherStation/1/5/중구'


# In[10]:

data=requests.get(url).text
print data

