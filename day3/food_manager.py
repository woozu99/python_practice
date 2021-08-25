
'''
* 사전을 사용한 음식점 메뉴판 관리 프로그램.
- key: 음식명, value: 음식의 가격
'''
foods = {}

while True:

    print("\n\n====== 음식점 메뉴 관리 프로그램 ======")
    print("# 1. 신규 메뉴 등록하기")
    print("# 2. 메뉴판 전체보기")
    print("# 3. 프로그램 종료")
    print("===========================================")
    menu = int(input("# 메뉴 입력: "))

    if menu == 1:
        '''
        1. 메뉴명을 입력받아 해당 메뉴가 사전에 이미 존재한다면
         이미 등록된 메뉴라고 얘기해 주세요.
        2. 사전에 존재하지 않는 메뉴라면 가격을 입력받아
        key:value 쌍으로 맵핑하여 사전에 저장하세요.
        '''
        menu_name = input('추가하실 메뉴명을 입력하세요: ')
        if menu_name in foods:
            print(f'{menu_name}는 이미 존재하는 메뉴입니다.')
        else:
            menu_price = int(input(f'{menu_name}의 가격을 입력하세요: '))
            foods[menu_name] = menu_price
            
    elif menu == 2:
        '''
        - 만약 2번을 선택했는데, 메뉴가 하나도 등록되어 있지 않다면
        먼저 등록하라고 메인 메뉴로 돌려보내 주세요.

        - 사전에 등록된 메뉴명과 가격을 전부 출력해 주세요.
        ex) 짜장면 : 4000원
            탕수육 : 18000원
            짬뽕 : 7000원 ...
        -----------------------------------------

        메뉴판 전체 출력 후 메뉴를 새롭게 입력받아 주세요.
        ex (1. 수정 | 2. 삭제 | 3. 나가기)
        새로운 메뉴를 입력받아서 수정과 삭제를 진행 해 주세요.
        # 수정 -> 가격을 변경할 메뉴의 이름을 먼저 입력받고
        해당 이름이 사전에 존재한다면 수정할 가격을 새롭게 입력받고
        수정을 진행 해 주세요. 이름이 없다면 없다고 출력.
        # 삭제 -> 삭제할 메뉴명을 입력받아서 삭제를 진행.
         이름이 없으면 없다고 출력.
        # 나가기 -> 메인메뉴로 나가시면 됩니다.
        '''

        

        while True:
            print('-' * 40)

            if len(foods) == 0:
                print('등록된 메뉴가 없습니다. 메뉴를 등록해주세요.')
                break
            else:
                 for k in foods:
                    print(k, ':', f'{foods[k]}원')

            inner_menu = int(input('1.수정 | 2. 삭제 | 3. 나가기\n'))

            if inner_menu == 1:
                menu_name = input('수정하실 메뉴명을 입력하세요: ')
                
                if menu_name in foods:
                    menu_price = int(input(f'{menu_name}의 가격을 입력하세요: '))
                    foods[menu_name] = menu_price
                else:
                    print(f'{menu_name}는 존재하지 않는 메뉴입니다.')
                    
            elif inner_menu == 2:
                menu_name = input('삭제하실 메뉴명을 입력하세요: ')
                    
                if menu_name in foods:
                    del(foods[menu_name])
                    print(f'{menu_name}이(가) 삭제되었습니다.')
                else:
                    print(f'{menu_name}는 존재하지 않는 메뉴입니다.')
            elif inner_menu == 3:
                break

            else:
                print('잘못된 입력입니다. 다시 입력해주세요.')



    elif menu == 3:
        '''
        ("# 프로그램을 종료하시겠습니까? [Y / N]")
        프로그램 종료 여부를 한번 더 물어봐 주세요.
        만약 y 이외의 값이 들어온다면 종료 의지가 없다고 판단하고
        종료를 취소하도록 하겠습니다.
        '''

        is_end = input('# 프로그램을 종료하시겠습니까? [Y / N]\n')
        if is_end == 'y' or is_end == 'Y':
            print('프로그램을 종료합니다.')
            break
        else:
            print('프로그램 종료를 취소하셨습니다.')
      
    else:
        print("메뉴를 잘못 입력하셨습니다.")

