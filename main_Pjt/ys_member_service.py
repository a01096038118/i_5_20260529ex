from ys_module_ex_001 import user_delete
from ys_module_ex_001 import sign_up
from ys_module_ex_001 import sign_in
from ys_module_ex_001 import sign_out
from ys_module_ex_001 import modify_profile
member = {}
current_user = None

while True:
    print("\n--- 메뉴를 선택하세요 ---")
    try:
        selectedMenuNum = int(input('1.회원가입    2.로그인    3.로그아웃     4.회원 정보 수정    5. 회원 탈퇴, 99. 종료'))
    except ValueError:
        print("숫자만 입력 가능합니다.")
        continue
    if selectedMenuNum == 1:
        sign_up(member)
        

    elif selectedMenuNum == 2:
        current_user = sign_in(member)

    elif selectedMenuNum == 3:
        current_user = sign_out(current_user)

    elif selectedMenuNum == 4:
        modify_profile(member, current_user)


    elif selectedMenuNum == 5:
        current_user = user_delete(member, current_user)

    elif selectedMenuNum == 99:
        print('프로그램을 종료합니다.')
        break
    else:
        print("없는 메뉴입니다. 다시 선택해주세요.")
