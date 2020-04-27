import sqlite3  # SQLite3 탑재
#  1개 조회용 함수
def select_one_book():
    conn = sqlite3.connect('my_books.db')     # 데이터베이스 커넥션 생성
    cur = conn.cursor()                        # 커서 확보

    cur.execute('SELECT * FROM my_books')    # 조회용 SQL 실행
    print('[3] 1개 데이터 출력하기')
    print(cur.fetchone())                      # 데이터 한개 출력하기
    conn.close()                               # 커넥션 닫기

if __name__ == "__main__":		               # 외부에서 호출 시
    select_one_book()                          # 1개 조회용 함수 호출
    print('=============================================')
