import mysql.connector
from mysql.connector import Error

# Fill in the database you want to work on
working_database = 'Retail'

# Fill in your mySQL root pass
mysql_password = 'dinh9Thuan'

try:
    connection = mysql.connector.connect(host='localhost',
                                         database=working_database,
                                         user='root',
                                         password=mysql_password)
    if connection.is_connected():
        db_info = connection.get_server_info()
        print('Connected to MySQL Server version ', db_info)
        cursor = connection.cursor()
        
        cursor.execute('select database();')
        record = cursor.fetchone()
        print('Connected to database: ', record)
        
        cursor.execute('show tables;')
        tables = cursor.fetchall()
        print('Tables in {} schema: {}'.format(working_database, tables))

except Error as e:
    print('Error while connecting to MySQL', e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print('\n', '* ' * 58, '\n')
        print('MySQL connection is closed.')