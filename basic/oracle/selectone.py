import cx_Oracle

# dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
# dsn = cx_Oracle.makedsn("127.0.0.1", 1521, "xe")
dsn = cx_Oracle.makedsn("211.183.2.21", 1521, "xe")
con = cx_Oracle.connect("scott", "tiger", dsn)
cursor = con.cursor()

vdeptno = input('부서번호 입력 : ')

cursor.execute("""SELECT * FROM dept where deptno = :deptno """, deptno=vdeptno)
row = cursor.fetchone()

print(row)

con.close()











