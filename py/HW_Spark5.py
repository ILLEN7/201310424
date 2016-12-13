
# coding: utf-8

# In[2]:

{"name":"Michael"}
{"name":"Andy", "age":30}
{"name":"Justin", "age":19}


# In[3]:

pDF= sqlCtx.read.json("/home/jsl/Downloads/spark-1.6.0-bin-hadoop2.6/examples/src/main/resources/people.json")


# In[ ]:

type(pDF)


# In[5]:

pDF.filter(pDF['age'] > 21).show()
pDF.registerTempTable("people")
sqlCtx.sql("select name from people").show()


# In[6]:

twitterDF= sqlCtx.read.json("src/ds_twitter_1_noquote.json")
twitterDF.printSchema()


# In[7]:

twitterDF.select('text').show()


# In[ ]:

twitterDF.registerTempTable("twitter")
sqlCtx.sql("select text from twitter").show()

