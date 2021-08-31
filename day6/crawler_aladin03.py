
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from datetime import datetime

# 엑셀처리 모듈 임포트
import xlsxwriter

# user-agent 정보를 변환해 주는 모듈 임포트
# 특정 브라우저로 크롤링을 진행할 때 차단되는 것을 방지
from fake_useragent import UserAgent

# 이미지를 바이트 변환 처리 모듈
from io import BytesIO

# 요청 헤더 정보를 꺼내올 수 있는 모듈
import urllib.request as req


d = datetime.today()

file_path = f'C:/test/crawling/알라딘 베스트셀러 1~400위(뉴 버전)_{d.year}_{d.month}_{d.day}.xlsx'

# User Agent 정보 변환 (필수는 아니다.)
opener = req.build_opener() # 헤더 정보를 초기화
opener.addheaders = [('User-agent', UserAgent().ie)]
req.install_opener(opener) # 새로운 헤더 정보 삽입.

# 엑셀 처리 선언
# Workbook 객체를 생성하여 엑셀 파일을 하나 생성(매개값으로 저장될 경로 지정.)
workbook = xlsxwriter.Workbook(file_path)

# 워크 시트 생성
worksheet = workbook.add_worksheet()

# 브라우저 안뜨게 하기
chrome_option = Options()
chrome_option.add_argument('--headless')

# 브라우저 설정 - 일반 모드
browser = webdriver.Chrome(r'C:\Users\admin\Desktop\java\github_up\python_practice\crawling\chromedriver.exe')

# 브라우저 사이즈 조정
browser.set_window_size(800, 600)

# 브라우저 내부 대기
# time.sleep(10) -> 브라우저 로딩에 상관없이 무조건 10초 대기.
# 웹 페이지 전체가 로딩될 때 까지 대기 후 남은시간 무시. 
browser.implicitly_wait(5)

# 브라우저 설정 - headless 모드
# browser = webdriver.Chrome('C:/Users/admin/Desktop/java_web_LKM/python/crawling/chromedriver.exe', options=chrome_option)

# 페이지 이동
target_page = 'https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1'
browser.get(target_page)

# 엑셀에 텍스트 저장
cell_format = workbook.add_format({'bold': True, 'font_color':'red', 'bg_color':'yellow'})
worksheet.write('A1', '썸네일', cell_format)
worksheet.write('B1', '제목', cell_format)
worksheet.write('C1', '작가', cell_format)
worksheet.write('D1', '출판사', cell_format)
worksheet.write('E1', '출판일', cell_format)
worksheet.write('F1', '가격', cell_format)
worksheet.write('G1', '링크', cell_format)

cur_page_num = 2 # 현재 페이지 번호
target_page_num = 9 # 목적지 페이지 번호
rank = 1 # 순위
cnt = 2 # 엑셀 행 수 카운트 해 줄 변수

while True:
    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    div_ss_book_box_list = soup.find_all('div', class_='ss_book_box')

    for div_ss_book_box in div_ss_book_box_list:
        # 이미지
        img_url = div_ss_book_box.select_one('table div > a > img.i_cover')

        # 타이틀, 작가, 가격을 모두 포함하는 ul부터 지목
        ul = div_ss_book_box.select_one('div.ss_book_list > ul')

        # 타이틀
        title = ul.select_one('li > a.bo3')

        # 작가
        author = title.find_parent().find_next_sibling()

        # 작가 데이터 상세 분해
        author_datas = author.text.split('|')
        author_name = author_datas[0].strip()
        company = author_datas[1].strip()
        pub_day = author_datas[2].strip()

        # 가격
        price = author.find_next_sibling()
        price_data = price.text.split(', ')[0]

        # 책 상세 정보 페이지 링크
        # title이라는 변수에 a태그를 지목해 놓은 상태.
        # title -> a태그의 요소 전부를 가지고 있는 상태.
        # 'href'로 작성된 키를 전달하고 해당 value를 받아 변수에 저장.
        page_link = title['href']

        # 이미지 바이트 변환 처리
        # BytesIO 객체의 매개값으로 아까 지목해 놨던 img의 src값을 전달.
        try:
            img_data = BytesIO(req.urlopen(img_url['src']).read())
        
            # 엑셀에 이미지 저장
            worksheet.insert_image(f'A{cnt}', img_url['src'], {'image_data':img_data, 'x_scale':0.5, 'y_scale':0.5})
        
        except:
            # 파이썬에서는 블록구조에 아무 것도 쓰지 않으면 에러.
            # 해당 블록을 건너뛰고 싶으면 pass를 쓰면 됨.
            pass

        # 엑셀에 나머지 텍스트 저장
        worksheet.write(f'B{cnt}', title.text)
        worksheet.write(f'C{cnt}', author_name)
        worksheet.write(f'D{cnt}', company)
        worksheet.write(f'E{cnt}', pub_day)
        worksheet.write(f'F{cnt}', price_data)
        worksheet.write(f'G{cnt}', page_link)

        cnt += 1
        rank += 1

    # 다음 페이지(탭)로 전환
    cur_page_num += 1
    browser.find_element_by_xpath(f'//*[@id="newbg_body"]/div[3]/ul/li[{cur_page_num}]').click()
    del(soup)
    time.sleep(3)

    if cur_page_num > target_page_num:
        print('크롤링 종료!')
        break # while True break


browser.close()
workbook.close()
