#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = int(input('nhập số a: '))
b = int(input('nhập số b: '))
c = int(input('nhập số c: '))
if a*a == b*b + c*c or a*a + b*b == c*c or a*a + c*c == b*b :
    print('3 số', a, b, c, 'là bộ 3 số pitago')
else :
    print('3 số', a, b, c, 'không phải 3 số pỉago')


# In[ ]:




