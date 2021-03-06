print ("------------------------------------------------------------------------------------")
print ("--- 람다(lambda) 함수 정의  ->   1. 람다 함수 정의 예                                  --")
print ("--- 1] 일반적인 함수를 한 줄의 문(Statement)으로 정의할 수 있는 새로운 함수 정의 리터럴     --")
print ("--- . 함수 몸체에는 식(expression)만이 올 수 있다.                                     --")
print ("--- . 대부분의 경우 함수 이름을 정의하지 않으면서 일회성으로 활용할 함수를 정의할 때    활용  --")
print ("--- . 구문(syntax)-> ◦lambda 콤마로 구분된 인수들: 식(expression)                     --")
print ("------------------------------------------------------------------------------------")
print
# lamda x: x + 1 → 하나의 statement, 콜론(:) 뒤에는 expression(식)만 올 수 있음
# f 식별자로 람다함수를 가리키게 할 수 있음 → 람다함수도 하나의 객체
f = lambda x: x + 1
print ("f->", f(1))