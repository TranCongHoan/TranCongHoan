#!/usr/bin/env python
# coding: utf-8

# In[6]:


time = int(input('Nhập số phút đã sử dụng : '))
if time >= 200 : 
    sum = 50*600 + 150*400 + (time - 200)*200
    print('số tiền phải thanh toán là: ', sum , 'vnd')
elif time > 50 and time < 200 :
    sum = 50*600 + (time - 50)*400
    print('số tiền phải thanh toán là: ', sum , 'vnd')
elif time <= 50 and time > (25000/600) :
    sum = time*600
    print('số tiền phải thanh toán là: ', sum , 'vnd')
else :
    print('số tiền phải thanh toán là 25000 vnd')


# In[ ]:





# In[ ]:




