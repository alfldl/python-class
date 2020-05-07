import re

# 1. 정규식에 search  사용 -> 매칭되는 첫번째 pattern 반환
#     전화번호에 해당하는 pattern
phonenum_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phonenum_regex.search("My Number is 315-234-1234")
print("mo.group()->" , mo.group())
print("---2. 괄호를 사용 , 정규식에 Group를 생성 , (\d\d\d) -> Group함수 사용--" )

# 2. 괄호를 사용 , 정규식에 Group를 생성 , (\d\d\d) -> Group함수 사용
phonenum_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo=phonenum_regex.search("My Number is 315-567-1234")
print("mo.group(1)->" , mo.group(1))
print("mo.group(2)->" , mo.group(2))
print("mo.group(3)->" , mo.group(3))
# tuple로 전달
print("mo.groups()->" , mo.groups())

# 3. findall -> 매칭되는 모든  pattern을 List로 반환
phonenum_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phonenum_regex.findall("cell: 315-235-5679  Work : 213-234-3456")
print("3. mo->" , mo)

