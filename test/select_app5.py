import streamlit as st 
import mysql.connector
from mysql.connector import Error
import os
from datetime import datetime, date, time 
                     # 여기 데이트 타임에 컴바인이 들어있음

# books table 사용한 앱

# 조회 버튼 위에, 체크박스 만들기
# 체크박스 안누르면 출판년도 오름차순
# 체크박스 선택 되면 출판년도 내림차순
# 화면에 보이도록 한다


# 여긴 오류남 
def main() :
    st.title('books table')
    
    st.subheader('몇년도 이후, 몇 페이지 이상 되는 책을 검색하고 싶으싶니까?')
    released_year = st.number_input('연도 입력', min_value= 1800, max_value= 2050)  # 유저한테 입력 받을 수 있도록 

    pages = st.number_input('페이지 수 입력', min_value= 10)

    order = 'asc'  # 아무것도 안누르면 asc로 정렬
    if st.checkbox('오름차순 / 내림차순') :
        order = 'desc'  # 체크박스 누르면 이렇게 해라 

    if st.button('조회') : 

        try :
            # 1. 커넉터로 부터 커넥션을 받는다.
            connection = mysql.connector.connect(
                host = 'database-1.cyfvtkkh7ho8.us-east-2.rds.amazonaws.com',  # 아이피주소 써도됨
                database = 'yhDB',
                user =  'streamlit',
                password = 'yh1234'
            )

            if connection.is_connected() :  # 해당 커넥션이 뎐결되어있냐? 
                db_info = connection.get_server_info()
                print("MySQL server version : ", db_info)

                # 2. 커서를 가져온다.              # 되어있으면 커서를 가져온다
                cursor = connection.cursor()

                # 3. 우리가 원하는 거 실행 가능. (쿼리문)
                                                    

                query = """select * from books;"""
                
                print( "{}개 적용됨".format(cursor.rowcount) )  # 저장하고나서 우리가 보기 편하게 디버깅용으로 이렇게 나타내라 

                # 4. 실행 후 커서에서 결과를 빼낸다
                
               
                
                cursor = connection.cursor(dictionary= True)  # 이렇게하면 키:밸류 처럼 딕셔너리 형식으로 나온다
                
                if order = 'asc' :

                    query = """select title, released_year, pages
                            from books
                            where released_year > %s and pages > %s
                            order by released_year asc ;"""

                else :
                    query = """select title, released_year, pages
                            from books
                            where released_year > %s and pages > %s
                            order by released_year desc ;"""
                
                param = ( released_year, pages)


                cursor.execute(query, param)
                results = cursor.fetchall()    

                for data in results :
                    print( data['title'], data['released_year'] )
                    st.write(data)


        except Error as e :
            print('디비 관련 에러 발생', e)

        finally :
            # 5.  모든 데이터베이스 실행 명령을 전부 끝냈으면,
            #     커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print("MySQL 커넥션 종료")






if __name__ == '__main__' :
    print(__name__)   # 네임이 뭔지 알수 있음
    main()