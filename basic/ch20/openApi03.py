# Open API
# ① http://developers.naver.com 싸이트 이동
# ② Naver API 사용 위해 Application 등록 수행
# ③ 사용 API에서 검색 서비스 선택(get / post 방식)
# ④ 파이썬 검색어로 검색하여 결과 JSON 확인

# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제
# 네이버 검색 Open API 예제 - 블로그 검색
# # 파파고 SMT API 예제
from   requests import Request
from   requests import Session

s = Session()

# ID와 비밀Key Setting
headers = {
    'X-Naver-Client-Id' : 'j513HictYVPoWEl27Yor',
    'X-Naver-Client-Secret' : 'I0m7fwb6Cn' ,
}
text = "Yesterday all my troubles seemed so far away"

# dict Type
payLoad = {
    'source' : 'en',
    'target' : 'ko',
    'text'   : text,
}
# encText = urllib.parse.quote("번역할 문장을 입력하세요")
#data = "source=ko&target=en&text=" + encText
# 문장번역 URL 지정
#url = "https://openapi.naver.com/v1/language/translate"
url = "https://openapi.naver.com/v1/papago/n2mt"
req = Request('POST' , url , data=payLoad, headers=headers)
# 미리 내부적으로 Compile
prepared = req.prepare()
# Session 객체를 통해 전송
res = s.send(prepared)

print("res.json()->", res.json())
# online jsonviewer  --> http://jsonviewer.stack.hu/
result = res.json()['message']['result']['translatedText']
print("result->", result)