import cx_Oracle
import json

dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
con = cx_Oracle.connect("scott", "tiger", dsn)
cursor = con.cursor()

cursor.execute("""SELECT * FROM dept""")
# row = cursor.fetchall()
# print(row)

for deptno, dname, loc in cursor:
    print("dept->", deptno, dname, loc)
    print( "{'deptno':'%s', 'dname':'%s', 'loc':'%s'}"
           % (deptno, dname, loc ))

con.close()














