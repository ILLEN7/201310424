
# coding: utf-8

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

