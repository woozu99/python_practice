from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import xlsxwriter as xl
from io import BytesIO
import urllib.request as req

d = datetime.today()

file_path = f'C:/test/crawling/멜론일간차트순위_{d.year}_{d.month}_{d.day}.xlsx'
driver = webdriver.Chrome(r'C:\Users\admin\Desktop\java\github_up\python_practice\crawling\chromedriver.exe')
web_page = 'https://www.melon.com/chart/day/index.htm'

driver.implicitly_wait(5)

driver.get(web_page)

workbook = xl.Workbook(file_path)
worksheet = workbook.add_worksheet()

cell_format = workbook.add_format({'bold': True, 'font_color':'red', 'bg_color':'yellow'})
worksheet.write('A1', '순위', cell_format)
worksheet.write('B1', '이미지', cell_format)
worksheet.write('C1', '노래제목', cell_format)
worksheet.write('D1', '가수', cell_format)
worksheet.write('E1', '앨범', cell_format)

cnt = 2

soup = BeautifulSoup(driver.page_source, 'html.parser')

for num in [50, 100]:
    music_list = soup.select(f'#lst{num}')


    for music_info in music_list:

        rank = music_info.select_one('.rank').text.strip()
        image_url = music_info.select_one('a.image_typeAll > img')
        title = music_info.select_one('div.rank01 > span > a').text.strip()
        singer = music_info.select_one('div.rank02 > a').text.strip()
        album = music_info.select_one('div.rank03 > a').text.strip()

        print(rank, image_url, title, singer, album)
        # print(rank, title, singer, album)

        worksheet.write(f'A{cnt}', rank)

        try:
            img_data = BytesIO(req.urlopen(image_url['src']).read())
            worksheet.insert_image(f'B{cnt}', image_url['src'], {'image_data':img_data, 'x_scale':0.5, 'y_scale':0.5})

        except:
            pass

        worksheet.write(f'C{cnt}', title)
        worksheet.write(f'D{cnt}', singer)
        worksheet.write(f'E{cnt}', album)

        cnt += 1

driver.close()
workbook.close()