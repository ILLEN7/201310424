
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


# In[17]:

import twitter

auth = twitter.oauth.OAuth(key['ACCESSTOKEN'],key['ACCESSTOKENSECRET'],
                            key['CONSUMERKEY'], key['CONSUMERSECRET'])
client = twitter.Twitter(auth=auth)
print client


# In[29]:

import oauth2 as oauth
import json

consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])
client = oauth.Client(consumer, token)


# In[22]:

q = '#seoul'
count = 200
max_id='805703606938648577'

search_results = _client.search.tweets(q=q, count=count, max_id=max_id)
statuses = search_results['statuses']


# In[28]:

print len(statuses)
print type(statuses)


# In[30]:

import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'seoul','count':200,'max_id':'754295227351871489'}
mybody=urllib.urlencode(myparam)
response, content = client.request(url+"?"+mybody, method="GET")
tsearch_json = json.loads(content)


# In[32]:

content


# In[33]:

print len(tsearch_json)
print len(tsearch_json['statuses'])


# In[34]:

import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"


# In[35]:

prev_id=None
f=open('_todel3.txt','a')
for i in range(0,20):
    myparam={'q':'seoul','count':10,'max_id':prev_id}
    mybody=urllib.urlencode(myparam)
    response, content = client.request(url+"?"+mybody, method="GET")
    tsearch_json = json.loads(content)
    print len(tsearch_json['statuses'])
    for i,tweet in enumerate(tsearch_json['statuses']):
        #print str(i),tweet['id'],tweet['user']['name'],tweet['text']
        f.write(json.dumps([str(i),tweet['id'],tweet['user']['name']]))
        f.write("\n")
    prev_id=int(tsearch_json['statuses'][-1]['id'])-1
    print prev_id
f.close()

