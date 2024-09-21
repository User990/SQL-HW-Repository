#!/usr/bin/env python
# coding: utf-8

# In[35]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/cristinaortiz/Downloads/data.sqlite')


# In[41]:


q6 = """
SELECT customers.customerName, customers.customerNumber, SUM(payments.amount) AS total_payment_amount
FROM customers
JOIN payments ON customers.customerNumber = payments.customerNumber
GROUP BY customers.customerNumber
ORDER BY total_payment_amount DESC
LIMIT 10;
"""
q6_result = pd.read_sql(q6, conn)
q6_result


# In[43]:


# Run this cell without changes

# Testing which columns are returned
assert list(q6_result.columns) == ['customerName', 'customerNumber', 'total_payment_amount']

# Testing how many rows are returned
assert len(q6_result) == 10

# Testing the values in the first result
assert list(q6_result.iloc[0]) == ['Euro+ Shopping Channel', 141, 715738.98]


# In[ ]:




