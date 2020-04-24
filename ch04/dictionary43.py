d = {'one': 'hana', 'two': 'dul', 'three': 'set'}
d['four'] = 'net' # 새 항목의 삽입
print ("d1->", d)
d['one'] = 1 # 기존 항목의 값 변경
print ("d2->", d)
print ('one' in d)   # 키에 대한 멤버쉽 테스트

d3 = {'one': 1, 'two': '둘', 'three': '삼', 'four': '사'}
print ("d3.keys()->"   , d3.keys())   # 키만 리스트로 추출함,임의의 순서
print ("Type(d3.keys())->"   , type(d3.keys())) # 키만 리스트로 추출함,임의의 순서
print ("d3.values()->" ,      type(d3.values())) # 값만 리스트로 추출함,임의의 순서
print ("d3.values()->" , d3.values()) # 값만 리스트로 추출함,임의의 순서
print ("d3.items()->"  , d3.items())  # 키와 값의 튜플을 리스트로 반환함