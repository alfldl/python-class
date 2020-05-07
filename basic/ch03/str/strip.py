# 문자열 좌.우  좌우공백 제거하기 ( lstrip(), rstrip(), strip() 함수 )
# lstrip() : 문자열 좌측의 공백을 없애주는 함수
# rstrip() : 문자열 우측의 공백을 없애주는 함수
# strip() : 문자열 좌.우의 공백을 없애주는 함수

txt = '   양쪽에 공백이 있는 문자열입니다.   '
ret1 = txt.lstrip()
ret2 = txt.rstrip()
ret3 = txt.strip()

print('<'+txt+'>')
print('<'+ret1+'>')     #왼쪽 공백 제거
print('<'+ret2+'>')     #오른쪽 공백 제거
print('<'+ret3+'>')     #좌우 공백 제거
