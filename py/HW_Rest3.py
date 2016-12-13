
# coding: utf-8

# In[27]:

import os
KeyPath=os.path.join('C:/Users/ILLEN/Documents','src','key.properties')

def GetKey(KeyPath):
    d=dict()
    f=open(KeyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d

key=GetKey(KeyPath)


# In[28]:

key['dataseoul']


# In[40]:

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX=str(1)
END_INDEX=str(10)
LINE_NUM=str(2)


# In[42]:

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
print params[31:]

import urlparse
_url='http://openapi.seoul.go.kr:8088/'
url1=urlparse.urljoin(_url,params)


# In[43]:

url='http://openapi.seoul.go.kr:8088/'
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
url+=LINE_NUM

print url


# In[44]:

myurl='http://openapi.seoul.go.kr:8088/77657243667369643133357a756f5350/xml/SearchSTNBySubwayLineService/1/10/2'


# In[54]:

import urllib
requests=urllib.urlopen(myurl)
response=requests.read().text
print response


# In[52]:

type(response)


# In[50]:

import requests
data=requests.get(myurl).text
print data


# In[53]:

type(data)


# In[55]:

import re
s=re.compile('<STATION_NM>(.+?)</STATION_NM>')
res=s.findall(data)


# In[56]:

for i in res:
    print i


# In[57]:

import xml.etree.ElementTree as ET
tree=ET.fromstring(data.encode('utf-8'))


# In[58]:

stds=tree.findall('row')
for elements in stds:
    for elm in elements:
        print elm.text


# In[59]:

import lxml
import lxml.etree
import StringIO

tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATION_NM')

for node in nodes:
    print node.text

