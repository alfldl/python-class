#string1.py
pin = "881120-1068234"
# 없으면 처음부터 : 6 -> 미만의 문자열
#             start  End
yyyymmdd = pin[    : 6]
num = pin[7:]   # 7포함 끝까지 가라
print(yyyymmdd) # 881120 출력
print(num)      # 1068234 출력
