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


sqlqueryvar= "CREATE TABLE Students (StudentID INT PRIMARY KEY,FirstName VARCHAR(50),LastName VARCHAR(50),Course VARCHAR(50),City VARCHAR(50))"



insertresult = sql_query(sqlqueryvar)
print(insertresult)

studentList = open("Python/Day4/Students.csv")

header = studentList.readline()
lines = studentList.readlines()
studentid = 0
town = 0
for line in lines:
    words = line.split(",")
    studentid = (words[0])
    sqlqueryvar= ("Insert into Student (StudentID,FirstName,LastName,Course,City) Values ("+ str(words[0]) + ",'" + str(words[1]) + "','" + str(words[2]) + "','"+ str(words[3]) +  "','" + str(words[4]) + "')")
    insertresult = sql_query(sqlqueryvar)
    print(insertresult)


sqlqueryvar= "Update Student set FirstName = 'Clare' where FirstName = 'Claire'"



insertresult = sql_query(sqlqueryvar)
print(insertresult)





def sqlselect_query(sqlvar):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=QAStore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    result = cur.execute(sqlvar).fetchall()
    cur.close()
    return result



sqlselectqueryvar = 'select * from Student'

resultvar = sqlselect_query(sqlselectqueryvar)

for row in resultvar:
    print(row)