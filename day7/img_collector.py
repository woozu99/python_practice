print('약간의 로딩이 발생할 수 있으니 잠시만 기다려주세요.')
print('인터넷 연결이 되어있어야 합니다.')

# 운영체제에서 제공되는 여러 기능(폴더생성)
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
import time as t

opener = req.build_opener()
opener.addheaders = [('User-agent', UserAgent().ie)]
req.install_opener(opener)


# 네이버 기본 url
base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

print('### 검색어를 입력하시면 해당 검색어에 맞는 이미지를 50개 다운로드 받습니다.')
print('### 이미지 자료는 네이버 검색 자료를 수집합니다.')
print('### 다운받은 이미지는C드라이브 imagedown 폴더에 자동 저장됩니다.')

# 검색어
s = input('### 검색어 입력: ')
quote = rep.quote_plus(s) 
url = base_url + quote

# 저장 경로
save_path = 'C:/imagedown/'

# 폴더 생성(예외처리 필수)
try:
    if not os.path.isdir(save_path):
        # 없으면 폴더 생성
        os.mkdir(save_path)
except OSError as e:
    print('폴더 생성 실패!')
    print('폴더 이름: ', e.filename)

print(url)

res = req.urlopen(url).read()


driver = webdriver.Chrome(r'C:\Users\admin\Desktop\java\github_up\python_practice\crawling\chromedriver.exe')
driver.get(url)

driver.implicitly_wait(5)

src = driver.page_source

# bs4 초기화
soup = BeautifulSoup(src, 'html.parser')
# print(soup)

img_list = soup.select('div.thumb > a > img')
print(img_list)

# 네이버가 크롤링을 못하게 하고있어서 아무것도 안나온다!!젠장

