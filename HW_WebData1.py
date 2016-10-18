
# coding: utf-8

# # HW1. WebData-1. 4가지 방식으로 python.org 크롤링 하기.

# In[33]:

import urllib
response=urllib.urlopen('http://python.org/')
html=response.read()
print response.info()


# In[4]:

print len(html)
print type(html)


# ## Regular Expression

# In[35]:

import re


# In[42]:

p=re.compile('href="(http://.*?)"')


# In[43]:

type(p)


# In[44]:

res=p.findall(html)


# In[45]:

print "http url 갯수", len(res)


# In[47]:

for item in res:
    print item


# In[13]:

import re


# In[14]:

p=re.compile('<h1>(.*?)</h1>')


# In[15]:

h1tags=p.findall(html)


# In[16]:

for i in h1tags:
    print i


# In[17]:

import re


# In[18]:

p=re.compile('<p>(.*?)</p>')


# In[19]:

ptags=p.findall(html)


# In[20]:

print len (ptags)


# In[21]:

print ptags[0]


# ## xpath

# In[7]:

print len(html)


# In[8]:

from lxml import etree


# In[9]:

htmlTree=etree.HTML(html)


# In[10]:

result=etree.tostring(htmlTree, pretty_print=True, method="html")


# In[11]:

print len(result)


# In[17]:

nodes=htmlTree.xpath('//*[@href]' )  


# In[13]:

print len(nodes)


# In[15]:

for node in nodes:
    print node.attrib['href']


# ## css selector

# In[6]:

import lxml.html
from lxml.cssselect import CSSSelector
import requests


# In[7]:

r=requests.get('http://python.org/')


# In[8]:

r.status_code


# In[9]:

html=lxml.html.fromstring(r.text)


# In[10]:

sel=CSSSelector('a[href]')


# In[14]:

results=sel(html)


# In[16]:

type(results)


# In[17]:

print results


# In[19]:

for item in results:
    print item.get('href'), item.text


# ## BeautifulSoup

# In[21]:

import urllib
response=urllib.urlopen('http://python.org/')
_html=response.read()


# In[22]:

from bs4 import BeautifulSoup


# In[23]:

soup=BeautifulSoup(_html)


# In[24]:

len(_html)


# In[25]:

print type(_html)


# In[26]:

len(soup)


# In[27]:

print type(soup)


# In[28]:

print _html


# In[29]:

atags=soup.findAll('a')


# In[30]:

len(atags)


# In[31]:

for tag in atags:
    print tag


# In[32]:

for tag in atags:
    print tag.attrs['href']

