# 논리 연산자
# 논리 연산자       의미
#   A and B         A와 B가 모두 참이면 참
#   A or B          A, B중 하나 이사이 참이면 참
#   not A           A 논리값의 반대
bool1 = True; bool2 = False; bool3 = True; bool4 = False
print(bool1 and bool2)    # False가 출력됨
print(bool1 and bool3)    # True가 출력됨
print(bool2 or bool3)     # True가 출력됨
print(bool2 or bool4)     # False가 출력됨
print(not bool1)          # False가 출력됨
print(not bool2)          # True가 출력됨
