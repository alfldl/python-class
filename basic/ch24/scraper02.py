import requests
#   package   첫 글자가 대문자면 Class
from bs4 import BeautifulSoup

res = requests.get("http://book.naver.com")

# HTML(XML)을 Parsing하기 좋게  Python객체
# html.parser(기본) 보다 좀 더 강력한 lxml(설치필요)많이 사용
soup = BeautifulSoup(res.text,'lxml')
#  soup안의  tag를 지정
a_tag = soup.a
div_tag = soup.div

#print("type(a_tag)->", type(a_tag))
#print("a_tag.prettify()->", a_tag.prettify())
print("type(div_tag)->", type(div_tag))
print("div_tag->", div_tag)
