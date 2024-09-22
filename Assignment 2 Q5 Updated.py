#!/usr/bin/env python
# coding: utf-8

# In[29]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/cristinaortiz/Downloads/data2 (1).sqlite')


# In[40]:


q5 = """
SELECT 
    employees.employeeNumber, 
    employees.firstName, 
    employees.lastName, 
    COUNT(customers.customerNumber) AS number_of_customers
FROM employees
JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber
GROUP BY employees.employeeNumber
HAVING AVG(customers.creditLimit) > 15000;
"""
q5_result = pd.read_sql(q5, conn)
q5_result


# In[ ]:




