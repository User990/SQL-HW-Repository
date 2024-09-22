#!/usr/bin/env python
# coding: utf-8

# In[29]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/cristinaortiz/Downloads/data2 (1).sqlite')


# In[38]:


QUERY4 = """
SELECT DISTINCT
    employees.employeeNumber,
    employees.firstName,
    employees.lastName,
    offices.city,
    employees.officeCode
FROM employees
JOIN offices ON employees.officeCode = offices.officeCode
JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber
JOIN orders ON customers.customerNumber = orders.customerNumber
JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
WHERE orderdetails.productCode IN (
    SELECT productCode
    FROM orderdetails
    JOIN orders ON orderdetails.orderNumber = orders.orderNumber
    JOIN customers ON orders.customerNumber = customers.customerNumber
    GROUP BY productCode
    HAVING COUNT(DISTINCT customers.customerNumber) < 20
);
"""
QUERY4_result = pd.read_sql(QUERY4, conn)
QUERY4_result


# In[ ]:




