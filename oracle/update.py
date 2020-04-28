import cx_Oracle

dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
con = cx_Oracle.connect("scott", "tiger", dsn)
cursor = con.cursor()

cursor.execute("update dept set loc='busan3' where deptno = 40")

con.commit()
con.close()




