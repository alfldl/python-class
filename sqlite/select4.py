import sqlite3  # SQLite3 탑재
 # 쪽수 많은 책 조회용 함수
def find_big_books():
    conn = sqlite3.connect('my_books.db')         # 데이터베이스 커넥션 생성
    cur = conn.cursor()                             # 커서 확보
    # 조회용 SQL 실행 (300 쪽이 넘는 책의 제목과 쪽수를 출력하라)
    cur.execute('SELECT title, pages FROM my_books WHERE pages > 300')
    print('[4] 페이지 많은 책 출력하기')
    books = cur.fetchall()                          # 조회한 데이터 불러오기

    for book in books:                              # 데이터 출력하기
        print(book)
        #print(book['title'])
    conn.close()                                    # 커넥션 닫기

if __name__ == "__main__":		                # 외부에서 호출 시
    find_big_books()                                # 쪽수 많은 책 조회용 함수 호출
    print('=============================================')