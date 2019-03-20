#!/usr/bin/env python
# coding: utf-8

# In[1]:



employees = [{'id': '001','name': 'Mary','pay': 15.00,'hours': 40},
             {'id': '002','name': 'John','pay': 22.00,'hours': 25},
             {'id': '003','name': 'Bob','pay': 35.00,'hours': 4},
             {'id': '004','name': 'Mel','pay': 43.00,'hours': 62},
             {'id': '005','name': 'Jen','pay': 17.00,'hours': 33},
             {'id': '006','name': 'Sue','pay': 29.00,'hours': 45},
             {'id': '007','name': 'Ken','pay': 40.00,'hours': 36},
             {'id': '008','name': 'Dave','pay': 20.00,'hours': 17},
             {'id': '009','name': 'Beth','pay': 37.00,'hours': 37},
             {'id': '010','name': 'Ray','pay': 16.50,'hours': 80}]


# In[11]:


for employee in employees:
    if employee['hours'] <= 40:
        weekpay = employee['hours'] * employee['pay']
    else: 
        weekpay = (40 * employee['pay']) + ((employee['hours'] - 40) * 1.5 * employee['pay'])


# In[12]:


print(employee['name'], weekpay)


# In[ ]:




