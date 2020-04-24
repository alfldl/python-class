# 사용자 정의 클래스

class Animal:
    name = 'dog'        # 멤버변수
    age = 5

a1 = Animal()           # 인스턴스 생성
print(a1.name)
print(a1.age)

a1.name='원숭이'
a1.age=10
print(a1.name)
print(a1.age)