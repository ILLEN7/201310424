
# coding: utf-8

# In[16]:

pwd


# In[2]:

import os
keyPath=os.path.join('C:/Users/ILLEN/Documents', 'src','key.properties')
print keyPath


# In[3]:

f=open(keyPath, 'r')
lines=f.readlines()
print lines


# In[4]:

key=dict()
for line in lines:
    row=line.split('=')
    print row[0], row[1]
    row0=row[0]
    key[row0]=row[1].strip()


# In[5]:

print key['dataseoul']


# In[12]:

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='ListLocaldata470401S'
START_INDEX='1'
END_INDEX='5'


# In[13]:

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
print url


# In[14]:

myurl='http://openapi.seoul.go.kr:8088/77657243667369643133357a756f5350/xml/ListLocaldata470401S/1/5'


# In[15]:

import requests
data=requests.get(url).text
print data


# In[16]:

print type(data.encode('utf-8'))


# In[17]:

import lxml
import lxml.etree
import StringIO

tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATMAN')
for node in nodes:
    print node.text

