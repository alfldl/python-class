# 멤버변수와 인스턴스 멤버변수
# 클래스에서 선언되는 변수는 멤버변수와 인스턴스 멤버변수가 있다.
# 1. 멤버변수: 메소드 바깥쪽에서 선언된 변수
# 2. 인스턴스 멤버변수 : 메소드 안에서 선언된 변수
#                       메소드 안에서만 사용가능한 지역변수
class MyClass:
    var = '안녕하세요!!'              # 멤버변수

    def sayHello(self):
        param1 = '안녕'               # 인스턴스 멤버변수
        print(param1)                 # '안녕’출력
        print(self.var)               # '안녕하세요’출력


obj = MyClass()
print(obj.var)                        # ‘안녕하세요’출력
#print(obj.param1)                        # ‘안녕하세요’출력
obj.sayHello()
print("MyClass().var->", MyClass().var)
