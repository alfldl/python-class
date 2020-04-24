import imaplib
import email  # 파싱 필요 모듈
# 1.IMAP Server에 접속
imap = imaplib.IMAP4_SSL('imap.gmail.com')
# 2.IMAP Server Login
imap.login('ttaekwang3@gmail.com','ktg9489#@!')
# 3.INBOX선택(받은편지함)
imap.select('inbox')
# -----------------------------------------------
# 4.email 검색
# -----------------------------------------------
# 전체를 검색(search) -> 고유 id(uid) 검색 ,unpacking 하여 받음
result, data = imap.uid('search', None, "ALL")
# 확보된 uid Data중 가장 마지막 자료 가져오면 최근 자료 가져옴
latest_email_uid = data[0].split()[-1]
# fetch를 통해 확보된 uid Data중 실제 Mail Data를 가져옴
result, data = imap.uid('fetch', latest_email_uid,'(RFC822)')
# 사람이 읽기 힘든 가공되지 않은 Data , Byte String
raw_email = data[0][1]

# 5. Raw Email Parsing(파싱하기)
#  byte가 string로 바뀜
email_message = email.message_from_string(raw_email.decode('utf-8'))
email_message['To']  # 받는 사람
email.utils.parseaddr(email_message['From'])  # 보낸사람

# 6.eMail 본문 내용 확인
if email_message.is_multipart():
    for p in email_message.get_payload():
        print(p.get_payload())

# 7. 로그아웃
imap.close()
imap.logout()
