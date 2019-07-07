#!/usr/bin/env python
# coding: utf-8

# In[116]:


#Import dependencies
import pandas as pd
import numpy as np


# In[117]:


#store filepath as variable
elect_data = "Resources/Election_Data.csv"


# In[118]:


#read election data with pandas
elect_data_df = pd.read_csv(elect_data, encoding="utf-8")


# In[119]:


#Show the dataframe
elect_data_df


# In[120]:


#Change column name to read properly
elect_data_df.columns = ["Voter_ID", "County", "Candidate"]


# In[121]:


#Count the total number of votes
total_votes = elect_data_df.Voter_ID.count()
total_votes


# In[122]:


#Count the votes each candidate received
votes = pd.read_csv('Resources/Election_Data.csv').Candidate.value_counts()
votes


# In[123]:


#Turn results into dataframe
from pandas import DataFrame

votes_rcvd = {'Candidate': ['Khan','Correy','Li','OTooley'], 'Votes': [2218231, 704200, 492940, 105630]}
votes_df = DataFrame(votes_rcvd, columns= ['Candidate', 'Votes'])
votes_df.set_index('Candidate')


# In[124]:


#Add column showing percentage of total vote
votes_df["Vote_Percentage"] = (votes_df['Votes']/total_votes)*100
votes_df.set_index('Candidate')


# In[125]:


total = votes_df.apply(np.sum)
total['Candidate'] = 'total'
votes_df.append(pd.DataFrame(total.values, index=total.keys()).T, ignore_index=True)


# In[126]:


totaled_votes_df = votes_df.append({'Candidate' : 'Total', 'Votes' : total_votes, 'Vote_Percentage' : '100'} , ignore_index=True)
totaled_votes_df.set_index('Candidate')


# In[127]:


print("Election Results:\n-----------------------\nTotal Votes:")
print(total_votes)
print("-----------------------")
print(totaled_votes_df)
print("-----------------------\nWinner: Khan")


# In[128]:


#Export as text file
totaled_votes_df.to_csv('Pypoll.csv')

