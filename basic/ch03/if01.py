#if문

n=int(input('숫자를 입력하세요?'))

if n > 0:
  print('{}는 양수입니다.'.format(n))

if n < 0:
    print('{}은 음수입니다'.format(n))

if True:
    print('항상 실행')