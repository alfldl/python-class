# 구구단 2~ 9단을 출력하는 프로그램 작성
dan=0
for dan in range(2,10):                     # 단 (2 ~ 9)
    print('[',dan,'단]')
    for i in range(1,10):                   # 1 ~ 9
        print(dan, '*' , i, '=', dan*i)
    print()
