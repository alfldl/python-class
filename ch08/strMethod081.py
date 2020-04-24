print ("---------------------------")
print ("------  문자열 메소드  ------")
s = 'i like programming.'
print ("s.upper()                      " , s.upper())
print ("s.upper().lower()              " , s.upper().lower())
print ("'I Like Programming'.swapcase()" , 'I Like Programming'.swapcase()) # 대문자는 소문자로, 소문자는 대문자로 변환
print ("s.capitalize(                  " , s.capitalize()) # 첫 문자를 대문자로 변환
print ("s.title()                    "   , s.title() )   # 각 단어의 첫 문자를 대문자로 변환

s1 = 'i like programming, i like swimming.'
print ("s1                     " , s1)
print ("s1.count('like')       " , s1.count('like')) # 'like' 문자열이 출현한 횟수를 반환

print ("s1.find('like')         " , s1.find('like')) # 'like'의 첫글자 위치 (offset)를 반환
print ("s1.find('programming')  " , s1.find('programming')) # 'programming'의 첫글자 위치를 반환
print ("s1.find('like', 3)      " , s1.find('like', 3) )# offset=3 부터 'like'을 검색하여 'like'의 첫글자 위치 반환
print ("s1.find('my')           " , s1.find('my') )# 'my' 단어는 없기 때문에 -1 반환


s3 = 'i like programming, i like swimming.'
print ("s3.startswith('i like')   " , s3.startswith('i like')) # 'i like'로 시작하는 문자열인지 판단
print ("s3.startswith('I like')   " , s3.startswith('I like')) # 대소문자 구별

print ("s3.endswith('swimming.')  " , s3.endswith('swimming.')) # 'swimming.'로 끝나는 문자열인지 판단
print ("s3.startswith('progr', 7) " , s3.startswith('progr', 7) )# 7번째 문자열이 'progr'로 시작하는지 판단

u = 'spam and ham'
print (u.replace('spam', 'spam, egg')) # replace()는 새로운 스트링을 생성함
print ("replace    u  -> "         , u)
u = ' spam and ham '
print (" u.split() "         , u.split() )# 공백으로 분리 (모든 공백 제거 및 문자열 내의 단어 리스트를 얻을 수 있음)
print (" u.split('and') "    , u.split('and')) # 'and'로 분리
u2 = 'spam and ham\tegg\ncheese'
print ("u2.split() "         , u2.split())
print ("-------------------------------------")
print ("----   join -> 연결한 문자열 반환     ")
print ("-------------------------------------")
u = 'spam ham\tegg\ncheese'
t = u.split() # 문자열 내의 단어 리스트
print ("u.split 99-->", t)

t2 = ':'.join(t) # 리스트 t 내부의 각 원소들을 ':'로 연결한 문자열 반환
print ("type(t2)->" , type(t2))
print ("':'.join(t)-->", t2)
print ()
t3 = ",".join(t) # 리스트 t 내부의 각 원소들을 ','으로 연결한 문자열 반환
print ("t3->" , t3)
print ("----------------------------------------------------")
print ("----    각각의 문자열을 지정하여 사용       ")
print ("----------------------------------------------------")
u = 'spam and egg'
c = u.center(60) # 60자리를 확보하되 기존 문자열을 가운데 정렬한 새로운 문자열 반환
print ("", type(c))
print (c)
print ("u.ljust(60)->", u.ljust(60)) # 60자리를 확보하되 기존 문자열을 왼쪽 정렬한 새로운 문자열 반환
print ("u.rjust(60)->",u.rjust(60)) # 60자리를 확보하되 기존 문자열을 오른쪽 정렬한 새로운 문자열 반환
print ("---------------------- Character -------------------")
print ('1234'.isdigit()) # 문자열 내의 Character들이 모두 숫자인가?
print ('abcd'.isalpha()) # 문자열 내의 Character들이 모두 영문자인가?
print ('1abc234'.isalnum()) # 문자열 내의 Character들이 모두 영문자 또는 숫자인가?
print ('abc'.islower() )# 문자열 내의 Character들이 모두 소문자인가?
print ('ABC'.isupper()) # 문자열 내의 Character들이 모두 대문자인가?
print ('\t\r\n'.isspace()) # 문자열 내의 Character들이 모두 공백 문자인가?
print ('This Is A Title'.istitle()) # 문자열이 Title 형식 (각 단어의 첫글자가 대문자)인가?

