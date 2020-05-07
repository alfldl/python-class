# 생성자
# 생성자는 객체가 생성될때 호출된다.
# 생성자는 멤버변수를 초기화하는 역할을 한다.


class Animal:
    #  생성자 , 첫번째 parameter -> self는 예약어
    def __init__(self):
        self.var = '안녕하세요!'
        print('Animal 인스턴스 객체가 생성되었습니다')


cat = Animal()         #‘Animal 인스턴스 객체가 생성되었습니다’출력
print(cat.var)          # '안녕하세요’출력
print(type(cat))          # '안녕하세요’출력
