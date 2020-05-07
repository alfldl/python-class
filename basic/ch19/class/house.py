class HousePark:
    lastname = "Park "
    def __init__(self, name):
        self.fullname=self.lastname+name
    def travel(self, where):
        print("%s %s 여행을 가네" % (self.fullname , where))
    def love(self, other):
        print("%s, %s 사랑 하네" % (self.fullname , other.fullname))
    def fight(self, other):
        print("%s, %s 전쟁 났네" % (self.fullname, other.fullname))
    def __add__(self, other):
         print("%s, %s 결혼 하네" % (self.fullname, other.fullname))
    def add3(self, a , b):
        k= a+b
        print("2덧셈 %d + %d  = %d 입니다" % ( a , b , k))
    def  __sub__(self, other):
        print("%s, %s 각방 쓰네" % (self.fullname , other.fullname))

class HouseKim(HousePark):
    lastname = "Kim "
    def travel(self, where, day):
        print("%s %s으로 여행 %d일 가네" % (self.fullname , where, day))
    # def add3(self, a , b, c):
    #     k= a+b+c
    #     print("3덧셈 %d + %d  +%d = %d 입니다" % ( a , b , c, k))
    def add3(self, a , b, c, d):
        k= a+b+c+d
        print("4덧셈 %d + %d  +%d  + %d= %d 입니다" % ( a , b , c, d,  k))

pey = HousePark("GiSun") # HousePark pey = new HousePark("GiSun");
julet=HouseKim('Eve')
pey.travel("정동진")
julet.travel("정동진", 3)
pey.love(julet)
pey+julet
#pey.add(julet)
pey.__add__(julet)
pey.add3(3,5)
#julet.add3(3, 5, 7)
julet.add3(3, 5, 7, 9)
pey.fight(julet)
pey-julet