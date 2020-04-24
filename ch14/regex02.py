# e-mail 추출기
# 1.pyperclip 모듈을 사용 복사와 붙여넣기
# 2.regex만듦 ,  e-mail 주소 매칭
# 3. 모든 매치를 찾는다
# 4. 매칭된 String을 하나의 문자열로 만든다
# 5. 매칭된 문자열이 없으면 간단한 메세지 출력
import  re
import pyperclip
# Create e-Mail regex  --> VERBOSE, X
# ''' -> MultiLine
email_regex = re.compile(r'''(
   [a-zA*Z0-9._%+-]+       # username
   @                        #  @ sysbol
   [a-zA-Z0-9.-]+          # domain name
   (\.[a-zA-Z]{2,4}){1,2}  # dot-something
 )''', re.VERBOSE)

# email Site https://en.wikipedia.org/wiki/Email_address
# ClipBoard에 복사된 내용에서 e-Mail Pattern과 매치되는 Text를 찾음
def find_match_list():
    text = pyperclip.paste()
    # clip Board에 있는 List를 하나씩 꺼내 matches List에 넣음
    matches = []
    print("find_match_list text-> Start...")
    print("find_match_list text->", text)
    # email에 있는 List Append
    for email in email_regex.findall(text):
        matches.append(email[0])

    print("find_match_list matches->", matches)

    return matches

# ClipBoard에 복사
def copy_result_to_clipboard(matches):
    if len(matches) > 0:
        # List하나하나가 개행되어 처리
        pyperclip.copy('\n'.join(matches))
        print('ClipBoard에 복사 됨')
    else:
        print("매칭되는 Pattern이 없음")

# ClipBoard에 복사된 내용에서 e-Mail Pattern과 매치되는 Text를 찾음
def main():
    matches = find_match_list()
    print("main matches->", matches)
    copy_result_to_clipboard(matches)

main()