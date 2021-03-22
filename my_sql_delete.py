# import streamlit as st
# import mysql.connector
# from mysql.connector import Error

# import numpy as numpy
# import pandas as pd 

# import json

# def my_sql_delete() :


#     # 화면에 보여주기
#     column_list = ['title', 'author_fname', 'author_lname', 'released_year', 'stock_quantity', 'pages']

#     selected_column_list = st.multiselect('컬럼을 선택하세요', column_list)  # 유저가 선택한게 셀렉트 컬럼리스트에 들어갈것이다

#     if len(selected_column_list) == 0 :
    
#         query = """select * from books;"""
#     else :
#         column_str =  ','.join(selected_column_list)  # 이것 하면  내 리스트가 ['title', 'book'] 일때 결과가 'title', 'book' 라고 뜬다 
#         #print(cloumn_str)
#         query = "select book_id, " + column_str + ' from books;'   # Unknown column 'book_id' in 'field list' 이 에러 나는건
#         #print(query)                                              # 우리가 쿼리문 쓸때 select  (colunm_str)  from books; 이렇게 가져와야하는데 
#                                                                    # 띄어쓰기 가 들어가지 않으면 형식이 맞지 않아 쓸수 없다
#     try :
#         # 1. 커넉터로부터 커넥션을 받는다.
#         connection = mysql.connector.connect(
#             host = 'database-1.cyfvtkkh7ho8.us-east-2.rds.amazonaws.com',
#             database = 'yhDB',
#             user = 'streamlit',
#             password = 'yh1234'
#         )
        
#         if connection.is_connected() :
#             cursor = connection.cursor(dictionary=True)

#         # 2. 쿼리 만들어서 실행
#         cursor.execute(query)
            
#         # 3. select 이므로, fetchall 한다
#         results =  cursor.fetchall()
        
#         # 파이썬의 리스트 + 딕셔너리 조합을 =>> json 형식으로 바꾸는것  해보면 " " 큰따옴표로 되어 딕셔너리 형태로 나온다 
#         json_results = json.dumps(results)  


#         # 판다스의 데이터 프레임으로 읽기 

#         df = pd.read_json(json_results)
        
#         st.dataframe(df)

            

                

        
#     except Error as e :
#         print('디비 관련 에러 발생', e)
    
#     finally :
#         # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
#         #    커서와 커넥션을 모두 닫아준다.
#         cursor.close()
#         connection.close()
#         print("MySQL 커넥션 종료")
