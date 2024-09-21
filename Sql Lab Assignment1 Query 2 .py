#!/usr/bin/env python
# coding: utf-8

# In[21]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/cristinaortiz/Downloads/data.sqlite')


# In[23]:


q2 = """
SELECT customerName, state, country
FROM customers
WHERE customerName LIKE '%Collect%'
AND country != 'USA'
;
"""
q2_result = pd.read_sql(q2, conn)
q2_result


# In[ ]:




