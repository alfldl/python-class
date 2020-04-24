# 멤버 연산자 ( in )
# in : 컬렉션에 포함되어 있으면 True, 포함되어 있지 않으면 False
list = [1, 2, 3, 4]
ret1 = 5 in list            # False
ret2 = 4 in list            # True
print("ret1->", ret1); print("ret2->",ret2)

str = 'abcde'
ret3 = 'c' in str           # True
ret4 = '1' in str           # False
print("ret3->",ret3); print("ret4->",ret4)
