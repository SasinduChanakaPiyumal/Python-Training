#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pyplot as plt


# In[8]:


def y_function(x):
    return x**2


# In[9]:


def y_derivative(x):
    return 2*x


# In[10]:


x = np.arange(-100,100,0.1)


# In[11]:


y = y_function(x)


# In[12]:


plt.plot(x,y)
plt.show()


# In[13]:


current_pos= (80,y_function(80))


# In[14]:


plt.plot(x,y)
plt.scatter(current_pos[0],current_pos[1],color ="red")
plt.show()


# In[20]:


L_rate = 0.001

for _ in range(1000):
    new_x = current_pos[0] - L_rate * y_derivative(current_pos[0])
    new_y = y_function(new_x)
    current_pos = (new_x,new_y)
    
    #plt.plot(x,y)
    #plt.scatter(current_pos[0],current_pos[1],color='red')
    #plt.pause(0.001)
    #plt.clf()
    print(_,current_pos)


# In[ ]:




