from xml.dom.minidom import Identified
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


sqlqueryvar= ""

"Create Table boats ( Boat_ID INT Primary Key Identity(1,1),Make VARCHAR(255),Model VARCHAR(255),Year INT,Owner VARCHAR(255),Spectification VARCHAR(255),Engine_Make VARCHAR(255) Null,Engine_Size INT Null,Boat_Club_Member BIT)


"Insert into boats (Boat_ID,Make,Model,Year,Owner,Spectification,Engine_Make,Engine_Size,Boat_Club_Member) Values ('HonWave', 'Honda', 'T38', 2021,'Claire Fitzjohn','Blue and White Rib','Honda',20,True")


insertresult = sql_query(sqlqueryvar)
print(insertresult)




sqlqueryvar= "Insert into salesperson (emp_no,first_name,last_name,dept_no,salary,sales_target,county,post_code,tel,notes) Values (0121,'Claire','Fitzjohn',3,100000,50,'Kent','CT012AB',0123456789,'New Record updated by claire')"
