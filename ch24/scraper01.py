import requests

res = requests.get("http://book.naver.com")
# 단순히 response의 모든 tag 가져옴
print("res.headers->", res.headers)
# dict Type
print("res.text->", res.text)

