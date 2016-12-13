
# coding: utf-8

# # HW6. WebData-6. 프로야구 기록 scraping

# In[13]:

import urllib2
import requests
urlperson='http://www.kbreport.com/player/list?key=오지환'
urlbase="http://www.kbreport.com/leader/main?"
url1="rows=20&order=oWAR&orderType=DESC&"
url2="teamId=5&defense_no=2&year_from=2015&year_to=2015&split01=&split02_1=&split02_2=&r_tpa_count=&tpa_count=0"
urlbaseball=urlbase+url1+url2
print urlbaseball


# In[14]:

print urlperson


# In[8]:

database=requests.get(urlbaseball).text
dataperson=requests.get(urlperson).text


# In[19]:

print dataperson [16000:17000]


# In[21]:

print database[6000:7000]


# ## Regular expression

# In[26]:

print database.find('top-score-top')
print database.find('top-score end')


# In[29]:

mydata=database[6340:8353+len('top-score end')]
import re
p=re.compile(u'.승.+')
found=p.findall(mydata)

print found
for item in found:
    print item


# ## BeautifulSoup

# In[33]:

database.encode('utf-8')
print database

from BeautifulSoup import BeautifulSoup


# In[37]:

soup=BeautifulSoup(database)


# In[39]:

print type(soup)


# In[57]:

tsts=soup.findAll('p')


# In[58]:

len(tsts)


# In[59]:

print tsts


# In[50]:

for tst in tsts:
    print tst

