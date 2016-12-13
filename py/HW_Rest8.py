
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

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='CardBusStatisticsService'
START_INDEX=str(1)
END_INDEX=str(5)
USE_MON=str(201512)
BUS_ROUTE_NO=str(7016)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,USE_MON,BUS_ROUTE_NO)
print params[31:]


# In[5]:

url="http://openapi.seoul.go.kr:8088/"
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=str(START_INDEX)
url+='/'
url+=str(END_INDEX)
url+='/'
url+=USE_MON
url+='/'
url+=BUS_ROUTE_NO

print url


# In[6]:

myurl='http://openapi.seoul.go.kr:8088/77657243667369643133357a756f5350/xml/CardBusStatisticsService/1/5/201512/7016'


# In[7]:

data=requests.get(myurl).text
print data

