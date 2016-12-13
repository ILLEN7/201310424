
# coding: utf-8

# # Rest-2. 키를 저장하고 읽기

# In[5]:

def GetKey(KeyPath):
    d=dict()
    f=open(KeyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d


# In[14]:

import os
KeyPath=os.path.join('C:/Users/ILLEN/Documents','src','key.properties')
key=GetKey(KeyPath)


# In[19]:

print key['dataseoul']

