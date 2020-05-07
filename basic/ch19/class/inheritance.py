# 클래스의 상속
class Add:                      # 부모클래스, 슈퍼클래스
    def add(self, n1, n2):      # 부모클래스의 메소드는 상속됨
        return n1 + n2

#  Calculator(Add) -> class Add 상속
class Calculator(Add):          # 자식클래스, 서브클래스
    def sub(self, n1, n2):
        return n1 - n2

obj = Calculator()
print(obj.add(1, 2))            # 3이 출력됨
print(obj.sub(1, 2))            # -1이 출력됨

#obj2 = Add()
#print(obj2.sub(1, 2))            # -1이 출력됨

