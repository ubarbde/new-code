#!/usr/bin/env python
# coding: utf-8

# In[19]:


#1.1
def divide():
    return 5/0
try:
    divide()
except ZeroDivisionError as ZDE:
    print("this is ujwal")
except:
    print("except ujwal")


# In[31]:


#1.2
subjects=["Americans ","Indians "]
verbs=["play ","watch "]
objects=["Baseball","Cricket"]
for s in subjects:
    for v in verbs:
        for o in objects:
            total_sentence = s+v+o
            print(total_sentence)


# In[ ]:




