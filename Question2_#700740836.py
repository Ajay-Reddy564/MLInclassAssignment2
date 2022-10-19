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









