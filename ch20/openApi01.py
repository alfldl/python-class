# API : 여러 APPlication 사이에서 간편한 Interface
# Open API
#  1) HTTP통해 Data 요청하며, 주로 XML이나 JSON 형식으로 응답
#  2) 최근  JSON 방식 응답하는 API가 빠르게 늘어나고 있음
#  3) 유용한 형식으로 정리된 Data 제공 받을수 있음
# core에서도 urllib가 있지만 ,주로 requests가 사용 됨 (쉽고 휠씬 편리)
import requests  # 설치
import pprint

# get방식의 호출
res = requests.get('https://developers.naver.com/main/')


#json_res = res.json()
print("type(res)->", type(res))
print("print res.text->", res.text)

# res를 json형태를 파이썬의 dict형태로 전환
#pprint.pprint(res.json())