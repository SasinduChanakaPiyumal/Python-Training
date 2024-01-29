#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
x = np.random.randn(10,1)
y = 2*x + np.random.rand()


# In[2]:


#new_y = m*x + c
m = 0.0
c = 0.0

learning_rate = 0.001


# In[3]:


# J = [(y-new_y)**2]/N
# J = {[y-(m*x + c)]**2}/N
def descend(x,y,m,c,learning_rate):
    dJdm = 0.0
    dJdc = 0.0
    N = x.shape[0]
    for xi,yi in zip(x,y):
        dJdc += -2 * (yi - (m * xi + c)) * (1/N)
        dJdm += -2 * (xi) * (yi - (m * xi + c)) * (1/N)
    m = m - learning_rate*dJdm
    c = c- learning_rate*dJdc
    return m,c    


# In[4]:


for i in range(1000):
    m,c= descend(x,y,m,c,learning_rate)
    new_y = m*x + c
    deff = np.divide(np.sum((y-new_y)**2,axis=0),x.shape[0])
    print(f'{i} deff is {deff},parameters m:{m}, c:{c}' )


# In[ ]:




