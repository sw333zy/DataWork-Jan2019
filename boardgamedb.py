#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

from sqlalchemy import create_engine


# In[2]:


#sqlite connect to db
db = r'database.sqlite'
engine = create_engine(r"sqlite:///{}".format(db))


# In[3]:


#getting table names
sql = "SELECT name FROM sqlite_master WHERE type = 'table';"

tables = pd.read_sql(sql, engine)
#view tables
tables


# In[4]:


#select all from board games
sql = "SELECT * FROM [BoardGames];"
gamesdf = pd.read_sql(sql, engine)
#print created board games dataframe .head()
gamesdf.head()


# In[5]:


#get total rows and columns with .shape
gamesdf.shape


# In[6]:


tables


# In[7]:


#select all from topics
sql = "SELECT * FROM [bgg.ldaOut.topics];"
topicsdf = pd.read_sql(sql, engine)
#print created topics dataframe .head()
topicsdf.head()


# In[8]:


topicsdf.shape


# In[9]:


tables


# In[10]:


#select all from terms
sql = "SELECT * FROM [bgg.ldaOut.top.terms];"
termsdf = pd.read_sql(sql, engine)
#print created terms dataframe .head()
termsdf.head()


# In[11]:


termsdf.shape


# In[12]:


tables


# In[14]:


#select all from documents
sql = "SELECT * FROM [bgg.ldaOut.top.documents];"
docsdf = pd.read_sql(sql, engine)
#print created documents dataframe .head()
docsdf.head()


# In[16]:


docsdf.shape


# In[17]:


tables


# In[18]:


#select all from bgg.topics
sql = "SELECT * FROM [bgg.topics];"
bggtopdf = pd.read_sql(sql, engine)
#print created documents dataframe .head()
bggtopdf.head()


# In[19]:


bggtopdf.shape


# In[ ]:




