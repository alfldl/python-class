# 생성자
# 생성자는 객체가 생성될때 호출
# 생성자는 멤버변수를 초기화하는 역할.
class Animal(object):
    #  생성자 , 첫번째 parameter -> self는 예약어
    def __init__(self, name , age, is_hungry):
        # 생성자 내부에서 self로 받으면 자동으로 member 가 생성됨
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
        print(self.name , ' Animal 인스턴스 객체가 생성되었습니다')

    def descript(self):
        print(self.name , "method called")

jeffrey = Animal("Jeffrey", 2 , True)         #‘Animal 인스턴스 객체가 생성되었습니다’출력
bruce = Animal("Bruce",     5 , False)         #‘Animal 인스턴스 객체가 생성되었습니다’출력
trum = Animal("Trum",       7,  True)         #‘Animal 인스턴스 객체가 생성되었습니다’출력
print(jeffrey.name , jeffrey.age , jeffrey.is_hungry)          # Jeffrey 2 True 출력
print(bruce.name , bruce.age , bruce.is_hungry)          # Bruce 5 False 출력
print(trum.name , trum.age , trum.is_hungry)          # Trum 7 True 출력

jeffrey.descript()