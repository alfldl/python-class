# 자원 해제 다른 프로그램이 접근 할수 있도록  With 문 끝날때 자동
with open('test.txt','r' ,  encoding='UTF8') as file:
    str = file.readlines()
    for s in str:
        print(s)
        #print(s, end='')

