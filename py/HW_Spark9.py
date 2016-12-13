
# coding: utf-8

# In[5]:

import os
import findspark

home=os.getenv("HOME")
spark_home=os.path.join("C:/Users/ILLEN/Downloads/spark-1.6.0-bin-hadoop2.6/spark-1.6.0-bin-hadoop2.6")
findspark.init(spark_home)       


# In[7]:

import pyspark 
conf=pyspark.SparkConf().setAppName("myApp") 
sc=pyspark.SparkContext(conf=conf)
sc


# In[2]:

df = sqlCtx.createDataFrame(
    [
        ['No','young', 'false', 'false', 'fair'],
        ['No','young', 'false', 'false', 'good'],
        ['Yes','young', 'true', 'false', 'good'],
        ['Yes','young', 'true', 'true', 'fair'],
        ['No','young', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'good'],
        ['Yes','middle', 'true', 'true', 'good'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'good'],
        ['Yes','old', 'true', 'false', 'good'],
        ['Yes','old', 'true', 'false', 'excellent'],
        ['No','old', 'false', 'false', 'fair'],
    ],
    ['cls','age','f1','f2','f3']
)


# In[4]:

df.printSchema()


# In[8]:

from pyspark.ml.feature import StringIndexer
labelIndexer = StringIndexer(inputCol="cls", outputCol="labels")
model=labelIndexer.fit(df)

