#!/usr/bin/env python
# coding: utf-8

# In[35]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/cristinaortiz/Downloads/data.sqlite')


# In[45]:


q7 = """
SELECT customers.customerName, customers.customerNumber, products.productName, orderdetails.productCode, SUM(orderdetails.quantityOrdered) AS total_ordered
FROM customers
JOIN orders ON customers.customerNumber = orders.customerNumber
JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
JOIN products ON orderdetails.productCode = products.productCode
GROUP BY customers.customerNumber, products.productCode
HAVING total_ordered >= 10
ORDER BY total_ordered ASC;
"""
q7_result = pd.read_sql(q7, conn)
q7_result


# In[47]:


# Run this cell without changes

# Testing which columns are returned
assert list(q7_result.columns) == ['customerName', 'customerNumber', 'productName', 'productCode', 'total_ordered']

# Testing how many rows are returned
assert len(q7_result) == 2531

# Testing the values in the first result
assert list(q7_result.iloc[0]) == ['Petit Auto', 314, '1913 Ford Model T Speedster', 'S18_2949', 10]


# In[ ]:




