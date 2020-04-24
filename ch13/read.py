# 파일 읽기
# test.txt 파일을 읽기 모드로 열고, 내용을 출력
file = open('test.txt', 'r',  encoding='UTF8')          # 읽기 모드로 test.txt 파일 열기
str = file.read()                      # text.txt 파일의 모든 내용을 읽어와서  str변수에 저장함
print(str)
file.close()                            # 파일 닫기
