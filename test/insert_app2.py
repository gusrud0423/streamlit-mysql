import streamlit as st 
import mysql.connector
from mysql.connector import Error
import os
from datetime import datetime, date, time 
                     # 여기 데이트 타임에 컴바인이 들어있음
# 화면에서 유저한테  시, 분, 초, 날짜  받아서  저장 버튼 누르면 DB에 저장 하게 
# date_input , time_input 사용

# people2 table 사용한 앱

def main() :
    st.title('people2 table')
    
    name = st.text_input('이름 입력')
    birth_date = st.date_input('생년월일')
    birth_time =  st.time_input('시간입력')

    birth_dt = datetime.combine(birth_date, birth_time)

    print(birth_date)
    print(birth_time)
    print(birth_dt)

    if st.button('저장') : 

        try :
            # 1. 커넉터로 부터 커넥션을 받는다.
            connection = mysql.connector.connect(
                host = 'database-1.cyfvtkkh7ho8.us-east-2.rds.amazonaws.com',
                database = 'yhDB',
                user =  'streamlit',
                password = 'yh1234'
            )

            if connection.is_connected() :
                db_info = connection.get_server_info()
                print("MySQL server version : ", db_info)

                # 2. 커서를 가져온다.
                cursor = connection.cursor()

                # 3. 우리가 원하는 거 실행 가능. (쿼리문)
                # cursor.execute('select database();')

            
                query = """insert into people2
                            values ( %s,%s,%s,%s);"""
                                                                        # 컴바인 쓰면 데이트랑 타임 합쳐서 볼수 있음
                record =  ( name, birth_date, birth_time, datetime.combine(birth_date, birth_time ) )
                print(datetime.now())

                cursor.execute(query,record)
                connection.commit()  
                print( "{}개 적용됨".format(cursor.rowcount) )

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