class Person:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone
    def __str__(self):
        return '<Person %s %s>' % (self.name, self.phone)


class Employee(Person):  # 괄호 안에 쓰여진 클래스는 슈퍼클래스를 의미한다.
    def __init__(self, name, phone, position, salary):
        Person.__init__(self, name, phone)  # Person클래스의 생성자 호출
        self.position = position
        self.salary = salary


p1 = Person('서동범', 1498)
print("p1.name->", p1.name)

m1 = Employee('이윤영', 5564, '대리', 200)
m2 = Employee('정재연', 8546, '과장', 300)
print("m1.name, m1.position->", m1.name, m1.position)  # 슈퍼클래스와 서브클래스의 멤버를 하나씩 출력한다.
print("m1->", m1)
print("m2.name, m2.position->", m2.name, m2.position)
print("m2->", m2)