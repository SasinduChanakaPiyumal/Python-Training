#!/usr/bin/env python
# coding: utf-8

# (02) Write a program to iterate from 0th number to the end number and
# append the product of the current number and the previous number in a list
# given as a parameter, to a new list. That new list should be returned.

# In[1]:


L = [2,8,9,4,6,2,4,6]


# In[5]:


[L[i]*L[i-1] if i != 0 else L[0] for i in range(len(L))]


# (03) Write a program such that for a given list, print the sum of those values
# which are present at the even indexes in list

# In[12]:


s=0
for i in range(len(L)):
    if i%2 == 0:
        s += L[i]
        print(s)   


# In[13]:


p = [L[i] for i in range(len(L)) if i%2==0]
sum(p)


# In[17]:


fun=lambda L : sum[L[i] for i in range(len(L)) if i%2==0]


# (06) For given two lists of integers, create a third list such that it should
# contain only numbers which are divisible by 3 from the first list and
# numbers which are divisible by 5 from the second list.

# In[20]:


s1 = [2,8,6,9,5,4,3,8,1]
s2 = [8,9,5,7,6,10,25,15]
[for i in range(len(s1)) s1[i] if i%2 == 0 && for e in range(len(s2)) s2[i] if i%5 == 0]


# In[21]:


s1 = [2,8,6,9,5,4,3,8,1]
s2 = [8,9,5,7,6,10,25,15]
[i for i in s1 if i%2 == 0]+[i for i in s2 if i%5 == 0]


# (09) Given an array, figure out which is larger, the first or last element in the
# array and set all the other elements to be that value. Return the changed
# array.

# In[23]:


fun = lambda L : [L[0] if L[0]>L[-1] else L[-1] for i in L]


# In[24]:


fun([9,8,6,2,3])


# In[25]:


fun([5,8,6,9,4,2,8])


# (10) Print the number of even integers in a given array.

# In[30]:


fun_even = lambda L : len([i for i in L if i%2==0])


# In[31]:


fun_even([5,8,9,6,3,5,4,7,5,8,9])


# (11) Print two separate lists of even values and odd values when you give a list

# In[33]:


def fun(L):
    L1 = [i for i in L if i%2==0]
    L2 = [i for i in L if i%2!=0]
    
    return L1,L2


# In[34]:


fun([9,8,7,5,6,4,1,2,3,6,5])


# (11) Print two separate lists of even values and odd values when you give a
# list

# In[ ]:




