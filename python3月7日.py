#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(10)
print(x)


# In[6]:


plt.hist(x,100)

plt.xlabel("x value")
plt.ylabel("Numbers of elements")
plt.show()


# In[10]:


mu, sigma = 0, 0.1 #mean and standard derivation
s = np.random.normal(mu, sigma, 10000)
plt.hist(s,10)

#plt.xlim(-2,2)
plt.show()


# In[24]:


import numpy as np
import matplotlib.pyplot as plt
import math

#SI unit
h = 6.62*10**-34 #Planck constant
c = 3*10**8      #speed of light
k = 1.38*10**-23 #Boltzmann Constant JK^-1

v = np.linspace(10**0, 10**15, 1000, endpoint=True)
#print(v)

T=float(input("Input temperature:"))
B=2*h*v**3/c**2/(math.e**(h*v/k/T)-1)
#print(B)

#plt.errorbar(v, B, yerr=0.5*B, xerr=0.1*v, ecolor="green")


plt.xlabel("Frequency (Hz)")
plt.ylabel("Intensity Watts/Hz/m^2")

num = 1000
dB = np.random.normal(0., 10**-8.5, num)
B += dB

plt.plot(v,B,'.')

plt.show()         


# In[ ]:




