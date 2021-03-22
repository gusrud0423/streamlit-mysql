#  파이선 앱에서 커넥션을 연결한 상태에서 커서를 가지고있다 
# 딜리트 쿼리문을 넣는다 라이브러리가 데이터베이스에서 테이블을 삭제해주고 삭제된 테이블이 몇개 행인지 돌려보내준다
# 그리고 파이썬에서 커밋을 날리면 데이터베이스에 영구 저장 
# 셀렉트 문은 커밋이 없다
# 인서트 문은 커밋이 있다

# 딜리트 문, 업데이트 문, 인서트 문은 커밋이 있다 

# 메뉴를 만들어 그안에서 셀렉트ㅡ, 인서트  업데이트 딜리트 하기 


import streamlit as st
import mysql.connector
from mysql.connector import Error

from my_sql_select import my_sql_select

from my_sql_insert import my_sql_insert

# from my_sql_update import my_sql_update

# from my_sql_delete import my_sql_delete

def main():
    menu = ['Select', 'Insert', 'Update', 'Delete']  # 메뉴 카테고리
    choice = st.sidebar.selectbox('메뉴', menu)  # 메뉴를 표시해라
    

    if choice == 'Select' :
        my_sql_select()

    if choice ==  'Insert' :
        my_sql_insert()

    # if choice == 'Update' :
    #     my_sql_update()
    
    # if choice == 'Delete' :
    #     my_sql_delete()
    

if __name__ == '__main__' :
    main()