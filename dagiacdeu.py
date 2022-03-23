#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle

tl = turtle.Turtle()
tl.penup()
tl.goto(-100,-150)


tl.fillcolor('yellow')
tl.pendown()

tl.begin_fill()
for i in range (10):
    tl.forward(144)
    tl.left(36)
tl.end_fill()

turtle.done()


# In[ ]:





# In[ ]:




