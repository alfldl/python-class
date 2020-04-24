# 사용자정의 클래스

class ClassVar:                         # 클래스
    text_list = []                      # 클래스멤버변수

    def add(self, text):                # 메소드
        self.text_list.append(text)
    
    def print_list(self):               # 메소드
        print(self.text_list)

if __name__ == '__main__':        
    a = ClassVar()
    a.add('a')
    a.print_list()                      # ['a'] 출력
    
    b = ClassVar()
    b.add('b')
    b.print_list()                      # ['a', 'b'] 출력