
# coding: utf-8

# In[2]:

import urllib2
url='http://archive.ics.uci.edu/ml/machine-learning-databases/horse-colic/horse-colic.data'
response=urllib2.urlopen(url)
html=response.read()
response.close()
print len(html)


# In[8]:

lines=html.splitlines()
data=[]

for line in lines:
    data.append(line.split())
print len(data), len(data[0])
print data[0]


# In[12]:

for i in range(0, 20):
    print data[i][3]


# In[13]:

sum=0
cnt=0
for i in range(0,20):
    val=data[i][3]
    if val is '?':
        print i, "None"
    else:
        sum+=float(val)
        cnt+=1
        print i, val, sum
        
average=float(sum/cnt)
print "count={0} sum={1} average={2:2.2f}".format(cnt, sum, average)

