
# coding: utf-8

# In[21]:

get_ipython().system(u'ls data/ds_spark_wiki.txt')


# In[17]:

lines = sc.textFile("data/ds_spark_wiki.txt")
wc = lines    .flatMap(lambda x: x.split(' '))


# In[18]:

wc.collect()


# In[27]:

from operator import add
wc = sc.textFile("data/ds_spark_wiki.txt")    .flatMap(lambda x: x.split(' '))    .map(lambda x: (x.lower().rstrip().lstrip().rstrip(',').rstrip('.'), 1))    .reduceByKey(add)


# In[28]:

wc.sount()


# In[29]:

wc.first()


# In[30]:

from operator import add
wc = sc.textFile("data/ds_spark_wiki.txt")    .map(lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower())    .map(lambda x:x.split())    .map(lambda x:[(i,1) for i in x])


# In[31]:

for e in wc.collect():
    print e


# In[33]:

documents = sc.textFile("data/ds_spark_wiki.txt").map(lambda line: line.split(" "))


# In[34]:

from pyspark.mllib.feature import HashingTF

hashingTF = HashingTF()
tf = hashingTF.transform(documents)


# In[35]:

tf.collect()

