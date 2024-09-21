#!/usr/bin/env python
# coding: utf-8

# In[35]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/cristinaortiz/Downloads/data.sqlite')


# In[39]:


q5 = """
SELECT customers.customerName, orders.orderNumber, orders.status
FROM customers
JOIN orders ON customers.customerNumber = orders.customerNumber
LIMIT 15;
"""
q5_result = pd.read_sql(q5, conn)
q5_result.head(15)


# In[ ]:




