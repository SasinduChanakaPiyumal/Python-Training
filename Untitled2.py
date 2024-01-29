#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[15]:


#x = np.array([5,6,7,8,9,12])
#y = np.array([3,4,5,7,8,10])

x = np.random.rand(20)
y = np.random.rand(20)


# In[16]:


m = 0
b = 0
l_rate =0.01
n = len(x)


# In[19]:


for i in range(200):
    J = (1/n)*sum(((m*x+b)-y)**2)
    
    m = m- l_rate*((2/n)*sum((m*x+b)-y)*(x))
    b = b- l_rate*((2/n)*sum((m*x+b)-y))
    print('cost {} in {} iteration'.format(J,i))
print('m {} b {}'.format(m,b))
   


# In[20]:


plt.scatter(x,y)


# In[22]:


plt.scatter(x,m*x+b)


# In[ ]:




