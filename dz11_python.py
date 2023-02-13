#!/usr/bin/env python
# coding: utf-8

# In[ ]:


f(x) = -12*x**4*sin(cos(x)) - 18*x***3+5*x**2 + 10*x - 30

Определить корни
Найти интервалы, на которых функция возрастает
Найти интервалы, на которых функция убывает
Построить график
Вычислить вершину
Определить промежутки, на котором f > 0
Определить промежутки, на котором f < 0


# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[182]:


limit = 10
step = 0.01
color = 'b'
liner_s = '-'
direct_up = True


# In[183]:


x = np.arange(-limit, limit, step)


# In[184]:


a, b, c, d, e = -12, -18, 5, 10, -30


# In[185]:


def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color


# In[186]:


def switch_line():
    global liner_s
    if liner_s == '-':
        liner_s = '--'
    else:
        liner_s = '-'
    return liner_s


# In[187]:


def func(x):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 +d*x+e


# In[188]:


x_change = [(-limit, 'limit')]
for i in range(len(x)-1):
    if(func(x[i]) > 0 and func(x[i+1]) < 0) or (func(x[i]) < 0 and func(x[i+1])>0):
         x_change.append((x[i] if abs(0-x[i]) < abs(0-x[i+1]) else x[i+1], 'zero'))
    if direct_up:
        if func(x[i]) > func(x[i+1]):
            x_change.append((x[i], 'direct'))
            direct_up = False
    else:
        if func(x[i]) < func(x[i+1]):
            x_change.append((x[i], 'direct'))
            direct_up = True
x_change.append((limit, 'limit'))
print (x_change)


# In[189]:


for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i+1][0]+step, step)
    if x_change[i][1] =='zero':   
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    
    else:
       # plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), switch_color())
        
roots = []        
for  x in x_change:
    if x[1] == 'zero':
        roots.append(str(round(x[0], 2)))
        plt.plot(x[0], func(x[0]), 'gx')
        
plt.rcParams['lines.linestyle'] = '-'
plt.plot(0, 0, 'b', label='Убывание > 0')
plt.plot(0, 0, 'r', label='Возрастание > 0')
plt.rcParams['lines.linestyle'] = '--'
plt.plot(0, 0, 'b', label='Убывание < 0')
plt.plot(0, 0, 'r', label='Возрастание < 0')
plt.title(f'Корни на промежутке [{-limit}:{limit}]: {",".join(roots)}')
plt.legend()
plt.grid()


# In[ ]:





# In[22]:


plt.plot(x, func(x), 'r')
plt.grid()


# In[ ]:





# In[ ]:





# In[ ]:




