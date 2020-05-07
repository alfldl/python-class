import sqlite3  # SQLite3 탑재
# 일부 조회용 함수
def select_some_books(number):
    conn = sqlite3.connect('my_books.db')         # 데이터베이스 커넥션 생성
    cur = conn.cursor()                             # 커서 확보
    cur.execute('SELECT * FROM my_books')       # 조회용 SQL 실행
    print('[2] 데이터 일부 출력하기')
    books = cur.fetchmany(number)                   # 조회한 데이터 일부 불러오기

    for book in books:                             # 데이터 출력하기
        print(book)

    conn.close()                                    # 커넥션 닫기

if __name__ == "__main__":		                # 외부에서 호출 시
    select_some_books(3)                            # 일부 조회용 함수 호출
    print('=============================================')
