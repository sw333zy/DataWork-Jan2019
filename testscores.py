#!/usr/bin/env python
# coding: utf-8

# In[1]:


#excel library import
import xlwt 
from xlwt import Workbook 
  
#make workbook
wb = Workbook() 
  
# create worksheet object with add_sheet
sheet = wb.add_sheet('testscores') 
  
#information for sheet (x,y)
sheet.write(0, 0, 'NAME') 
sheet.write(1, 0, 'SEX') 
sheet.write(2, 0, 'AGE') 
sheet.write(3, 0, 'SCORE') 
sheet.write(0, 1, 'RYAN') 
sheet.write(0, 2, 'FEMALE') 
sheet.write(0, 3, '16') 
sheet.write(0, 4, '99') 

#save sheet  
wb.save('xlwt testscores.xls') 


# In[ ]:




