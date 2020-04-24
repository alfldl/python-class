# 키보드로 입력한 점수(0 ~ 100)가 어느 학점에 해당하는지 구하는 프로그램
# 90~ A학점
# 80~ B학점
# 70~ C학점
# 60~ D학점
# 60점 미만 F학점
n = int(input('정수n 를 입력하세요?'))

if n > 100:
    print('점수를 확인하세요')
elif n >= 90:
        print(' A학점입니다')
elif n >= 80 :
    print('B학점입니다')
elif n >= 70 :
    print('C학점입니다')
elif n >= 60:
    print('D학점입니다')
else :
    print('F학점입니다')
