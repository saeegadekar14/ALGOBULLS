#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install alpha_vantage


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
import numpy as np


# In[3]:


API_key='LCGAAANH9ATJWBC2'
ts = TimeSeries(key=API_key, output_format='pandas')


# In[4]:


class ScriptData:
    def __init__(self, script):
        self.script = script
    
   # @classmethod
    def fetch_intraday_data(self):
        data=ts.get_intraday(self.script)
        return data
    def convert_intraday_data(self):
        df=pd.DataFrame(self.fetch_intraday_data())    
        return df


# In[5]:


script_data=ScriptData('GOOGL')
script_data.fetch_intraday_data()
script_data.convert_intraday_data()
data=ts.get_intraday('GOOGL')
data


# In[6]:


try:
    ts.get_intraday('NVDA')
    print('True')
except ValueError:
    print('False')


# In[7]:


try:
    ts.get_intraday('GOOGL')
    print('True')
except ValueError:
    print('False')


# In[8]:


df=data[0]
df


# In[9]:


type(df)


# In[10]:


df.columns = df.columns.str.replace(' ', '')
df.loc[:,"4.close"]


# In[11]:


df['pandas_SMA_3'] = df.iloc[:,1].rolling(window=5).mean()


# In[12]:


df.loc[:,"pandas_SMA_3"]


# In[13]:


def indicator1(f,timeperiod):
    p=ts.get_intraday(f)
    df=p[0]
    df['pandas_SMA'] = df.iloc[:,1].rolling(window=timeperiod).mean()
    return df.loc[:,"pandas_SMA"]


# In[16]:


indicator1('GOOGL',5)


# In[17]:


indicator1('AAPL',5)


# In[ ]:




