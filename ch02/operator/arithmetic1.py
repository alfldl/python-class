# 산술 연산자
a = 2
b = 4
ret1 = a + b
ret2 = a - b
ret3 = a * b
ret4 = a / b                    # a 나누기 b의 몫을 구함 (실수형)
ret5 = a ** b                   # 승
ret6 = a + a * b / a            # 6.0 출력
ret7 = (a + b) * (a - b)        # () 우선순위 최우선
ret8 = a * b ** a               # ** : 거듭제곱을 구함 (4의 2승)     32 출력

print("a + b=", ret1)
print("a - b=", ret2)
print("a * b=", ret3)
print("a / b=", ret4)
print("a ** b=", ret5)
print("a + a * b / a=", ret6)
print("(a + b) * (a - b)=", ret7)
print("a * b ** a=", ret8)
