# 조건 8자이상 , 영문자와 숫자가 혼합
# passwd_val.py

# password='' 가 문자열림을 컴파일러에 알려줌
def validate_password(password=''):
    if(len(password)) < 8:
        return False
    elif password.isalpha():
        return False
    elif password.isnumeric():
        return False
    else:
        return True

def main():
    user_password = input('input Your Password: ')
    if validate_password(user_password):
        print('유효한 password 입니다')
    else:
        print('유효하지 않은 password 입니다')

main()