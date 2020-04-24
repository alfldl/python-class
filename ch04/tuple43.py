# tuple은 정의할때 괄호 붙이지 않아도 됨
colors = 'red', 'green', 'blue', 'yellow', 'orange'
print ('colors->', colors)
print ('colors len->', len(colors))
print ('colors->', colors)
# unpacking
a,b,c,d,e = colors
print ('a->', a)
print ('c->', c)

# 마지막 item 가져오기
the_last = colors[-1]
print ('the_last->', the_last)

# 마지막 item 가져오기 ->첫자 대문자
the_last = the_last.capitalize()
print ('the_last capitalize->', the_last)
