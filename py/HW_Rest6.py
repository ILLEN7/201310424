
# coding: utf-8

# In[2]:

import os
keyPath=os.path.join('C:/Users/ILLEN/Documents', 'src','key.properties')

f=open(keyPath, 'r')
lines=f.readlines()

key=dict()
for line in lines:
    row=line.split('=')
    row0=row[0]
    key[row0]=row[1].strip()


# In[4]:

print key['dataseoul']


# In[5]:

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='CardSubwayStatisticsService'
START_INDEX='1'
END_INDEX='5'
USE_MON='201306'


# In[13]:

url='http://openAPI.seoul.go.kr:8088'
url+='/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
url+='/'
url+=USE_MON
print url


# In[20]:

import requests

_maxIter=2
_iter=0
while _iter<_maxIter:
    myurl='http://openAPI.seoul.go.kr:8088/77657243667369643133357a756f5350/xml/CardSubwayStatisticsService/1/5/201306'
    response = requests.get(myurl).text
    print response
    START_INDEX+='5'
    END_INDEX+='5'
    _iter+=1


# In[23]:

KEY=str(key['dataseoul'])
TYPE='json'
SERVICE='CardSubwayStatisticsService'
START_INDEX='1'
END_INDEX='5'
USE_MON='201306'


url='http://openAPI.seoul.go.kr:8088'
url+='/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
url+='/'
url+=USE_MON
print url


# In[27]:

myurl2='http://openAPI.seoul.go.kr:8088/77657243667369643133357a756f5350/json/CardSubwayStatisticsService/1/5/201306'


# In[31]:

import requests
response=requests.get(myurl2).text
print response


# In[32]:

type(response)


# In[37]:

import json
jd=json.loads(response)
print jd['CardSubwayStatisticsService']['row'][0]


# In[38]:

for item in jd['CardSubwayStatisticsService']['row']:
    print item.keys()
    for i in item.keys():
        if i=='STATION_NM':
            print ''.join(item.values())
            print item.values()[1]

