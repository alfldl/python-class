print("------------------------------------------------------------------------------")
print("--- 함수의 정의와 호출      :        2) 함수 객체와 함수 호출                     --")
print("--- . members → 리스트 반환  / newmember → 문자열 반환  / append 메소드 : 추가  --")
print("--- . members와 addmembers는 동일한 객체(리스트)를 가리킴                        --")
print("------------------------------------------------------------------------------")

# 함수 이름에 저장된 레퍼런스를 다른 변수에 할당하여 그 변수를 이용한 함수 호출 가능
def addmember(members, newmember):
    if newmember not in members:  # 기존 멤버가 아니면
        members.append(newmember)  # 추가


members = ['kang', 'choi', 'park', 'youn']  # 리스트에 초기 멤버 설정
addmember(members, 'jo')  # 새로운 멤버 추가
addmember(members, 'hwang')  # 새로운 멤버 추가
addmember(members, 'choi')  # (이미 존재하는) 새로운 멤버 추가
print("members->", members)
