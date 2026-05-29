from ys_module_ex_001 import user_delete
from ys_module_ex_001 import sign_up
from ys_module_ex_001 import sign_in
from ys_module_ex_001 import sign_out
from ys_module_ex_001 import modify_profile

import ry_config
import ry_moduleEx
import hj_memo_config
import hj_memo_DB
from datetime import datetime
import hj_memo_read_config
from hj_memo_service import MemoService
from hj_memo_dumy import memoDummyInit

member = {}
current_user = None
bankAccount = []
currentMoney = 0
current_user = None

while True:
    print("\n--- 메뉴를 선택하세요 ---")
    # try:
    #     selectedMenuNum = int(input('1.회원가입    2.로그인     99. 종료'))
    #     # selectedMenuNum = int(input('3.로그아웃     4.회원 정보 수정    5. 회원 탈퇴, 99. 종료'))
    # except ValueError:
    #     print("숫자만 입력 가능합니다.")
    #     continue

    selectedMenuNum = int(input('1.회원가입    2.로그인 '))
    # selectedMenuNum = int(input('3.로그아웃    4.회원 정보 수정   5. 회원 탈퇴 '))

    if selectedMenuNum == 1:
        sign_up(member)
        
    elif selectedMenuNum == 2:
        current_user = sign_in(member)
        
    if current_user:
        while True:
            selectMenu = ry_moduleEx.userSelectedMenuNum()

            if selectMenu == ry_config.MENU_DEPOSIT:
                
                print('=' *70)
                accountNumber = ry_moduleEx.selectdumyInit()
                while True:
                    inMoney = int(input('입금 금액: '))
                    inMoneyMemo = input('메모 내용: ')
                    currentMoney += inMoney
                        
                    print(f'총 금액: {currentMoney}')
                    print('=' *70)

                    nowTime = ry_moduleEx.usertimeLine()
                    memo = ry_moduleEx.usermemoLine(nowTime, inMoney, inMoneyMemo, currentMoney )           
                    bankAccount.append(memo)

                    again = input('계속 입금을 진행하려면 1, 아니면 2를 입력하세요: ')

                    if again == '2':
                        break
                        
            elif selectMenu == ry_config.MENU_WITHDRAWAL:
                print('=' *70)
                accountNumber = ry_moduleEx.selectdumyInit()
                while True:
                    subMoney = int(input('출금 금액: '))
                    subMoneyMemo = input('메모 내용: ')
                    currentMoney -= subMoney

                    accountNumber = ry_moduleEx.selectdumyInit()
                                
                    print(f'총 금액: {currentMoney}')
                    print('=' *70)

                    nowTime = ry_moduleEx.usertimeLine()
                    memo = ry_moduleEx.usermemoSubLine(nowTime, subMoney, subMoneyMemo, currentMoney)
                    bankAccount.append(memo)
                    
                    again = input('계속 출금을 진행하려면 1, 아니면 2를 입력하세요: ')

                    if again == '2':
                        break

            elif selectMenu == ry_config.MENU_INQUIRY:
                accountNumber = ry_moduleEx.selectdumyInit()

                inputAccount = input('계좌번호 입력: ')
                if inputAccount == accountNumber["banknumber"]:
            
                    print('=' *75)
                    print(f'{"날짜&시간":<20} {"입금":<10} {"출금":<10} {"내역":<10} {"잔액":<10} ')
                            # print(f'memoList: {memoList}')
                    print('=' *75)
                    # if inMoneyMemo in memoList or subMoneyMemo in memoList:
                    #     memoList = hj_memo_DB.userMemoList
                    for history in bankAccount:
                        print(history)
                    print('=' *75)
                            
                    break
                
                else:
                    print('입력하신 계좌정보가 없습니다.')
                    
                    
            if selectedMenuNum == hj_memo_config.MEMO_UPDATE:                
                # selectedMenuNum = int(input('3.수정 4.삭제 99.종료 ')

                MemoService.showMemoList()
                        # MemoService().modifyMemo(modifyNum, newMemo)
                        

                modifyNum = int(input('수정할 메모 번호 입력: '))
                newMemo = input('새로운 메모 입력: ')
                        
                MemoService().modifyMemo(modifyNum, newMemo)

                print('메모 수정이 완료되었습니다')

                            


    # elif selectedMenuNum == 3:
    #     current_user = sign_out(current_user)

    # elif selectedMenuNum == 4:
    #     modify_profile(member, current_user)


    # elif selectedMenuNum == 5:
    #     current_user = user_delete(member, current_user)

    # elif selectedMenuNum == 99:
    #     print('프로그램을 종료합니다.')
    #     break
    # else:
    #     print("없는 메뉴입니다. 다시 선택해주세요.")
