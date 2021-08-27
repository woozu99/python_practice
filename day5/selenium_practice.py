'''
네이버로 접속해서 뉴스스탠드 쪽에 있는 파란 '네이버 뉴스'를 클릭
상단에 있는 메뉴 중 정치, 경제, 사회, 생활/문화, 세계, IT/과학 탭을 돌아다니며 헤드라인 뉴스 4개씩 클릭
뒤로가기는 driver.back()메서드
'''
from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Users\admin\Desktop\java\github_up\python_practice\crawling\chromedriver.exe')

# 뉴스페이지 들어가기
driver.get('https://www.naver.com')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="NM_NEWSSTAND_HEADER"]/div[2]/a[1]').click()
time.sleep(1)

for i in range(6):
    click_btn = driver.find_element_by_xpath(f'//*[@id="lnb"]/ul/li[{3 + i}]/a')
    click_btn.click()
    time.sleep(1)
    for j in range(4):
        if i == 0:
            try:
                click_btn = driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{j + 1}]/div[1]/ul/li[1]/div[1]/div/a')
            except:
                click_btn = driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{j + 1}]/div[1]/ul/li[1]/div[2]/a')
            click_btn.click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
        else:
            try:
                click_btn = driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{j + 1}]/div[2]/ul/li[1]/div[1]/div/a')
            except:
                click_btn = driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{j + 1}]/div[2]/ul/li[1]/div/a')
            click_btn.click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
