import streamlit as st 
import mysql.connector
from mysql.connector import Error
import os
from datetime import datetime, date, time 
                     # 여기 데이트 타임에 컴바인이 들어있음
# 화면에서 유저한테  시, 분, 초, 날짜  받아서  저장 버튼 누르면 DB에 저장 하게 
# date_input , time_input 사용

# cats4 table 사용한 앱

def main() :
    st.title('cats4 table')
    
   

    if st.button('저장') : 

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
               
                                                
                query = """select * from books;"""   # 내가 실행 시키고 싶은 쿼리는 워크밴치에서 먼저 실행을 시켜보고 가져와야해 

                                                            

                cursor.execute(query)
                # connection.commit()    # 메모리에 반영이 아니라 데이터베이스에 반영해라 라는 커밋 이고 셀렉트는 이게 필요없다 
                print( "{}개 적용됨".format(cursor.rowcount) )  # 저장하고나서 우리가 보기 편하게 디버깅용으로 이렇게 나타내라 

                # 4. 실행 후 커서에서 결과를 빼낸다
                # record = cursor.fetchone()   커밋하는건 결과를 셀렉트 해오는게아니라서 이 코드가 필요없다
                # print('Connected to db : ', record)

    


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