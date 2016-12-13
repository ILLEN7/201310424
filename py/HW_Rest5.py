
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


# In[3]:

print key['dataseoul']


# In[7]:

import requests
import urlparse

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='CardSubwayStatisticsService'
START_INDEX=1
END_INDEX=5
USE_MON='201506'


# In[9]:

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
url+=USE_MON

print url


# In[10]:

myurl='http://openapi.seoul.go.kr:8088/77657243667369643133357a756f5350/xml/CardSubwayStatisticsService/1/5/201506'


# In[13]:

responses=requests.get(myurl).text
print responses


# In[15]:

type(responses)


# In[18]:

import xml.etree.ElementTree as ET
tree=ET.fromstring(responses.encode('utf-8'))

stds=tree.findall('row')
for elements in stds:
    for elm in elements:
        print elm.text

