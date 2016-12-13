
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


# In[54]:

import requests
import urlparse

KEY=str(key['dataseoul'])
TYPE='json'
SERVICE='CardSubwayStatisticsService'
START_INDEX=1
END_INDEX=5
USE_MON='201306'


# In[55]:

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


# In[56]:

myurl='http://openapi.seoul.go.kr:8088/77657243667369643133357a756f5350/json/CardSubwayStatisticsService/1/5/201306'


# In[61]:

import requests
response=requests.get(myurl).text
print response


# In[62]:

import json
jd= json.loads(response)


# In[34]:

import pymongo


# In[35]:

from pymongo import MongoClient
client=MongoClient('localhost:27017')


# In[46]:

db=client.seouldata


# In[63]:

db.myseoul.insert({
        response
    })


# In[38]:

empCol=db.mytable.find()


# In[39]:

type(empCol)


# In[40]:

for emp in empCol:
    print emp


# In[41]:

type(emp)


# In[43]:

emp['EnglishName']

