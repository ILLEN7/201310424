
# coding: utf-8

# In[3]:

import lxml.html
from lxml.cssselect import CSSSelector
import requests
r=requests.get('https://www.ieee.org/conferences_events/index.html')
html=lxml.html.fromstring(r.text)


# In[4]:

print lxml.html.tostring(html)


# In[21]:

sel=CSSSelector('#inner-container > div.content-gray > div.content-lc > div.content-lc-bottom > div.content-c > div:nth-child(1) > div > div:nth-child(2)')


# In[22]:

results=sel(html)


# In[24]:

for item in results:
    print lxml.html.tostring(item)


# In[27]:

sel=CSSSelector('#inner-container > div.content-gray > div.content-lc\
> div.content-lc-bottom > div.content-c > div:nth-child(1)\
> div > div a')
results=sel(html)
print results


# In[28]:

for item in results:
    print item.text


# In[31]:

sel=CSSSelector('#inner-container > div.content-gray > div.content-lc\
> div.content-lc-bottom > div.content-c > div:nth-child(1)\
> div > div p > br')
result=sel(html)
print result


# In[33]:

for item in result:
    print lxml.html.tostring(item)


# In[36]:

sel=CSSSelector('div.box-c-indent p > a')
result=sel(html)
print len(result)
print result


# In[37]:

for item in result:
    if item is not None:
        print item.text_content()

