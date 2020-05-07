# 1~n 까지 합을 구하는 프로그램
# 1~n까지 합을 구해주는 함수
def sum(n):
    sum = 0
    for i in range(1, n + 1):  # 1~n까지 loop가 돌아감
        sum = sum + i
        
    print('1 ~', n, '=', sum)

# 함수 호출
sum(5)
sum(10)
sum(30)
sum(100)
