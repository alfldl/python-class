# Mail Message사용 객체 선언
from email.message import EmailMessage
import smtplib   # 자체 Core에 포함

# SSL로 Open(SMTP 객체 생성)
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# smtp 정상여부 Hello Test
smtp.ehlo()
# smtp Login  --> 본인 계정으로
smtp.login('ttaekwang3@gmail.com','tae9489#@!')

# Message 생성
msg = EmailMessage()

# 내부적으로 dic으로 선언
msg['Subject'] = '파이썬 Mail Test'
msg['From'] = 'ttaekwang3@gmail.com'
msg['to'] = 'Goldtrol@naver.com'
msg.set_content('''본문 전송 내용 , \n
                 MultiLine 가능
                 파이썬 입니다
                  ''''')
# Mail 전송
smtp.send_message(msg)
# 연결 종료
smtp.quit()

