# 문자열에서 특정 문자 위치 찾기 ( find() 함수 )
# find() 함수는 특정문자의 index번호를 리턴한다.

txt = 'A lot of things occur each day, every day.'
offset5 = txt.find('A')             # 가장먼저 나오는 'A' 의 index번호를 리턴함
offset1 = txt.find('e')             # 가장먼저 나오는 'e' 의 index번호를 리턴함
offset2 = txt.find('day')           # 가장먼저 나오는 'day' 의 index번호를 리턴함
offset3 = txt.find('day', 30)       # index번호 30번 이후에 나오는 day의 index번호를 리턴함

print(offset5)   # 22가 출력됨
print(offset1)   # 22가 출력됨
print(offset2)   # 27이 출력됨
print(offset3)   # 38이 출력됨
