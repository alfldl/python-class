# 문자열 포맷팅
# 문자열에서 변하는 값을 나타내는 포맷 문자열은 % 기호를 사용함

#  포맷문자열            설명
#  --------------------------------------------------
#      %s                문자열
#      %c                문자나 기호 한개
#      %d                정수
#      %f                실수
#      %%                '%' 라는 기호 자체를 표시함

txt1 = '자바';  txt2='파이썬'
num1= 5;  num2=10

print('나는 %s보다 %s에 더 익숙합니다.' %(txt1, txt2))
print('%s은 %s보다 %d배 더 쉽습니다.' %(txt2, txt1, num1))
print('%d + %d = %d' %(num1, num2, num1+num2))
print('작년 세계 경제 성장률은 전년에 비해 %d %% 포인트 증가했다.' %num1)