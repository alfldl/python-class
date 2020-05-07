# 일반 매개변수와  함께 사용하는 가변매개변수

# 함수 정의
def print_args(n, *args):   # 매개변수의 순서가 바뀌면 안됨
    for i in range(n):
        print(args[i])
        
        
# 함수 호출        
print_args(3, '파이썬', '자바', '오라클')
