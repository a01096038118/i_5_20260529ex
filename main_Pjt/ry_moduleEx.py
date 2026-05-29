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