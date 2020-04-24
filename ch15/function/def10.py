#지역변수와 전역변수

#1.변수는 자신이 생성된 범위(코드블록) 안에서만 유효
#2.함수 안에서 만든 변수는 함수 안에서만 살아있다가 함수 코드의 실행이 종료되면 그 생명이 다함  
#  이것을 지역변수(Local Variable)라고 함
#  이와는 반대로 함수 외부에서 만든 변수는 프로그램이 살아있는 동안에는 함께 살아있다가 프로그램이 종료될 때 같이 소멸됨.
#이렇게 프로그램 전체를 유효 범위로 가지는 변수를 전역 변수(Global Variable) 라 함.
#3.파이썬은 함수 안에서 사용되는 모든 변수를 지역변수로 간주
#4.전역 변수를 사용하기 위해서는 global 키워드를 이용


def scope():
    global a            # 전역변수
    a=1
    print('2. a=',a)   # a=1 출력됨
    
 
a=10                    # 지역변수 a=10을 정의함
print('1. a=',a)       # a=10 출력됨(지역변수가 출력됨)
scope()
print('3. a=',a)       # a=1 출력됨(전역변수가 출력됨)