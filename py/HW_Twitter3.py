
# coding: utf-8

# In[2]:

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


# In[27]:

import oauth2 as oauth
import json

consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])
client = oauth.Client(consumer, token)


# In[23]:

q = '#seoul'
count = 20
search_results = _client.search.tweets(q=q, count=count)
statuses = search_results['statuses']


# In[24]:

print len(statuses)
print type(statuses)


# In[25]:

print statuses[0].keys()


# In[26]:

for i,tweet in enumerate(statuses):
    print "[%d]\t%d\t%s:%s" % (i,tweet['id'],tweet['user']['name'],tweet['text'])


# In[28]:

import urllib
url1 = 'https://api.twitter.com/1.1/search/tweets.json'
myparam={'q':'seoul','count':20}
mybody=urllib.urlencode(myparam)

resp, tsearch = client.request(url1+"?"+mybody, method="GET")
tsearch_json = json.loads(tsearch)


# In[29]:

print type(tsearch_json)
print tsearch_json.keys()
print len(tsearch_json['statuses'])


# In[30]:

len(tsearch_json['statuses'][0])


# In[31]:

for i,tweet in enumerate(tsearch_json['statuses']):
    print "[%d]\t%d\t%s:%s" % (i,tweet['id'],tweet['user']['name'],tweet['text'])

