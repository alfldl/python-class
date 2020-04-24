# 문자열 길이 구하기 ( len() 함수 )

msg = input('임의의 문장을 입력하세요?')
msglen = len(msg)

print('당신이 입력한 문장의 길이는 %d 입니다.' %msglen)
print('당신이 입력한 문장의 길이는 {} 입니다.' .format(msglen))

hello = "날씨가 좋네요"
# utf-8 는 한글 3Byte
length = len(hello.encode('utf-8'))
length3 = len(hello)
print('hello 문장의 길이는 %d 입니다.' %length)
print('hello3 문장의 길이는 %d 입니다.' %length3)
