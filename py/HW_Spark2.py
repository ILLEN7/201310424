
# coding: utf-8

# In[10]:

import os
import findspark

home=os.getenv("HOME")
spark_home=os.path.join("C:/Users/ILLEN/Downloads/spark-1.6.0-bin-hadoop2.6/spark-1.6.0-bin-hadoop2.6")
findspark.init(spark_home)       


# In[11]:

import pyspark 
conf=pyspark.SparkConf().setAppName("myApp") 
sc=pyspark.SparkContext(conf=conf)


# In[12]:

print sc


# In[13]:

sc.version
sc.master
sc._conf.get("spark.jars.packages")
sc._conf.getAll()

