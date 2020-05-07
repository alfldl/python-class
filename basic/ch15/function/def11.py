# 재귀함수(Recursive Function)
# : 함수가 자기자신을 호출하는 함수를 재귀함수라 한다.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)   
    
    
print('3!=', factorial(3))    

print('5!=', factorial(5)) 

print('10!=', factorial(10)) 

print('983!=', factorial(983)) 

   
        
