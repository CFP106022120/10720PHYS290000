#!/usr/bin/env python
# coding: utf-8

# In[3]:


fp = open('Alice.txt','r',encoding = 'UTF-8')

line = fp.readline()

while line:
    print(line)
    line = fp.readline()
    
fp.close()


# In[15]:


import matplotlib.pyplot as plt
fp = open('Alice.txt','r',encoding = 'UTF-8')
line = fp.readline()

my_dict = {}

while line:
    s = line.split()
    for x in s:
        if x not in my_dict:
            my_dict[x] = 1
        else:
            my_dict[x] = my_dict[x] + 1
    line = fp.readline()

fp.close()

num = []

for key in my_dict:
    num.append(my_dict[key])
    
print(len(num))
num.sort()
num.reverse()

plt.loglog(range(len(num)),num)
plt.xlabel('Rank of the word')
plt.ylabel('Number of the occurance')
plt.show()


# In[ ]:




