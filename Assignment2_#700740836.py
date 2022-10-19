#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np

#creating a random vector of size 15 with integers in the range 1-20 as given in the question
x = np.random.randint(1,20,15)
print("Original array:")
print(x)

#Here we are Reshaping the array using a method called reshape
y = x.reshape(3, 5)
print("Reshaped array:")
print(y)

#printing the Shape of an array
print('Shape of the array:',y.shape)

#replacing the max in each row with 0
for i in y:
    i[i == max(i)] = 0
    
print("Replacing the max in each row with Zero")
print(y)
   
   
   

       
   


# In[2]:


#importing pandas package 
import pandas as pd

data= pd.read_csv("data.csv") #reading the file given in the question
data.head()


# In[3]:


#description of the data using a method called describe which gives the whole values
data.describe()


# In[4]:


#check the dataframe if it has null values
data.isnull().any()


# In[5]:


#replacing the null values with mean
data.fillna(data.mean(), inplace=True)
data.isnull().any()


# In[6]:


#Selecting two columns Pulse and Calories and calculating min,max,count,mean of the values in those columns
data.agg({'Pulse':['min','max','count','mean'],'Calories':['min','max','count','mean']})


# In[7]:


#extracting the data values that satisfy the given condition in the ' calories' column
data.loc[(data['Calories']>500)&(data['Calories']<1000)]


# In[8]:


#fetching the data within calories values > 500 and pulse < 100.
data.loc[(data['Calories']>500)&(data['Pulse']<100)]


# In[9]:


#checking for null values
data.fillna(data.mean(), inplace=True)
data.isnull().any()


# In[10]:


#deleting 'Maxpulse' column here
df_modified = data[['Duration','Pulse','Calories']]
df_modified.head()


# In[16]:


#Here we are taking the main table again in order to excute the delete "Maxpulse" column method in the next question
import pandas as pd

data= pd.read_csv("data.csv")
data.head()


# In[17]:


#Deleting "Maxpulse"
del data['Maxpulse']
data.head()


# In[18]:


data.dtypes


# In[20]:


data.fillna(data.mean(), inplace=True)
data.isnull().any()


# In[21]:


#Changing the coulumn's data type to int 
import numpy as np
data['Calories'] = data['Calories'].astype(np.int64)
data.dtypes


# In[22]:


#Plotting the data
data.plot.scatter(x='Duration',y='Calories',c='DarkBlue')


# In[23]:


import matplotlib.pyplot as plt
# Given Data to plot
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# Here i am exploding 1st slice
explode = (0.1, 0, 0, 0,0,0)  
# Final Plot
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()


# In[ ]:




