# 딕셔너리 형식 가변 매개변수
# 매개변수 앞에 **를 붙이면 딕셔너리 가변 매개변수가 됩니다.

# 함수 정의
def print_team(**players):
    i = 0
    for k in players.keys():
        i=i+1
        print('{0}={1} {2}'.format(k, players[k], i))
        
        
# 함수 호출
#players= {'조현우':'GK', '손흥민':'FW', '기성룡':'MF','박주호':'DF' }
#print_team(players)
print_team(조현우='GK', 손흥민='FW', 기성룡='MF', 박주호='DF')
