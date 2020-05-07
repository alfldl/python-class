# 함수를 변수에 담아서 사용하기


# 예1. 함수를 변수에 담아서 사용하기
def something(a):
    print(a)    
    
p=something         # 함수이름을 변수 p에 저장함

p(123)              # 변수 p를 이용해서 something()함수를 호출함 
p('abc')            # 변수 p를 이용해서 something()함수를 호출함 



# 예2. 함수를 변수에 담아서 사용하기
def plus(a,b):
    return a+b

def minus(a,b):
    return  a-b

first=[plus, minus]     #plus()함수와 minus()함수를 리스트의 요소로 할당함
print(first[0](1,2))    #first[0]은 plus()함수를 담고 있고, plus(1,2)를 호출함
print(first[1](1,2))    #first[1]은 minus()함수를 담고 있고, minus(1,2)를 호출함



# 예3. 함수를 매개변수로 사용하기
#     :파이썬에서는 함수를 매개변수로도 사용할 수 있고, 함수의 결과로 반환하는 것도 가능하다
def hello_korean():
    print('안녕하세요')
    
def hello_english():
    print('Hello')
    
def greet(hello):       # 함수를 매개변수로 전달할 함수
    hello()    
    
greet(hello_korean)
greet(hello_english)





