# 문자열을 수치형 자료로 변환하기 ( int(), float() 함수 )
# int() : 문자를 정수형으로 형변환
# float() : 문자를 실수형으로 형변환
numstr = input('숫자를 입력하세요? ')
#예외처리: 프로그램이 비정상적으로 종료되는 것을 막기 위해서 사용
'''
 try:
         예외가 발생할 가능성이 있는 문장
 except:
         예외처리 메세지
'''
try:
   num = int(numstr)
   print('당신이 입력한 숫자는 정수 %d입니다.' %num)
except:
   print('첫번째 expect...' )
   try:
      num = float(numstr)
      print('당신이 입력한 숫자는 실수 %f입니다.' %num)
   except:
      print('+++ 숫자를 입력하세요~ +++')
