#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# Calculate the variety
data=pd.read_csv("C:/Users/Lenovo/Desktop/Demo/result.csv",header=0,index_col=0)
data[data>1]=1 #In order to change the cell>1 to =1
a=data[data>0].count()#count the number of item of given papers
a=a.to_frame()


# In[3]:


#Create an empty dataframe to store the cumulative sum of dij of each paper
cumulative_sum_f=pd.DataFrame(np.zeros((data.shape[1],1)),index=data.columns.values.tolist())
#Create an empty dataframe to store the new diversity of each paper
new_diversity=pd.DataFrame(np.zeros((data.shape[1],1)),index=data.columns.values.tolist())


# In[4]:


#Input the balance
balance=pd.read_excel("C:/Users/Lenovo/Desktop/Demo/balance.xlsx",header=0,index_col=0)#input balance


# In[5]:


#Input the disparity matrix（use the 1-cosine as the distance measurement）
disparity_matrix=pd.read_excel("C:/Users/Lenovo/Desktop/Demo/1-cosine.xlsx",header=0,index_col=0)#input disparity matrix


# In[6]:


#Calculate the cumulative sum of dij 
for i in range(0,data.shape[1]):
    data_array=data.iloc[:,i].values
    data_arrayt=np.transpose(data_array)
    cumulative_sum=np.dot(np.dot(data_arrayt,disparity_matrix),data_array)
    cumulative_sum_f.iloc[i,0]=cumulative_sum


# In[7]:


#Calculate the new diversity and export the result
for j in range(0,data.shape[1]):
    diversity=a.iloc[j,0]*balance.iloc[j,0]*cumulative_sum_f.iloc[j,0]
    new_diversity.iloc[j,0]=diversity
new_diversity.to_csv("C:/Users/Lenovo/Desktop/Demo/new_diveristy.csv")


# In[ ]:




