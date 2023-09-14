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


sqlqueryvar= "Insert into salesperson (emp_no,first_name,last_name,dept_no,salary,sales_target,county,post_code,tel,notes) Values (0121,'Claire','Fitzjohn',3,100000,50,'Kent','CT012AB',0123456789,'New Record updated by claire')"



insertresult = sql_query(sqlqueryvar)
print(insertresult)




