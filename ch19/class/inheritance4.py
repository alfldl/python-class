class Animal:  # Animal에 있는 cry를 Dog의 cry가 override 함
    def cry(self):
        print('...')

class Dog(Animal):
    def cry(self):
        print('멍멍')

class Duck(Animal):
    def cry(self):
        print('꽥꽥')

class Fish(Animal):  # Fish는 cry가 없으므로 Animal의 내용을 그대로 사용
    pass

# in 뒤에는 튜플 안에 객체 3개 존재 -> each의 객체 형이 동적으로 결정되므로 그때마다의 cry가 다르게 사용
for each in (Dog(), Duck(), Fish()):
    each.cry()
