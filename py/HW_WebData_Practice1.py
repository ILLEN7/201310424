
# coding: utf-8

# In[1]:

import urllib
response=urllib.urlopen('https://www.google.com/finance/historical?q=KRX%3AKOSPI200&ei=sUjxV8maGYKT0gTOz7qoDA')
_html=response.read()
print response.info()


# In[152]:

import re


# In[224]:

_date=re.compile('<td class="lm">(.*?)\s(\d+)\,\s(\d+)') # Sep 30, 2016
_ohlc=re.compile('<td class="rgt">(\d+\.\d+)') # Open, High, Low, Close data
_vol=re.compile('<td class="rgt rm">(\d+\,\d+\,\d+)') # Volume


# In[36]:

res1=_date.findall(_html)
res2=_ohlc.findall(_html)
res3=_vol.findall(_html)


# In[6]:

print "kospi 200 table(date)", len(res1)


# In[229]:

type(res1), type(res2), type(res3)


# In[8]:

res1_str=str(res1)
f=open("kospi_date.txt",'w')
f.write(res1_str)
f.close()


# In[9]:

for item in res1:
    print item


# In[12]:

print "kospi 200 table(open,high,low,close)", len(res2)


# In[13]:

res2_str=str(res2)
f=open('kospi_ohlc.txt','w')
f.write(res2_str)
f.close()


# In[14]:

for item2 in res2:
    print item2


# In[16]:

print "kospi 200 table(volume)", len(res3)


# In[17]:

res3_str=str(res3)
f=open('kospi_volume.txt','w')
f.write(res3_str)
f.close()


# In[49]:

for item3 in res3:
    print item3


# In[45]:

date_f=open('kospi_date.txt','r')
line1=date_f.readline()
print line1
date_f.close()


# In[46]:

ohlc_f=open('kospi_ohlc.txt','r')
line2=ohlc_f.readline()
print line2
ohlc_f.close()


# In[48]:

vol_f=open('kospi_volume.txt','r')
line3=vol_f.readline()
print line3
vol_f.close()


# ## CSSSelector로 크롤링하기

# In[37]:

import urllib
f=urllib.urlopen("https://www.google.com/finance/historical?q=KRX%3AKOSPI200&ei=sUjxV8maGYKT0gTOz7qoDA")
mydata=f.read()


# In[46]:

import lxml.html
from lxml.cssselect import CSSSelector
html = lxml.html.fromstring(mydata)
sel = CSSSelector('#prices > table')
nodes=sel(html)


# In[48]:

len(nodes)


# In[50]:

for node in nodes:
    print node.text_content()


# ## xpath로 크롤링하기

# In[275]:

import urllib
resp=urllib.urlopen("https://www.google.com/finance/historical?q=KRX%3AKOSPI200&ei=sUjxV8maGYKT0gTOz7qoDA")
html=resp.read()
resp.close()


# In[276]:

from lxml import etree
htmlTree=etree.HTML(html)


# In[277]:

result=etree.tostring(htmlTree, pretty_print=True, method="html")


# In[278]:

print len(result)


# In[313]:

nodes=htmlTree.xpath('//*/td')


# In[324]:

len(nodes), type(nodes)


# In[330]:

for node in nodes:
    print node.text


# ## BeautifulSoup

# In[332]:

import urllib
resp=urllib.urlopen("https://www.google.com/finance/historical?q=KRX%3AKOSPI200&ei=sUjxV8maGYKT0gTOz7qoDA")
html=resp.read()
resp.close()


# In[334]:

from bs4 import BeautifulSoup
soup=BeautifulSoup(html)


# In[336]:

len(html), type(html)


# In[350]:

print len(soup),
print type(soup)


# In[351]:

strongtags=soup('strong')


# In[353]:

for tag in strongtags:
    print tag


# In[365]:

ttags=soup.findAll('td')


# In[367]:

len(ttags)


# In[378]:

for tag in ttags:
    print tag.text

