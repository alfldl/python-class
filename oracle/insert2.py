import cx_Oracle
import json
dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
con = cx_Oracle.connect("scott", "tiger", dsn)
cursor = con.cursor()

with open('C:\PyCharmProject\Sources\Basic\ch25\emp2.json' , encoding='UTF-8') \
        as data_file:
    data = json.load(data_file)
    for v in data:
        print("empno->",v['empno'],"ename->", v['ename'])
        cursor.execute("insert into emp2 values (:vempno , :vename) "
                       , vempno=v['empno'] , vename=v['ename'] )
con.commit()
con.close()
