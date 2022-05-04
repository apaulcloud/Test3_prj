#!/usr/bin/env python
# coding: utf-8

# IIQF - IntelliJ project

# - install IntelliJ and create first package
#

# - esc + a
# - esc +b
# - Shift + enter
# - Ctrl + enter
# - esc d
# - esc + m


# first python program in IntelliJ Idea

print("Amit is a professional with more than eighteen years of experience in " + "\n"
             "implementing financial markets and infrastructure projects")

str1 = "hello ... 3rd line " + "starts "

# convert to upper case
print("UpperCase"+str1.upper() + "\n")

print("First character in upper case"+str1.title())


n1 = 23

print("n1 = ")
print(n1)

# # home work May 7th
# basics of intellij
# - check how get plugins for python
# - create python project
# - share the link of recorded session
# - create a python project with intellij
# - take jupyter notebook code and write to one .py file and create and run
# - how to see plotted graph in IntelliJ

import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
import pandas_datareader.data as pd_data #not needed

# !pip install pandas
# ! pip install pandas_datareader
# !pip install yfinance

print("imported pandas and matplotlib")
stk = web.DataReader("HDFC.NS", data_source="yahoo")
print(stk)
print("hdfc.ns imported from yahoo...plotting graph")

stk['Close'].plot() #close price only
plt.show()

print("hdfc plotted")

#Plot only for a specific Date range
from datetime import datetime
start = datetime(2022, 1, 1)
end = datetime(2022, 3, 31)

TD_DataFrame = web.DataReader('TD', 'yahoo', start, end)
print("start plotting TD")
TD_DataFrame['Close'].plot()
plt.show()

# Define the ticker list
# import pandas as pd
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

# Fetch the data
import yfinance as yf

data = yf.download(tickers_list, '2015-1-1')['Adj Close']

# Print first 5 rows of the data
print(data.head())


# conda info --envs

data_csv = pd.read_csv('Data/AAPL.csv') #file should be in exact location

data_csv.describe()

data_csv.plot()

data_csv.columns

data_csv['Open'].plot()

data_csv['Close'].plot()

data_csv.info()

data_csv.info

data_csv.dtypes
