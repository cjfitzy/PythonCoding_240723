import pyodbc




def qassql_query(sqlvar):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=QAStore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    result = cur.execute(sqlvar).fetchall()
    cur.close()
    return result



sqlqueryvar = 'select sp.first_name, sp.last_name, sp.salary, sp.sales_target, s.order_no, s.order_value, s.order_date from  [salesperson] sp   inner join [sale] s  on sp.emp_no = s.emp_no order by sp.first_name, sp.last_name, s.order_date, s.order_value desc'

resultvar = qassql_query(sqlqueryvar)

for row in resultvar:
    print(row)


def northwindsql_query(sqlvar):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=Northwind;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    result = cur.execute(sqlvar).fetchall()
    cur.close()
    return result



sqlqueryvar = 'select top 10 o.OrderID,o.ProductID,p.ProductName,o.UnitPrice,o.Quantity,p.QuantityPerUnit from [Order Details] o  inner join [Products] p   on o.ProductID = p.ProductID  order by o.OrderID desc'

resultvar = northwindsql_query(sqlqueryvar)

for row in resultvar:
    print(row)



    
