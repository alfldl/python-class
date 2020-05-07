import cx_Oracle

dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
con = cx_Oracle.connect("scott", "tiger", dsn)
cursor = con.cursor()

vdeptno = input('부서번호 입력 : ')
vdname = input('부서명 입력 : ')
vloc = input('위치 입력 : ')

cursor.execute("insert into dept values(:deptno , :dname , :loc)",
                 deptno=vdeptno,  dname=vdname,  loc=vloc )

con.commit()
con.close()









