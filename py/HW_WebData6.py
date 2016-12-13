
# coding: utf-8

# In[5]:

import urllib2
import requests
urlperson='http://www.kbreport.com/player/list?key=오지환'
urlbase="http://www.kbreport.com/leader/main?"
url1="rows=20&order=oWAR&orderType=DESC&"
url2="teamId=5&defense_no=2&year_from=2015&year_to=2015&split01=&split02_1=&split02_2=&r_tpa_count=&tpa_count=0"
urlbaseball=urlbase+url1+url2
print urlbaseball


# In[2]:

print urlperson


# In[8]:

database=requests.get(urlbaseball).text
dataperson=requests.get(urlperson).text


# In[9]:

print dataperson [16000:17000]


# In[11]:

print database[6000:7000]


# In[12]:

print database.find('top-score-top')
print database.find('top-score end')


# In[13]:

mydata=database[6340:8353+len('top-score end')]
import re
p=re.compile(u'.승.+')
found=p.findall(mydata)

print found
for item in found:
    print item


# In[14]:

database.encode('utf-8')
print database

from BeautifulSoup import BeautifulSoup


# In[15]:

soup=BeautifulSoup(database)


# In[16]:

print type(soup)


# In[17]:

tsts=soup.findAll('p')


# In[18]:

len(tsts)


# In[19]:

print tsts


# In[20]:

for tst in tsts:
    print tst

