#dictionary.py

a = {'A':90, 'B':80, 'C':70, "D":75}
print(a)
result = a.pop('B')
print(a)            # {'A':90, 'C':70, "D":75} 이 출력
print(result)       # 80 출력