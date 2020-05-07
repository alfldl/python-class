# 절대시간(epoch) 을 다루는 모듈
import time

def calc_prod():
    # calculate
    product = 1
    for i in range(1, 100000):
        product = product + i
    return product

def main():
    start = time.time()
    prod = calc_prod()
    end = time.time()
    print('Result-> {}'.format(str(prod)))
    print('calculate time {}'.format(end-start))


if __name__  == '__main__':
    main()