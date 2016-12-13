
# coding: utf-8

# In[2]:

import os
import findspark

home=os.getenv("HOME")
spark_home=os.path.join("C:/Users/ILLEN/Downloads/spark-1.6.0-bin-hadoop2.6/spark-1.6.0-bin-hadoop2.6")
findspark.init(spark_home)       


# In[5]:

import pyspark 
conf=pyspark.SparkConf().setAppName("myApp") 
sc=pyspark.SparkContext(conf=conf)


# In[7]:

sc


# In[9]:

from pyspark.mllib.linalg import Vectors
dv1=Vectors.dense([0.0, 1.1, 0.1])
print dv1


# In[11]:

import numpy as np

dv2 = np.array([1.0, 2.1, 3.2])
print dv1
print dv2


# In[12]:

dv2 = [1.0, 2.1, 3.2]


# In[13]:

sv1 = Vectors.sparse(3, [1, 2], [1.0, 3.0])
print sv1.toArray()


# In[14]:

sv2 = sps.csc_matrix((np.array([1.0,3.0]), np.array([0,2]), np.array([0,2])), shape = (3,1))
sv2.todense()
print sv2

