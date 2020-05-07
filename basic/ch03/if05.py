# 3개의 정수를 입력받아서 큰 값과 작은 값을 구하는 프로그램 작성
n1 = int(input('정수n1 를 입력하세요?'))
n2 = int(input('정수n2 를 입력하세요?'))
n3 = int(input('정수n3 를 입력하세요?'))

if n1 >=n2 and n1>= n3:
    print(n1, '이 가장 큰 수입니다')
elif n2>=n1 and n2>= n3:
    print(n2, '이 가장 큰수입니다')
else:
    print(n3, '이 가장 큰수입니다')

if n1 <=n2 and n1<= n3:
    print(n1, '이 가장 작은 수입니다')
elif n2<=n1 and n2<= n3:
    print(n2, '이 가장 작은수입니다')
else:
    print(n3, '이 가장 작은 수입니다')
