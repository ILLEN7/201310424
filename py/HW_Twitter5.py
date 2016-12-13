
# coding: utf-8

# In[4]:

import os
keyPath=os.path.join('C:/Users/ILLEN/Documents', 'src','key.properties')

f=open(keyPath, 'r')
lines=f.readlines()

key=dict()
for line in lines:
    row=line.split('=')
    row0=row[0]
    key[row0]=row[1].strip()


# In[5]:

import twitter

auth = twitter.oauth.OAuth(key['ACCESSTOKEN'],key['ACCESSTOKENSECRET'],
                            key['CONSUMERKEY'], key['CONSUMERSECRET'])
_client = twitter.Twitter(auth=auth)
print _client


# In[7]:

import oauth2 as oauth
import json

consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])
client = oauth.Client(consumer, token)


# In[12]:

import urllib
url = 'https://api.twitter.com/1.1/followers/list.json'

response, content = client.request(url, method='GET')
tfollower_json = json.loads(content)


# In[14]:

print len(tfollower_json)
print type(tfollower_json)


# In[15]:

for k,v in tfollower_json.iteritems():
    print k


# In[16]:

for k,v in tfollower_json['users'][0].iteritems():
        print k


# In[17]:

for i in tfollower_json['users']:
    print i['id'],i['screen_name']

