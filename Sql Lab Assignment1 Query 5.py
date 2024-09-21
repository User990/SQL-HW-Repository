#!/usr/bin/env python
# coding: utf-8

# In[35]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/cristinaortiz/Downloads/data.sqlite')


# In[37]:


q4 = """
SELECT state, AVG(creditLimit) AS average_credit_limit
FROM customers
WHERE country = 'USA'
GROUP BY state
;
"""
q4_result = pd.read_sql(q4, conn)
q4_result


# In[ ]:




