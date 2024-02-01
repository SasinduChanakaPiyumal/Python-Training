#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Employee():
    pass


# In[2]:


e1 = Employee()
e2 = Employee()
e3 = Employee()
e4 = Employee()


# In[3]:


print(e1)
print(e2)
print(e3)
print(e4)


# In[4]:


print(type(e1))
print(type(e2))
print(type(e3))


# In[5]:


class Student():
    pass


# In[6]:


s1= Student()


# In[7]:


isinstance(e1,Employee)


# In[8]:


isinstance(s1,Employee)


# In[9]:


class Employee():
    
    def __init__(self,a,b,c):
        self.name = a
        self.age = b
        self.salary = c


# In[10]:


e1 = Employee("Sam",21,75000)
e2 = Employee("Jane",24,100000)


# In[11]:


e1.name


# In[12]:


e2.age


# In[13]:


e2.salary


# In[14]:


e1.__dict__


# In[15]:


e2.__dict__


# In[ ]:




