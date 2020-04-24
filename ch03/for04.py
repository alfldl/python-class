# 1부터 100까지 홀,짝수의 합을 구하는 프로그램 작성

odd=0; even=0
for i in range(1,101):
    if i % 2 == 1 :
        odd += i
    else:
        even +=i

print('1~100 까지의 홀수의 합=',odd)
print('1~100 까지의 짝수의 합=',even)
