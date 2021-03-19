# 데이터베이스 안에 있는 내용을 바꾸는 것이기 때문에 커밋이 있어야 함 

# 딕셔너리로 가져올 필요없이 커서를 가져온다 

import streamlit as st
import mysql.connector
from mysql.connector import Error




def main() :

    try :  # 셀렉트해서 화면에 보여주게 
        # 1. 커넉터로부터 커넥션을 받는다.
        connection = mysql.connector.connect(
            host = 'database-1.cyfvtkkh7ho8.us-east-2.rds.amazonaws.com',
            database = 'yhDB',
            user = 'streamlit',
            password = 'yh1234'
        )

        if connection.is_connected() :
            cursor = connection.cursor(dictionary= True) # 딕셔너리형태로 가져와라
            query = """ select *
                        from books limit  5; """

            cursor.execute(query)
            results = cursor.fetchall()
            for row in results :
                st.write(row) 


    except Error as e :

                print('디비 관련 에러 발생', e)
            
    finally :
        # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
        #    커서와 커넥션을 모두 닫아준다.
        cursor.close()
        connection.close()
        print("MySQL 커넥션 종료")

    book_id = st.number_input('책 아이디 입력', min_value= book_id_list[0],
                                                max_value= book_id_list[-1])

    stock_quantity = st.number_input('수량 입력', min_value=0)
    

    #유저한테 입력받을 변수 저장
    # book_id_list = []

    for row in results :
        st.write(row)
        book_id_list.append()


    if st.button('실행') :

        try :
                # 1. 커넉터로부터 커넥션을 받는다.
                connection = mysql.connector.connect(
                    host = 'database-1.cyfvtkkh7ho8.us-east-2.rds.amazonaws.com',
                    database = 'yhDB',
                    user = 'streamlit',
                    password = 'yh1234'
                )
                
                if connection.is_connected() :
                    
                    # 2. 커서를 가져온다.
                    cursor = connection.cursor()

                    # 3. 우리가 원하는거 실행 가능.   
                    query = """update books
                                set pages = %s, stock_quantity = %s
                                 where book_id = %s;"""         
                                           
                    data = ( pages, stock_quantity, book_id  ) # ( pages,  )이렇게 써야지 튜플 형식
                                        # 아까는 인서트하는 거였고 이건 데이터 업데이트라 데이터라고 변수를  지정해야 보기 편함
                    cursor.execute( query, data )

                    connection.commit()

        except Error as e :

            print('디비 관련 에러 발생', e)
        
        finally :
            # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
            #    커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print("MySQL 커넥션 종료")

        




if __name__ == '__main__' :
    main()