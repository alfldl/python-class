# datetime에서 datetime을 빼면 timedelta 값
import datetime

now = datetime.datetime.now()
Datetime1 = datetime.datetime.strptime('2019-11-13 01:00:00', '%Y-%m-%d %H:%M:%S')
Datetime2 = datetime.datetime.strptime('2019-11-12 00:00:00', '%Y-%m-%d %H:%M:%S')
result = Datetime1 - Datetime2
nowresult = now - Datetime2
print(result)  # 1 day, 0:00:10
print(result.days)  # 1
print('result.seconds->', result.seconds)  # 시간 단위까지의 초 단위로 보여줌
print('result.total_seconds()->', result.total_seconds())  # 전체일자 포함 초 단위로 보여줌

print('now + Datetime2 : nowresult->', nowresult)  # 1 day, 0:00:10
