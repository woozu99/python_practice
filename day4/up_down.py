import random
import time

ran_num = random.randint(1, 100)
count = 6

print('즐거운 업다운 게임!')
time.sleep(1)

while True:
    your_num = int(input('숫자를 입력하세요: '))
    
    if your_num == ran_num:
        print('정답입니다.')
        if count >= 0:
            print('제한 횟수 내에 맞추셔서 승리하셨습니다.')
        else:
            print('제한 횟수 내에 맞추지 못하여 패배하셨습니다')
        break
    
    elif your_num > ran_num:
        count -= 1
        print('down')
    else:
        count -= 1
        print('up')
    
    if count > 0:
            print(f'기회가 {count}회 남았습니다.')
    else:
        print('기회를 다 소진하셨습니다. 그래도 계속 진행해주세요.')