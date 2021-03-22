import streamlit as st
import mysql.connector
from mysql.connector import Error

import numpy as numpy
import pandas as pd 

import json

def my_sql_insert() :


    # 화면에 보여주기
    column_list = ['title', 'author_fname', 'author_lname', 'released_year', 'stock_quantity', 'pages']

    inserted_column_list = st.multiselect('컬럼을 선택하세요', column_list)  # 유저가 선택한게 셀렉트 컬럼리스트에 들어갈것이다

    # if st.button('저장') : 

    #     try :
    #         # 1. 커넉터로 부터 커넥션을 받는다.
    #         connection = mysql.connector.connect(
    #             host = 'database-1.cyfvtkkh7ho8.us-east-2.rds.amazonaws.com',
    #             database = 'yhDB',
    #             user =  'streamlit',
    #             password = 'yh1234'
    #         )

    #         if connection.is_connected() :
    #             db_info = connection.get_server_info()
    #             print("MySQL server version : ", db_info)

    #             # 2. 커서를 가져온다.
    #             cursor = connection.cursor()

    #             # 3. 우리가 원하는 거 실행 가능. (쿼리문)
    #             # cursor.execute('select database();')

            
    #             query = """insert into books ( title, author_fname, author_lname, released_year, stock_quantity, pages )
    #                         values ( %s,%s,%s,%s,%s,%s );"""

    #             record =  ( title, author_fname, author_lname, released_year, stock_quantity, pages )

    #             cursor.execute(query,record)
    #             connection.commit()  
    #             print( "{}개 적용됨".format(cursor.rowcount) )

    #             # 4. 실행 후 커서에서 결과를 빼낸다
    #             # record = cursor.fetchone()   커밋하는건 결과를 셀렉트 해오는게아니라서 이 코드가 필요없다
    #             # print('Connected to db : ', record)

    


    #     except Error as e :
    #         print('디비 관련 에러 발생', e)

    #     finally :
    #         # 5.  모든 데이터베이스 실행 명령을 전부 끝냈으면,
    #         #     커서와 커넥션을 모두 닫아준다.
    #         cursor.close()
    #         connection.close()
    #         print("MySQL 커넥션 종료")
