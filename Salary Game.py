#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import matplotlib.pyplot as plt
import numpy as np

print('學生數量:')
student = int(input())  
print('每人一開始有多少錢:')
money   = int(input())  
print('輸一次給多少錢:')
lost_money = int(input()) 
print('方法:')
way     = input() # a不可負債 b可負債
print('times:')
times   = int(input()) #猜拳幾次

student_money = list() #建立一個學生有多少錢的列表
student_money = [money] * student #初始化給個人的錢
if way == 'a': #方式a
    while times != 0:
        times = times - 1
        rs = random.sample(range(0,student),2)   #隨機挑兩位學生
        winner = random.randint(0,3)             #哪位獲勝 
        
        if winner == 2:
            continue
        
        if student_money[rs[0]] == 0 or student_money[rs[1]] == 0:
            times += 1
            continue
        if winner == 0:
            if student_money[rs[1]] >= lost_money:
                student_money[rs[0]] = student_money[rs[0]] + lost_money 
                student_money[rs[1]] = student_money[rs[1]] - lost_money
            else:
                student_money[rs[0]] = student_money[rs[0]] + student_money[rs[1]] 
                student_money[rs[1]] = 0
        if winner == 1:
            if student_money[rs[0]] >= lost_money:
                student_money[rs[1]] = student_money[rs[1]] + lost_money 
                student_money[rs[0]] = student_money[rs[0]] - lost_money
            else:
                student_money[rs[1]] = student_money[rs[1]] + student_money[rs[0]] 
                student_money[rs[1]] = 0        
if way == 'b': #方式b
    while times != 0:
        times = times - 1
        rs = random.sample(range(0,student),2)   #隨機挑兩位學生
        winner = random.randint(0,2)             #哪位獲勝     
        if winner == 0:
            student_money[rs[0]] = student_money[rs[0]] + lost_money 
            student_money[rs[1]] = student_money[rs[1]] - lost_money
        if winner == 1:
            student_money[rs[1]] = student_money[rs[1]] + lost_money 
            student_money[rs[0]] = student_money[rs[0]] - lost_money
                
print(student_money)   
bins = np.arange(min(student_money)-lost_money,max(student_money)+lost_money,lost_money)
plt.hist(student_money)
plt.show()


# In[ ]:




