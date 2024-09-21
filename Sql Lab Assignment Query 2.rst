.. code:: ipython3

    import sqlite3
    import pandas as pd
    
    conn = sqlite3.connect('/Users/cristinaortiz/Downloads/data.sqlite')

.. code:: ipython3

    q2 = """
    SELECT customerName, state, country
    FROM customers
    WHERE customerName LIKE '%Collect%'
    AND country != 'USA'
    ;
    """
    q2_result = pd.read_sql(q2, conn)
    q2_result




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>customerName</th>
          <th>state</th>
          <th>country</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Australian Collectors, Co.</td>
          <td>Victoria</td>
          <td>Australia</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Clover Collections, Co.</td>
          <td>None</td>
          <td>Ireland</td>
        </tr>
        <tr>
          <th>2</th>
          <td>UK Collectables, Ltd.</td>
          <td>None</td>
          <td>UK</td>
        </tr>
        <tr>
          <th>3</th>
          <td>King Kong Collectables, Co.</td>
          <td>None</td>
          <td>Hong Kong</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Heintze Collectables</td>
          <td>None</td>
          <td>Denmark</td>
        </tr>
        <tr>
          <th>5</th>
          <td>Royal Canadian Collectables, Ltd.</td>
          <td>BC</td>
          <td>Canada</td>
        </tr>
        <tr>
          <th>6</th>
          <td>BG&amp;E Collectables</td>
          <td>None</td>
          <td>Switzerland</td>
        </tr>
        <tr>
          <th>7</th>
          <td>Reims Collectables</td>
          <td>None</td>
          <td>France</td>
        </tr>
        <tr>
          <th>8</th>
          <td>Precious Collectables</td>
          <td>None</td>
          <td>Switzerland</td>
        </tr>
        <tr>
          <th>9</th>
          <td>Salzburg Collectables</td>
          <td>None</td>
          <td>Austria</td>
        </tr>
        <tr>
          <th>10</th>
          <td>Tokyo Collectables, Ltd</td>
          <td>Tokyo</td>
          <td>Japan</td>
        </tr>
        <tr>
          <th>11</th>
          <td>Stuttgart Collectable Exchange</td>
          <td>None</td>
          <td>Germany</td>
        </tr>
        <tr>
          <th>12</th>
          <td>Bavarian Collectables Imports, Co.</td>
          <td>None</td>
          <td>Germany</td>
        </tr>
        <tr>
          <th>13</th>
          <td>Australian Collectables, Ltd</td>
          <td>Victoria</td>
          <td>Australia</td>
        </tr>
        <tr>
          <th>14</th>
          <td>Kremlin Collectables, Co.</td>
          <td>None</td>
          <td>Russia</td>
        </tr>
      </tbody>
    </table>
    </div>



