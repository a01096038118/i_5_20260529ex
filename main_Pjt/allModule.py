import random
from ys_module_ex_001 import user_delete
from ys_module_ex_001 import sign_up
from ys_module_ex_001 import sign_in
from ys_module_ex_001 import sign_out
from ys_module_ex_001 import modify_profile
from ys_module_ex_001 import inputSelectedMenuNum
import ry_config
import ry_moduleEx
import hj_memo_config
import hj_memo_DB
from datetime import datetime
import hj_memo_read_config
from hj_memo_service import MemoService
from hj_memo_dumy import memoDummyInit

userMemoList = []

MEMO_WRITE = 1
MEMO_READ = 2
MEMO_UPDATE = 3
MEMO_DELETE = 4
MEMO_EXIT = 99
DEV_MOD = True

MEMO_READ_LATEST = 1
MEMO_READ_OLDEST = 2
MEMO_READ_MONTH = 3

MENU_DEPOSIT = 1
MENU_WITHDRAWAL = 2
MENU_INQUIRY = 3
EXIT = 4



def inputSelectedMenuNum():
    selectedMenuNum = int(input('1.회원가입    2.로그인 '))
    return selectedMenuNum

def sign_up(member):
    print(('회원가입을 하시려면 가입하시려는 UID, UPW, UMAIL, UPHONE를 입력해 주세요.' ))
    UID = input('UserId: ')
    if UID == "":
        print('아이디는 공백으로 만들 수 없습니다.')
        return
    if UID in member:
        print('동일한 아이디로는 가입할 수 없습니다.')
        return
    if not UID.isalnum():
        print('아이디에는 특수 문자를 사용할 수 없습니다.')
        return
    
    UPW = input('UserPw: ')
    UPW_confirm = input('UserPw Confirm (비밀번호 확인): ')
    if UPW != UPW_confirm:
        print('비밀번호가 일치하지 않습니다. 회원가입을 취소합니다.')
        return
    else:
        UEMAIL = input('UserEmail: ')
        UPHONE = input('UserPhone: ')

        print('회원가입이 완료되었습니다.')
        member[UID] = {
            'UID': UID,
            'UPW': UPW,
            'UEMAIL': UEMAIL,
            'UPHONE': UPHONE
                    }
    
    
    
def sign_in(member):
    if not isinstance(member, dict):
        print("로그인 시스템에 오류가 발생했습니다. (회원 데이터가 올바르지 않습니다.)")
        return None
    print('로그인하실 UserID, UserPW를 입력해주세요. ')
    Login_ID = input('UserId: ')
    Login_PW = input('UserPw: ')
    if Login_ID in member: 
        if member [Login_ID] ['UPW'] == Login_PW:
            print('로그인이 완료되었습니다.')
            return Login_ID
                
        else:
            print('비밀번호가 틀렸습니다. ')  
            return None  
    else:
        print('회원님의 정보가 없습니다. ')
        return None

def sign_out(current_user):
    if current_user is None :
            print('현재 로그인되어있지 않습니다.')
            return None
            
    else:
        print(f'{current_user}님, 로그아웃 되었습니다.')
        return None

def modify_profile(member, current_user):
    if current_user is None :
        print('현재 로그인되어있지 않습니다.')
    else:
        selectedUpdateMenu = int(input('PW를 수정하시려면 1, EMAIL을 수정하시려면 2, PHONE을 수정하시려면 3, 전부 수정하시려면 4를 눌러주세요(ID는 변경 불가) '))
        if selectedUpdateMenu == 1:
            print(f'{current_user}님, 수정하실 PW를 입력해주세요.')
            New_PW = input('New_Pw: ')
            if member[current_user]['UPW'] == New_PW:
                print('기존과 동일한 비밀번호입니다.')
            else:
                member[current_user]['UPW'] = New_PW
                print('변경이 완료되었습니다.')

        elif selectedUpdateMenu == 2:
            print(f'{current_user}님, 수정하실 EMAIL를 입력해주세요.')
            New_EMAIL = input('New_Email: ')
            if member[current_user]['UEMAIL'] == New_EMAIL:
                    print('기존과 동일한 이메일입니다.')
            else:
                member[current_user]['UEMAIL'] = New_EMAIL
                print('변경이 완료되었습니다.')

        elif selectedUpdateMenu == 3:
            print(f'{current_user}님, 수정하실 PHONE를 입력해주세요.')
            New_PHONE = input('New_UPhone: ')
            if member[current_user]['UPHONE'] == New_PHONE:
                print('기존과 동일한 전화번호입니다.')
            else:
                member[current_user]['UPHONE'] = New_PHONE
                print('변경이 완료되었습니다.')

        elif selectedUpdateMenu == 4:
            print(f'{current_user}님, 수정하실 PW, EMAIL, PHONE를 입력해주세요.')
            new_pw = input('New_Pw: ')
            new_email = input('New_Email: ')
            new_phone = input('New_Phone: ')
            updated_fields = []

            if member[current_user]['UPW'] != new_pw:
                member[current_user]['UPW'] = new_pw
                updated_fields.append('비밀번호')
        
            if member[current_user]['UEMAIL'] != new_email:
                member[current_user]['UEMAIL'] = new_email
                updated_fields.append('이메일')
            
            if member[current_user]['UPHONE'] != new_phone:
                member[current_user]['UPHONE'] = new_phone
                updated_fields.append('전화번호')

            if updated_fields:
                print(f"[{', '.join(updated_fields)}] 변경이 완료되었습니다.")
            else:
                print("변경된 정보가 없습니다.")
        else:
            print("잘못된 메뉴 선택입니다.")

