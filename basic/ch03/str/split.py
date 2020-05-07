# 문자열을 특정문자로 분리하기 ( split() 함수 )
# split() 함수는 구분자(separator)로 구분되어 있는 문자열을 파싱(parsing)하는 역할을 한다.
url = 'http://www.naver.com/news/today=20160831'
log = 'name:홍길동 age:17 sex:남자 nation:조선'

ret1 = url.split('/')               # url 변수에 저장된 데이터를 구분자('/')로 파싱함
print(ret1)

ret2 = log.split()                  # log 변수에 저장된 데이터를 공백으로 파싱함
print(ret2)
for data in ret2:
   d1, d2 = data.split(':')         # data변수에 저장된 데이터를 구분자(':')로 파싱함
   print('%s -> %s' %(d1, d2))
