# Tuple은 List의 Read Only
# range : List나 Tuple를 사용, 저장하지 않더라도 특정범위의
#          숫자 시퀀스 생성
# range(start,stop,step)
L = range(10)  # 0,1,2,3,4,5,6,7,8,9

print (L)
print ("L[::2]->",L[::2])  # start : end : jump
A = L[::2]
for  aa in A:
    print('A->',aa)

t = (1,2,3)
print ("len(t)->" , len(t))

print ("t[0]->", t[0])
print (t[-1])
print (" t[0:2] ->" , t[0:2])
print ("t[::2]->" , t[::2])

print ("t + t + t ->" , t + t + t)
print (t * 3)
print ("L->", L)
# t[1] = 7  # -> 오류 발생


print (3 in t)