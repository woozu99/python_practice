'''
* points.txt파일의 숫자값을 모두 읽어서 총합과 평균을 구한 뒤 총점, 평균값을 result.txt라는 파일에 쓰는 프로그램을 작성해 보세요.
'''
import traceback as tb

root_path = 'C:/test/'
read_file_name = 'points.txt'
write_file_name = 'result.txt'

total = 0
count = 0
avg = 0

error_flag = False

try:
    f = open(root_path + read_file_name, 'r')
    str_scores = f.read().split(' ')
    scores = map(int, str_scores)
    
    for i in scores:
        total += i
        count += 1
    
    avg = total / count

except:
    print('읽기 에러 발생')
    print(tb.format_exc())
    error_flag = True
finally:
    f.close()

if not error_flag:
    try:
        f = open(root_path + write_file_name, 'w')
        f.write(f'total: {total}\naverage: {avg:0.2f}')
        print("파일 저장 성공")
    except:
        print('쓰기 에러 발생')
        print(tb.format_exc())
    finally:
        f.close()