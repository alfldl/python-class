# datetime의 각 날짜와 시간에 관련된 항목값에 접근하려면 timetuple 메서드를 사용
import datetime

now = datetime.datetime.now()
nowTuple1 = now.timetuple()
#nowTuple.(tm_year=2018, tm_mon=9, tm_mday=28, tm_hour=14, tm_min=15, tm_sec=40, tm_wday=6, tm_yday=109, tm_isdst=-1)

print('nowTuple1->', nowTuple1)
print('nowTuple1.tm_year->', nowTuple1.tm_year)
