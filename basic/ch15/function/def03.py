# 최대값, 최소값 구하기
# 최대값을 구해주는 함수
def max(n1, n2):
    if(n1 > n2):
        return n1
    else:
        return n2
 
# 최소값을 구해주는 함수
def min(n1, n2):
    if(n1 > n2):
        return n2
    else:
        return n1  
    
print('2개의 정수를 입력 하세요?')
n1 = input("첫번째")
n2 = input("두번째")

nn1= int(n1)
nn2= int(n2)

max = max(nn1, nn2)
min = min(nn1, nn2)

print('max=', max)  
print('min=', min)  
    
