
# coding: utf-8

# In[2]:

import pymongo


# In[4]:

from pymongo import MongoClient
client = MongoClient('localhost:27017')
db=client.Employees


# In[5]:

_id=1
_name='js'
_age=11
_country='ko'


# In[6]:

db.mytable.insert({
    'd': _id,
    'name': _name,
    'age': _age,
    'country': _country
})


# In[10]:

db.Employees.insert_one(
    {
    'd': _id,
    'name': _name,
    'age': _age,
    'country': _country
     })


# In[11]:

empCol = db.Employees.find()
for emp in empCol:
        print emp


# In[12]:

_name='jslim'
_age=123
db.Employees.update_one(
        {'id': _id},
        {
        '$set': {
            'name':_name,
            'age':_age,
        }
        }
    )


# In[13]:

empCol = db.Employees.find()
for emp in empCol:
        print emp

