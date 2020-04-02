#!/usr/bin/env python
# coding: utf-8

# In[44]:


primes = []
with open("./primes.txt", "r") as f:
    for line in f:
        for char in line.split(" "):
            if char == "" or char == "\n":
                continue
            primes.append(int(char))
        


# In[45]:


len(primes)


# In[74]:


x = list(range(1, len(primes)))


# In[75]:


len(x)


# In[76]:


y = []
for i, a in enumerate(primes):
    if i == len(primes) - 1:
        break
    y.append(primes[i+1]**2 - a**2)


# In[77]:


len(y)


# In[84]:


# Save data as csv
with open("prime_data.csv", "w+") as f:
    for i, a in enumerate(y):
        f.write(f'{i},{a}\n')


# In[ ]:




