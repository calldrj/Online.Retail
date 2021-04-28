import mysql.connector
from mysql.connector import Error

# Fill in the database you want to work on
working_database = 'Retail'

# Fill in your mySQL root pass
my_password = '*****'

def validateLogin(username, password):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database=working_database,
                                             user='root',
                                             password=my_password)
        if connection.is_connected():
            cursor = connection.cursor(buffered=True)
            cursor.execute('select database();')
        
            """ Queries to find Buyer ID and the Cart associated with the buyer """
            q = "SELECT buyer_ID FROM buyers \
                WHERE login_ID = '{}' AND passw = '{}'".\
                format(username.get(), password.get())
            cursor.execute(q)
            if cursor.rowcount == 1:
                buyer_id = cursor.fetchall()[0][0]
                print('Buyer ID:', buyer_id)
                q = "SELECT item_ID FROM cart \
                    WHERE buyer_ID = '{}'".format(buyer_id)
                cursor.execute(q)
                item_IDs = [x[0] for x in cursor.fetchall()]
                print('Item IDs found in Cart:', item_IDs)  
            else:
                print('Buyer ID  not found! Please enter ID and password or hit Register')
            
    except Error as e:
        print('Error while connecting to MySQL', e)

    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            
    return