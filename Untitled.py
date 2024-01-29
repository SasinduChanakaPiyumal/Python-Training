#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 5
while x<=10:
    print(x)
    x+=1
else:
    print("end of the loop")


# In[2]:


x =5
while x<=10:
    print(x)
    x+=1
print("End of the loop")


# In[7]:


x=5
while x<=10:
    if x==8:
        break
        
    print(x)
    x+=1
else:
    print("End of the loop")


# In[8]:


x=5
while x<=10:
    if x==8:
        break
        
    print(x)
    x+=1

print("End of the loop")


# In[10]:


x = int(input("Enter a value:"))
while x<=20 and x>=10:
    print("The value you enterd is",x)
    x = int(input("Enter a value:"))
else:
    print("The value you enterd is wrong")


# In[13]:


flag = True
while flag:
    x = int(input("Enter a value:"))
    if x>20 or x<10:
        flag = False
    print("The value you enterd is",x)
else:
    print("The value you enterd is wrong")


# In[19]:


pin =123456789

x = int(input("Enter pin number:"))
n=1
while x != pin:
    if n>3:
        print("Your Account has blocked")
        break
    print("You enterd invalid pin")
    x = int(input("Enter pin number again:"))
    n+=1
else:
    print("You have accessed")
    


# In[ ]:





# In[ ]:




