# 문자열이 숫자인지 검사하기 ( isdigit() 함수 )
# isdigit() 함수는 문자열을 구성하는 요소가 모두 숫자이면 True,
# 문자가 포함되어 있으면 False를 리턴한다.

txt1 = '010-1234-5678'
txt2 = 'R2D2'
txt3 = '1212'

ret1 = txt1.isdigit()
ret2 = txt2.isdigit()
ret3 = txt3.isdigit()

print(ret1)      # False가 출력됨  ( 하이픈 '-'  포함)
print(ret2)      # False가 출력됨  ( 알파벳 포함)
print(ret3)      # True가 출력됨
