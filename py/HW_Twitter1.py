
# coding: utf-8

# In[1]:

import os
keyPath=os.path.join('C:/Users/ILLEN/Documents', 'src','key.properties')

f=open(keyPath, 'r')
lines=f.readlines()

key=dict()
for line in lines:
    row=line.split('=')
    row0=row[0]
    key[row0]=row[1].strip()


# In[3]:

import twitter

auth = twitter.oauth.OAuth(key['ACCESSTOKEN'],key['ACCESSTOKENSECRET'],
                            key['CONSUMERKEY'], key['CONSUMERSECRET'])
_client = twitter.Twitter(auth=auth)
print _client


# In[4]:

_client.statuses.update(status="Hello Twitter 1 160924")

