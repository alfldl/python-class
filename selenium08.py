#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# 드라이버1 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:/PycharmProjects/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
# chromedriver = '/usr/local/Cellar/chromedriver/chromedriver' # 맥
driver = webdriver.Chrome(chromedriver)

driver.get('http://v.media.daum.net/v/20170202180355822')

i = 0
# 1. div안의 id="harmonyContainer" 해당 속성 가져옴
# body = driver.find_element_by_xpath("//div[@id='harmonyContainer']")
body = driver.find_element_by_xpath("//div[@class='article_view']")

# 1안의 tag_name이 p인것을 순환하며 가져옴
for num, p in enumerate(body.find_elements_by_tag_name('p')):
    print('no:{}  p-내용:{}'.format(num, p.text) )

driver.quit()