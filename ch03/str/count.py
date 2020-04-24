# 문자열에 있는 문자의 갯수 구하기 ( count() 함수 )

txt = 'A lot of things occur each day, every day.'
word_count1 = txt.count('o')            # 알파벳 'o' 의 갯수를 구함
word_count2 = txt.count('day')          # 단어 'day' 의 갯수를 구함
word_count3 = txt.count(' ')            # 공백의 갯수를 구함

print(word_count1)                      # 3이 출력됨
print(word_count2)                      # 2가 출력됨
print(word_count3)                      # 8이 출력됨
