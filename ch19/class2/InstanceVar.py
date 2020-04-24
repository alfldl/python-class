# 사용자 정의 클래스
class InstanceVar:
    def __init__(self):             # 생성자(인스턴스가 생성될 때 호출됨)
        self.text_list = []         # 리스트를 초기화 역할

    def add(self, text):            # 메소드
        self.text_list.append(text) # 리스트에 값을 추가하는 역할
    
    def print_list(self):           # 메소드
        print(self.text_list)       # 리스트를 출력하는 역할

if __name__ == '__main__':        
    a = InstanceVar()               # 인스턴스 생성
    a.add('a1')
    a.add('a2')
    a.print_list()                  # ['a'] 출력
    
    b = InstanceVar()               # 인스턴스 생성
    b.add('b')
    b.print_list()                  # ['b'] 출력