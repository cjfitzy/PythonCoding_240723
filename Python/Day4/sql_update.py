import pyodbc

def sql_query(sqlvar):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=QAStore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    try:
        result = cur.execute(sqlvar)
    except Exception as e:
        print(e)
        result = None
    conn.commit()
    cur.close()
    return result


sqlqueryvar= "Update [salesperson] set first_name = 'Clare' where first_name = 'Claire'"



insertresult = sql_query(sqlqueryvar)
print(insertresult)




