# 사용자 정의 클래스

class ContactInfo:                          # 클래스
    def __init__(self, name, email):        # 생성자
        self.name = name
        self.email = email

    def print_info(self):                   # 메소드
        print('{0} : {1}'.format(self.name, self.email))

if __name__ == '__main__':                  # 객체 생성
    ahn = ContactInfo('ktg', 'giduck23@gmail.com')
    ca = ContactInfo('choongang', 'webmaster@choongang.co.kr')
    
    ahn.print_info()                        # print_info() 메소드 호출 
    ca.print_info()