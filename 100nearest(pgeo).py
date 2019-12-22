#!/usr/bin/env python
# coding: utf-8

# # importing required libraries 

# In[3]:


import pandas as pd
import numpy as np
import pgeocode


# In[4]:


f=pd.read_csv('agents.tsv',sep='\t')


# In[5]:


f


# In[6]:


df=f.copy()


# In[7]:


df.head()


# In[8]:


df.info()


# In[9]:


df.STATE.unique()


# In[10]:


df.CITY.nunique()


# # Grouping them by cities

# In[11]:


gb=df.groupby('CITY')


# In[12]:


gb.groups


# In[13]:


df.groupby('STATE')['ZIPCODE'].nunique()


# # PGEO module

# In[14]:


def distance(x,y):
    dist = pgeocode.GeoDistance('US')
    return dist.query_postal_code(str(x), y)


# # Finding the distances between city and agent

# In[15]:


df['NYC_dist']=df['ZIPCODE'].apply(lambda x : distance(x,10001))


# In[16]:



df['LA_dist']=df['ZIPCODE'].apply(lambda x : distance(x,90001))


# In[17]:


df['Chicago_dist']=df['ZIPCODE'].apply(lambda x : distance(x,60007))


# In[18]:


df['Houston_dist']=df['ZIPCODE'].apply(lambda x : distance(x,77001))


# In[19]:


df['phoenix_dist']=df['ZIPCODE'].apply(lambda x : distance(x,85001))


# In[20]:


df['dallas_dist']=df['ZIPCODE'].apply(lambda x : distance(x,75001))


# In[21]:


df['sanjose_dist']=df['ZIPCODE'].apply(lambda x : distance(x,94088))


# In[22]:


df['austin_dist']=df['ZIPCODE'].apply(lambda x : distance(x,73301))


# In[23]:


df['columbus_dist']=df['ZIPCODE'].apply(lambda x : distance(x,43004))


# In[ ]:


df['Boston_dist']=df['ZIPCODE'].apply(lambda x : distance(x,"02212"))


# In[ ]:


df['San Diego_dist']=df['ZIPCODE'].apply(lambda x : distance(x,"91901"))


# In[24]:


df


# # Converting the DF to CSV

# In[42]:


df.to_csv('m_agents.csv')


# In[43]:


df


# In[44]:


df=pd.read_csv('m_agents.csv')


# In[45]:


df['mean']=(df['LA_dist']+df['Chicago_dist']+df['Houston_dist']+df['phoenix_dist']+df['dallas_dist']+df['sanjose_dist']+df['austin_dist']+df['columbus_dist']+df['Boston_dist']+df['San Diego_dist'])/9


# In[46]:


df.columns


# In[47]:


del df['Unnamed: 0']


# In[48]:


df_sorted=df.sort_values('mean')


# In[49]:


near_100=df_sorted.head(100)


# In[50]:


near_100.to_csv('100near.csv',index=False)


# In[51]:


g=pd.read_csv('100near.csv')


# # Printing 100 nearest agents to all cities

# In[55]:


g

