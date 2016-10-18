
# coding: utf-8

# # 웹데이터-3: wiki에서 'python'으로 검색해서 http url 출력하기

# In[3]:

from urllib import urlopen
keyword='python'
resp=urlopen('http://www.google.com/search?q='+keyword+'')
html=resp.read()
len(html)


# In[5]:

import re
p=re.compile('.*(error).*')
print p.search(html).group(1)


# In[6]:

import webbrowser
webbrowser.open('http://www.google.com/search?q=python')

