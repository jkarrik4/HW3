#!/usr/bin/env python
# coding: utf-8

# In[241]:


#Import dependencies
import pandas as pd
import numpy as np


# In[242]:


#Store filepath in a variable
budget_data = "Resources/Budget_Data.csv"


# In[243]:


#Read budget_data with pandas
budget_data_df = pd.read_csv(budget_data, encoding="utf-8")


# In[244]:


#Show the 
budget_data_df.head()


# In[ ]:





# In[245]:


#Change headers
budget_data_df.columns = ["Months", "Profits"]
budget_data_df.head()


# In[246]:


#Count the total number of months recorded
total_months = budget_data_df.Months.count()
print("Total Months:") 
print(total_months)


# In[247]:


#Find total profit/loss
total_profit = budget_data_df.Profits.sum()
print("Total Profit:")
print(total_profit)


# In[248]:


#Create column showing change in value from one row to next
budget_data_df["Profit_Change"] = budget_data_df.Profits.diff()
budget_data_df.head()


# In[249]:


budget_data_df["Profits"] = budget_data_df["Profits"].map("${:,.2f}".format)

budget_data_df.head()


# In[250]:


#Find average of change in profit/loss
avg_profit_change = budget_data_df.Profit_Change.mean()
print("Average Change in Profit:")
print(avg_profit_change)
d = {'Total Months:' : total_months, 'Total ($):' : total_profit, 'Average Change ($):' : avg_profit_change, 'Greatest Increase in Profits ($):' : budget_data_df.Profit_Change.max(), 'Greatest Decrease in Losses ($):' : budget_data_df.Profit_Change.min()}
d_df = pd.DataFrame.from_dict(d, orient ='index', dtype='int32')


# In[251]:


#Find greatest increase in profits
print("Greatest Increase in Profit:")
print(budget_data_df.Profit_Change.max())


# In[252]:


#Find greatest decrease in losses
print("Greatest Decrease in Losses:")
print( budget_data_df.Profit_Change.min())


# In[253]:


#Create data frame to present info
from pandas import DataFrame

PyBank = {'A': ['Total Months','Total($)','Average Change($)','Greatest Increase in Profits($)','Greatest Decrease in Profits($)'], 'B':[total_months, total_profit, avg_profit_change, budget_data_df.Profit_Change.max(), budget_data_df.Profit_Change.min()]}

pb = DataFrame(PyBank, columns= ['A', 'B'])     
pb["B"] = pb["B"].map("{:,.2f}".format)
pb.set_index('A')      


# In[256]:


#Export dataframe as text file
pb.to_csv('Pybank.csv')


# In[ ]:





# In[ ]:




