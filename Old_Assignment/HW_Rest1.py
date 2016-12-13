
# coding: utf-8

# # REST-1. ip 주소에서 지역정보 알아내기

# In[2]:

import requests
url='http://freegeoip.net/json/'
geostr=requests.get(url).text
print geostr


# In[4]:

type(geostr)


# In[6]:

import json
geojson=json.loads(geostr)


# In[8]:

type(geojson)


# In[15]:

print geojson['ip']
print geojson['country_code']


# In[18]:

country=geojson.get('country_code')
print country


# In[21]:

import urllib

def GetCountry(ip):
    res=urllib.urlopen("http://freegeoip.net/json/"+ip).read().decode('utf-8')
    resJson=json.loads(res)
    return resJson.get("country_code")


# In[22]:

print GetCountry('61.72.147.164')

