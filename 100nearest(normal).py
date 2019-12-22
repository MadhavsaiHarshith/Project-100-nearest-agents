#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing required libraries
import pandas as pd
import numpy as np


# In[3]:


f=pd.read_csv('agents.tsv',sep='\t')


# In[4]:


f


# In[5]:


df=f.copy()


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


df.STATE.unique()


# In[9]:


df.CITY.nunique()


# In[10]:


gb=df.groupby('CITY')


# In[11]:


gb.groups


# In[12]:


df.groupby('STATE')['ZIPCODE'].nunique()


# In[14]:


z=pd.DataFrame([])


# In[15]:


z["NYC_dist"]=(df["ZIPCODE"]-10001)


# In[16]:


z["LA_dist"]=(df["ZIPCODE"]-90001)


# In[17]:


z["Chicago_dist"]=df["ZIPCODE"]-60007


# In[18]:


z["Houston_dist"]=df["ZIPCODE"]-77001


# In[19]:


z["phoenix_dist"]=df["ZIPCODE"]-85001


# In[20]:


z["dallas_dist"]=df["ZIPCODE"]-75001


# In[21]:


z["sanjose_dist"]=df["ZIPCODE"]-94088


# In[22]:


z["austin_dist"]=df["ZIPCODE"]-73301


# In[23]:


z["columbus_dist"]=df["ZIPCODE"]-43004


# In[24]:


z["Boston_dist"]=df["ZIPCODE"]-2212


# In[25]:


z["San Diego_dist"]=df["ZIPCODE"]-91901


# In[26]:


z=z.apply(lambda x:abs(x))


# In[27]:


z["name"]=df["NAME"]


# In[32]:


z['mean']=(z["NYC_dist"]+z['LA_dist']+z['Chicago_dist']+z['Houston_dist']+z['phoenix_dist']+z['dallas_dist']+z['sanjose_dist']+z['austin_dist']+z['columbus_dist']+z['Boston_dist']+z['San Diego_dist'])/11


# In[33]:


x=z.sort_values(by="mean")[:100]


# In[34]:


x


# In[31]:





# In[ ]:




