'''
* 사용자의 입력을 파일(xxx.txt)에 저장하는 프로그램을 작성하세요.
(단 프로그램을 다시 실행하더라도 파일명이 동일하다면 기존 작성한 내용을 그대로 유지하고 새로 입력된 내용이 추가되어야 합니다.)
'''
root_path = 'C:\\test\\'
text = ''

print('저장할 내용을 입력(\'그만\'이라고 입력 시 종료됩니다')

while True:
    in_text = input('> ')
    
    if in_text == '그만':
        break
        
    text += in_text
    text += '\n'
    
if text == '':
    print('입력하신 내용이 없습니다. 프로그램을 종료합니다.')
else:
    in_title = input('파일명을 입력: ')
    title = root_path + in_title + '.txt'

    try:
        f = open(title, 'a')
        f.write(text)
        print('파일 저장 성공!')
    except:
        print('파일 저장 실패!')
    finally:
        f.close()