#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt


# In[8]:


x = np.array([5,10,15,20,25,30]).reshape((-1,1))
y = np.array([6,12,18,24,30,36])


# In[9]:


plt.scatter(x,y,color = 'blue')


# In[10]:


model = LinearRegression()
model.fit(x,y)


# In[15]:


new_x = np.array([1,2,3,4,5]).reshape((-1,1))


# In[16]:


pred = model.predict(new_x)
pred


# In[19]:


plt.scatter(x,y,color='blue')
x = x.flatten()
y = y.flatten()
m,c = np.polyfit(x, y, 1)
plt.plot(x, m*x+c)


# In[ ]:




