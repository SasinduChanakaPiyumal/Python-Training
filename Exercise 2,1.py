#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func1(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()


# In[2]:


func1(10)


# In[3]:


def func2(n):
    for i in range(0,n):
        for j in range(i):
            print("*",end=" ")
        print()


# In[4]:


func2(20)


# In[5]:


def func3(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end= "")
        for k in range(i+1):
            print("*",end=" ")
        print()
        


# In[6]:


func3(8)


# In[38]:


def func4(n):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" ",end= "")
        for k in range(i):
            print("*",end=" ")
        print()


# In[39]:


func4(8)


# In[16]:


def func5(n):
    func3(n)
    func4(n)


# In[17]:


func5(8)


# In[32]:


def func6(n):
    func3(n)
    func4(n-1)


# In[40]:


func6(8)


# In[47]:


def func7(n):
    for i in range(n):
        print(" "*(n-1-i) +" *"*(i+1))
    for i in range(n-1):
        print(" "*(i+1)+" *"*(n-1-i))


# In[48]:


func7(8)


# In[ ]:




