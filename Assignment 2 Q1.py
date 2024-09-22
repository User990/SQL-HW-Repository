#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/cristinaortiz/Downloads/data2.sqlite')


# In[11]:


q = """
SELECT
    customerNumber,
    contactLastName,
    contactFirstName
FROM customers
WHERE customerNumber IN (
    SELECT customerNumber
    FROM orders
    WHERE orderDate = '2003-01-31'
);
"""
result = pd.read_sql(q, conn)
result


# In[ ]:




