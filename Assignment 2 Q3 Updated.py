#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/cristinaortiz/Downloads/data2.sqlite')


# In[22]:


q3 = """
SELECT
    products.productName,
    COUNT(DISTINCT orders.customerNumber) AS total_customers
FROM products
JOIN orderdetails ON products.productCode = orderdetails.productCode
JOIN orders ON orderdetails.orderNumber = orders.orderNumber
WHERE orders.customerNumber IS NOT NULL
AND products.productCode IS NOT NULL
GROUP BY products.productName
ORDER BY total_customers DESC;
"""
q3_result = pd.read_sql(q3, conn)
q3_result


# In[ ]:




