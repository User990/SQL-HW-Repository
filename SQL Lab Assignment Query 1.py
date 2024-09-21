#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/cristinaortiz/Downloads/data.sqlite')


# In[3]:


q0 = """
SELECT productline
FROM productlines
;
"""

pd.read_sql(q0, conn)


# In[5]:


q1 = """
SELECT contactFirstName, contactLastName, phone, addressLine1, creditLimit
FROM customers
WHERE state = 'CA' AND creditLimit > 25000
;
"""

pd.read_sql(q1,conn)


# In[7]:


q1 = """
SELECT contactFirstName, contactLastName, phone, addressLine1, creditLimit
FROM customers
WHERE state = 'CA' AND creditLimit > 25000
;
"""
q1_result = pd.read_sql(q1, conn)
q1_result


# In[16]:


# Testing which columns are returned
assert list(q1_result.columns) == ['contactFirstName', 'contactLastName', 'phone', 'addressLine1', 'creditLimit']

# Testing how many rows are returned
assert len(q1_result) == 10

# Testing the values in the first result
assert list(q1_result.iloc[0]) == ['Susan', 'Nelson', '4155551450', '5677 Strong St.', 210500]


# In[18]:




