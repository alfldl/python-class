# 파일 생성(파일 쓰기)
# test.txt 파일 생성함


file = open('test.txt', 'w')        # 쓰기 모드로 열기

file.write('hello')                 # test.txt파일에 'hello' 쓰기

file.close()                        # 파일 닫기