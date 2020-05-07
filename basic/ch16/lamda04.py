print ("--------------------------------------------------------------------------------------------------------")
print ("--- 람다(lambda) 함수 정의  ->   2. 람다 함수 사용하기                                                     --")
print ("--- 람다 함수를 사용하는 코드 예제                                                                         --")
print ("--- 더하기, 빼기, 곱하기, 나누기에 해당하는 람다 함수 리스트 정의                                              --")
print ("--- 인덱스 0은 첫 번째 인자 / 인덱스 2는 세 번째 인자로 곱셈 수행 / 리스트의 원소에 람다함수가 들어가고, 검색도 가능  --")
print ("---------------------------------------------------------------------------------------------------------")
print
# 리스트의 원소가 람다함수로 들어감
func = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
def menu():
    print ("0. add" )
    print ("1. sub" )
    print ("2. mul" )
    print ("3. div" )
    print ("4. quit" )
    return input('Select menu:')

while 1:                             # while 1 → 무한 루프
    sel = int(menu())
    print("sel->",sel)
    print("len(func)->",len(func))
    if sel < 0 or sel > len(func):  # 0보다 작은 값이거나 4보다 큰 값(-1, -2, -3, 5, 6, 7, 8)은 수행 X
        continue
    if sel == len(func):
        break                     # 중간에 break 있어, 조건 미 충족 시 무한루프를 빠져나옴
    x = int(input('First operand:') )
    y = int(input('Second operand:') )
    print ('Result =', func[sel](x,y))
