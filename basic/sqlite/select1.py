import sqlite3  # SQLite3 탑재
# 전체 조회용 함수
def select_all_books():
    conn = sqlite3.connect('my_books.db')         # 데이터베이스 커넥션 생성
    cur = conn.cursor()                             # 커서 확보
    cur.execute('SELECT * FROM my_books')       # 조회용 SQL 실행

    print('[1] 전체 데이터 출력하기')
    books = cur.fetchall()                          # 조회한 데이터 불러오기

    for book in books:                              # 데이터 출력하기
        print(book)
    conn.close()                                    # 커넥션 닫기

if __name__ == "__main__":		                # 외부에서 호출 시
    select_all_books()                              # 전체 조회용 함수 호출
    print('=============================================')
