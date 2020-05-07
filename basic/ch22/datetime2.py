from datetime import datetime

def main():
    theDateTime = datetime(2018 , 6, 25 , 12, 15, 8)
    # 날짜를 보기 좋은 포멧팅
    print('theDateTime1 ->', theDateTime.strftime('%Y/%m/%d %H:%M:%S'))
    print('theDateTime2 -> {}'.format(theDateTime.strftime('%Y/%m/%d %H:%M:%S')))
    print('theDateTime3 -> {}'.format(theDateTime.strftime('%I/%M %p')))

if __name__ == '__main__':
    main()
