
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


# In[4]:

import twitter

auth = twitter.oauth.OAuth(key['ACCESSTOKEN'],key['ACCESSTOKENSECRET'],
                            key['CONSUMERKEY'], key['CONSUMERSECRET'])
_client = twitter.Twitter(auth=auth)
print _client


# In[6]:

timeline = _client.statuses.home_timeline()
print type(timeline)
print len(timeline)


# In[8]:

print type(timeline[0])
for key in timeline[0].keys():
    print key,timeline[0][key]

