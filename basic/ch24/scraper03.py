import requests
#   package   첫 글자가 대문자면 Class
from bs4 import BeautifulSoup
import csv

# 이 싸이트 Table들을  읽어서 CSV 파일로 저장
# 대문자로 주면 상수로 묵시적 약속
BASE_URL = 'http://www.pythonscraping.com'


def create_list_from_table(table_tag):
    # CSV File로 만들기 위해 2중 List 생성
    gifts = []

    # Header에 해당하는 첫번째 Row 작성
    headers=[]
    header_tag = table_tag.find('tr')
    for th_tag in header_tag.find_all('th'):
        # space등 제거
        headers.append(th_tag.text.strip())

    print('headers->', headers)
    gifts.append(headers)

    # 본문 : 선물 record 작성
    for tr_tag in table_tag.find_all('tr'):
        gift = []
        for td_tag in tr_tag.find_all('td'):
            if td_tag.text.strip() != '':
                # 좌우공백제거 , \n문자를 공백 변경
                gift.append(td_tag.text.strip().replace('\n', ' '))
            else:
                # text문자가 없으면 img라 가정 , img tag를 가져오기 위한 처리
                #  img tag 의 src 속성을 가져옴 , 3번째 문자부터 끝까지 가져옴--> ../
                gift.append(BASE_URL+td_tag.find('img').get('src')[2:])

        if not gift:
            continue

        gifts.append(gift)
    print('gifts->', gifts)

    return gifts

def create_csv_file(gifts, filename):
    with open(filename , 'w' , encoding='utf-8' , newline='') as file:
        writer = csv.writer(file)
        # gifts를 Line단위로
        for line in gifts:
            writer.writerow(line)


def main():
    res = requests.get(BASE_URL+"/pages/page3.html")
    # HTML(XML)을 Parsing하기 좋게  Python객체
    # html.parser(기본) 보다 좀 더 강력한 lxml(설치필요)많이 사용
    soup = BeautifulSoup(res.text,'lxml')

    #  1. table tag 선택하여 확보 함
    table_tag = soup.find(id='giftList')
    print("jtable_tag->%s" %table_tag)
     # 2. List 형태로 가져옴
    gifts = create_list_from_table(table_tag)
    # 3. csv 형태의 file로 만듦
    create_csv_file(gifts , 'gifts.csv')
    print("csv Completed ...")
    #print("table_tag->", table_tag)


if __name__  == '__main__':
    main()