def user_delete(member, current_user):
    if current_user is None :
        print('현재 로그인되어있지 않습니다.')
        return current_user
    else:
        password = f'{random.randint(0, 9999):04d}'
        print('탈퇴를 위해 패스워드를 입력받겠습니다. 아래에 나온 패스워드를 입력해주세요. ')
        print(f'Password: {password}')
        User_input = input('password: ')
        if User_input == password:
            del member[current_user]
            print('회원 탈퇴가 완료되었습니다. ')
            return None
        else:
            print('인증 번호가 일치하지 않아 탈퇴할 수 없습니다..')
            return current_user
        
from datetime import datetime


def selectdumyInit():
    accountNumber = {
             'name': '홍길동',
             'bank': 'DW은행',
             'banknumber': '123-456789-012'
             }
    return accountNumber

def userSelectedMenuNum():
    selectMenu = int(input('1.입금   2.출금   3.조회   4.종료 '))
    return selectMenu

def usertimeLine():
    nowTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return nowTime

def usermemoLine(nowTime, inMoney, inMoneyMemo, currentMoney ):
    memo = f'[{nowTime}] \t {inMoney:<10} {0:<10} \t {inMoneyMemo:<8} \t{currentMoney:<10}'
    return memo

def usermemoSubLine(nowTime, subMoney, subMoneyMemo, currentMoney):
    memo = f'[{nowTime}] \t {0:<10} {-subMoney:<10} \t {subMoneyMemo:<8} \t{currentMoney:<10}'
    return memo

def userReadNumber(accountNumber):

    inputNumber = input('계좌번호 입력: ')

    if inputNumber == accountNumber:
        return True

    else:
        return False
    
class MemoService:
     
    def __init__(self, memoList):
        self.memoList = memoList

    # def getTime(self, memo):
    #     return memo['작성시간']

    def readLatest(self): # 내림차순
        self.memoList.sort(key=self.getTime, reverse=True)
        
        for memo in self.memoList:
            for key, value in memo.items():
                print(f'{key}: {value}')
            print('-' * 40)
            
    def readOldest(self): # 오름차순
        self.memoList.sort(key=self.getTime)
        
        for memo in self.memoList:
            for key, value in memo.items():
                print(f'{key}: {value}')
            print('-' * 40)    

    # def readMonth(self):
    #     memoReadMonth = input('조회 월을 입력: [숫자 두자리로 입력하세요. ex) 5월 -> 05] ')
    #     for memo in self.memoList:
    #         monthMemo = memo['작성시간'].split('-')[1]
    #         if memoReadMonth == monthMemo:
    #             print(memo)

    def showMemoList(self):
        for idx, memo in enumerate(self.memoList):
            print(f'{idx}. {memo}')

    def modifyMemo(self, modifyNum, newMemo):
        self.memoList[modifyNum]['메모내용'] = newMemo

    def deleteMemo(self, deleteNum):
        return self.memoList.pop(deleteNum)
        
import hj_memo_DB

def memoDummyInit():

    hj_memo_DB.userMemoList.append({
        '작성시간': '2026-04-01 10:21:11',
        '메모내용': '4월 메모1'
    })
    hj_memo_DB.userMemoList.append({
        '작성시간': '2026-05-02 12:21:11',
        '메모내용': '5월 메모1'
    })
    hj_memo_DB.userMemoList.append({
        '작성시간': '2026-05-05 22:23:05',
        '메모내용': '5월 메모2'
    })
    hj_memo_DB.userMemoList.append({
        '작성시간': '2026-05-28 16:53:44',
        '메모내용': '5월 메모3'
    })