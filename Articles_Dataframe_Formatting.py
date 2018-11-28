#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import glob
import csv


# In[5]:


path = "/Users/parkerglenn/Desktop/DataSets/News_Articles"


# In[14]:


list_ = []
all_files = glob.glob(path + "/*.csv")
frame = pd.DataFrame()


# In[7]:


df_from_each_file = (pd.read_csv(f) for f in all_files)
concatenated_df = pd.concat(df_from_each_file, ignore_index = True)


# In[8]:


dates = concatenated_df['date']


# In[9]:


url = concatenated_df['url']


# In[10]:


df1 = concatenated_df[~concatenated_df['date'].isna()]
df = df1[~df1['url'].isna()]
df = df.reset_index()
df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)


# In[11]:


df = df.sort_values(by=['date'])


# In[12]:


df.to_csv("all_GOOD_articles.csv")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




