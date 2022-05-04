#!/usr/bin/env python
# coding: utf-8

# IIQF - first Class by Dr. Hari
# 

# What is
# - IID : Independent and identically distributed
# - Git : Git is a DevOps tool used for source code management. It is a free and open-source version control system used to handle small to very large projects efficiently. Git is used to tracking changes in the source code, enabling multiple developers to work together on non-linear development.
# - Git and Git desktop 
# - install Anaconda
# - complete Python recording
# - Excel
# - Explore Jupyter notebook
# - Create Git account
# - in GIT, create one repository
# - Jupyter notebook 
#   - markdown mode
#   - write 10 lines from your resume and get it as a text
#   
# - install IntelliJ and create first package
# 
# 

# - esc + a
# - esc +b
# - Shift + enter
# - Ctrl + enter
# - esc d
# - esc + m
# 

# 

# In[ ]:


# first python program in IntelliJ Idea

print("Amit is a professional with more than eighteen years of experience in " + "\n"
                                                                                 "implementing financial markets and infrastructure projects")

str1 = "hello ... 3rd line " + "starts "

# In[ ]:

print(str1.upper() + "\n")

print(str1.title())

# In[ ]:


n1 = 23

print("n1 = ")
print(n1)

# # home work May 7th
# basics of intellij
# - check how get plugins for putho
# - create python project
# - share the link of recorded sesson
# - create pme pythn projct with intellij
# - take jupyter notebook codde and write to one .py file and create and run 
# 
# - how to see plotted graph in IntelliJ

# # homework, 1 week, Apr 30th
# abhishek, nivththa, kayastha
# Ajay, 
# 
# - 20-30 min recorded
# - GUI git desktop, install it
# - create github acc

# # home work - everyone
# 5 min
# - Ajay, Abhishek kayastha
# - read stock market data with pandas from csv
# - read stock data from some website
# 
# -read data from website, yahoo finance
# import pandas_datareader as web
# #! pip install pandas_datareader
# web.DataReader("HDFC.NS", data_source = "yahoo")
# 
# - nse 
# - use web.DataReader("HDFC.NS",:"yhaoo ..")
# web.DataReader("HDFC.NS", data_source = "yahoo")
# iloc
# df.head(10)
# 
# 
# help (DataReader)
# 

# # home work one month
# - Abhishek
# - numpy - generate random numbers
# - normal distribution
# - uniform ddistribution
# - add some image to explain what is normal Gausian dist
# - what is the difference betwee normal an uniform dist ?
# 
# import numberp as np
# np.random.rand()

# # home work 5
# - read and write data
# 
# - read data from website for diff stocks
# - write data to database, mysql, develop code in jupyter notebook
# - use diff query for this data
# - count, mean
# 

import pandas as pd

print("imported pandas")
# !pip install pandas


# ! pip install pandas_datareader

import matplotlib.pyplot as plt
import pandas_datareader as web
import pandas_datareader.data as pd_data

# !pip install yfinance

stk = web.DataReader("HDFC.NS", data_source="yahoo")
print(stk)
print("hdfc.ns imported from yahoo")

stk['Close'].plot()
plt.show()

print("hdfc plotted")

from datetime import datetime

start = datetime(2022, 1, 1)

end = datetime(2022, 3, 31)


TD_DataFrame = web.DataReader('TD', 'yahoo', start, end)

# Define the ticker list
# import pandas as pd
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

# Fetch the data
import yfinance as yf
yf_data = yf.download(tickers_list,'2015-1-1')['Adj Close']

# Print first 5 rows of the data
# print(data.head())


# conda info --envs

data_csv = pd.read_csv('Data/AAPL.csv')

data_csv.describe()

# In[23]:


data_csv.plot()

# In[35]:


data_csv.columns

# In[28]:


data_csv['Open'].plot()

# In[29]:


data_csv['Close'].plot()

# In[37]:


data_csv.info()

# In[39]:


data_csv.info

# In[25]:


data_csv.dtypes
