# 문자열 정렬하기 (sorted() 함수 )
# sorted() 함수 : 특정 변수에 저장된 값을 오름차순 정렬해주는 함수 ( 1,2,3... 사전순 정렬)
strdata = input('정렬할 문자열을 입력하세요? ')
ret1 = sorted(strdata)                  # 오름차순 정렬 (ex. a b c ...)
ret2 = sorted(strdata, reverse=True)    # 내림차순 정렬 (ex. z y x ...)
print(ret1)
print(ret2)

ret1 = ''.join(ret1)
ret2 = ' '.join(ret2)
print('오름차순으로 정렬된 문자열은 <' + ret1 + '> 입니다.')
print('내림차순으로 정렬된 문자열은 <' + ret2 + '> 입니다.')

