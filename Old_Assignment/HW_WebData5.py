
# coding: utf-8

# # 웹데이터-5: 국제학회 목록을 크롤링하기

# ## CSS Selector 활용해 학회 일정 크롤링하기

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
# #을 왜 붙이는 것일까? '#'의 뜻은???


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


# ## CSSSelector 활용해서 학회 정보까지 크롤링하기

# In[31]:

sel=CSSSelector('#inner-container > div.content-gray > div.content-lc\
> div.content-lc-bottom > div.content-c > div:nth-child(1)\
> div > div p > br')
result=sel(html)
print result


# In[33]:

for item in result:
    print lxml.html.tostring(item)


# ## 간단한 Selector로 크롤링하기

# In[36]:

sel=CSSSelector('div.box-c-indent p > a')
result=sel(html)
print len(result)
print result


# In[37]:

for item in result:
    if item is not None:  # 이것이 무슨 뜻인가..!!!
        print item.text_content()

