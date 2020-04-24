import pyperclip

PASSWORDS = {
    'gmail':'FGHkshdkfkgkg',
    'naver':'ttakjt3456',
    'daum':'qwef5678'
}

def main():
    site = input('input your site:')
    password = PASSWORDS[site]

    if password:
        pyperclip.copy(password)
        print('Your password is Copied')
    else:
        print('Not Valid Site')
main()