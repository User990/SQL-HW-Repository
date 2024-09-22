#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/cristinaortiz/Downloads/data2.sqlite')


# In[16]:


q2 = """
SELECT
    products.productName,
    SUM(orderdetails.quantityOrdered) AS total_items_sold
FROM products
JOIN orderdetails ON products.productCode = orderdetails.productCode
GROUP BY products.productName
ORDER BY total_items_sold DESC;
"""
q2_result = pd.read_sql(q2, conn)
q2_result


# In[ ]:




