import mysql.connector
from mysql.connector import Error

# Fill in the database you want to work on
working_database = 'Retail'

# Fill in your mySQL root pass
my_password = '******'

def buyer_info(first_name, last_name, login_ID, password, account_num, bank_name):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database=working_database,
                                             user='root',
                                             password=my_password)
        if connection.is_connected():
            cursor = connection.cursor(buffered=True)
            cursor.execute('select database();')
        
            """ Queries to add a buyer's info from registration form into table buyers """
            q = "INSERT INTO buyers (first_name, last_name, login_ID, passw) \
                VALUES ('{}', '{}', '{}', '{}');".\
                format(first_name.get(), last_name.get(), login_ID.get(), password.get())
            cursor.execute(q)

            """ Queries to get buyer_ID from registration info to insert into table banks """
            q = "SELECT buyer_ID FROM buyers \
                WHERE login_ID = '{}' AND passw = '{}'".\
                format(login_ID.get(), password.get())
            cursor.execute(q)

            """ Queries to add the buyer's bank info from registration form into table banks """
            if cursor.rowcount == 1:
                buyer_id = cursor.fetchall()[0][0]
                print('Buyer ID:', buyer_id)
                q = "INSERT INTO banks (buyer_ID, account_num, bank_name) \
                    VALUES ('{}', '{}', '{}');".\
                    format(buyer_id, account_num.get(), bank_name.get())
                cursor.execute(q)
            else:
                print('Buyer ID  not found! System Error.')

    except Error as e:
        print('Error while connecting to MySQL', e)

    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            
            


    