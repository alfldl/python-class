import cx_Oracle
import json
import ast

dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
con = cx_Oracle.connect("scott", "tiger", dsn)
cursor = con.cursor()
cursor.execute("""SELECT * FROM emp2 order by empno""")

i = 0
with open('C:\PyCharmProject\Sources\Basic\ch25\emp3.json', 'w', encoding="utf-8") \
        as make_file:
    text ="["
    for empno, ename in cursor:
        if i == 0:
            text1 = "{'empno':'%s', 'ename':'%s'}" % (empno, ename )
        else:  # 두번째 라인부터는 , 첨가
            text1 = ",{'empno':'%s', 'ename':'%s'}" % (empno, ename )
        text = text +  text1
        i = i + 1
        # print ("text->", text)
    text = text + "]"
    print("text->", text)
    empDict = ast.literal_eval(text)   # text를 Dictionary로 생성
    # Dictionary를 json 자료로 만들어 줌
    json.dump(empDict, make_file, ensure_ascii=False, indent="\t")
    print("empDict->",empDict)
con.close()


