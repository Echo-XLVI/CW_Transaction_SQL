import psycopg2
import re

def transaction(queries:list):
    conn=psycopg2.connect(host='localhost',port='5648',database='manufacturing',user='postgres',password='1380ACreZA46')
    cursor=conn.cursor()

    result={}

    try:
        for query in queries:
            if re.match(r'^[Ss][Ee][Ll][Ee][Cc][Tt]',query):
                cursor.execute(query)
                result[query]=cursor.fetchall()
            else:
                cursor.execute(query)
            conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

queries=["update inventory set body=body-1,wheel=wheel-1 ","update production set bicycle_count=bicycle_count+1"]

transaction(queries)