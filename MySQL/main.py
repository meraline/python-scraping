import pymysql
from MySQL.config import host,user,password,db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('Подключился....')
    
except  Exception as ex:
    print('Не подключаеться')
    print(ex)
    
