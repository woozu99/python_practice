# 셀레늄: 웹 자동화 및 웹이 소스코드를 수집하는 모듈
# cmd -> pip install selenium(셀레늄 라이브러리 다운로드)
# 셀레늄 임포트
from selenium import webdriver
import time

# 다운로드 받은 크롬 물리 드라이버 가동 명령(chromedriver를 다운받아서 설치 경로 적기)
driver = webdriver.Chrome(r'C:\Users\admin\Desktop\java\github_up\python_practice\crawling\chromedriver.exe')
# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.naver.com')

time.sleep(1)

'''
# 자동으로 버튼이나 링크 를릭하기
login_btn = driver.find_element_by_xpath('//*[@id="account"]/a')
login_btn.click()

# 자동으로 텍스트 입력하기
time.sleep(1.5)
id_input = driver.find_element_by_xpath('//*[@id="id"]')
id_input.send_keys('myid')

time.sleep(1)
pw_input = driver.find_element_by_xpath('//*[@id="pw"]')
pw_input.send_keys('mypw')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="log.login"]').click()
'''

# 네이버에 접속해서 검색창에 '오늘 날씨'를 검색한 후 가장 처음에 뜨는 뉴스를 띄우기
driver.find_element_by_xpath('//*[@id="query"]').send_keys('오늘 날씨')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="search_btn"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="sp_nws_all1"]/div[1]/div/a').click()