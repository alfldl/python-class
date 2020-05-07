# 정적 메소드
# 정적 메소드는 공유를 목적으로 하는 경우에 주로 사용하며,
# 인스턴스를 생성하지 않고, 클래스명.정적메소드를 직접 호출한다.
class Calculator:
    @staticmethod
    def plus(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


if __name__ == '__main__':
    print("{0} + {1} = {2}".format(7, 4, Calculator.plus(7, 4)))
    print("{0} - {1} = {2}".format(7, 4, Calculator.minus(7, 4)))
    print("{0} * {1} = {2}".format(7, 4, Calculator.multiply(7, 4)))
    print("{0} / {1} = {2}".format(7, 4, Calculator.divide(7, 4)))
