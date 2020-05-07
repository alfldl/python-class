# continue문: 다시 반복문으로 돌아가라는 의미
for i in range(1,11):
    if i==5:
        continue
    print('출력=',i)

# continue문을 이용하여 1~100 까지의 짝수만 출력
for i in range(1,101):
    if i%2==1:
        continue
    print('짝수=',i)

# continue문을 이용하여 5의 배수만 출력
for i in range(1,101):
    if i%5!=0:
        continue
    print('5의 배수=',i)


