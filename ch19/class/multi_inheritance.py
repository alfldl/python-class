# 클래스의 다중 상속
# : 2개 이상의 부모 클래스로 부터 상속 받는것을 의미함.
class Add:                          # 부모클래스
    def add(self, n1, n2):
        return n1 + n2

class Multiply:                     # 부모클래스
    def multiply(self, n1, n2):
        return n1 * n2

# 클래스의 다중상속 (Add, Multiply 클래스를 상속 받는다)
class Calculator(Add, Multiply):    # 자식클래스
    def sub(self, n1, n2):
        return n1 - n2

cal = Calculator()
print(cal.add(1, 2))                # 3이 출력됨
print(cal.multiply(3, 2))           # 6이 출력됨
