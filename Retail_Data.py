import mysql.connector
from mysql.connector import Error

# Fill in the database you want to work on
working_database = 'Retail'

# Fill in your mySQL root pass
mysql_password = '*****'

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
        
        
        """********** TABLE disc_category **********"""
        print('\n', '* ' * 58, '\n')
        print('TABLE disc_category:\n')
        # Read products info from a data file (DiscountCategory.csv) 
        disc_category = pd.read_csv('./retail/DiscountCategory.csv', header=None)
        
        # Generate an array of SQL's INSERT commands to add all entries in DiscountCategory.csv to Retail DB
        Q = ["INSERT INTO disc_category (category_ID, category, disc_percent) \
              VALUES ('{}', '{}', '{}');"\
             .format(f[0], f[1], f[2]) for f in disc_category.values]
        for q in Q:
            cursor.execute(q)
        
        """********** TABLE vendors **********"""
        print('\n', '* ' * 58, '\n')
        print('TABLE vendors:\n')
        # Read vendors info from a data file (Vendors.csv) 
        vendors = pd.read_csv('./retail/Vendors.csv', header=None)
        
        # Generate an array of SQL's INSERT commands to add all entries in Vendors.csv to Retail DB
        Q = ["INSERT INTO vendors (vendor_ID, phone, email) \
              VALUES ('{}', '{}', '{}');"\
             .format(f[0], f[1], f[2]) for f in vendors.values]
        for q in Q:
            cursor.execute(q)
        
        """********** TABLE products **********"""
        print('\n', '* ' * 58, '\n')
        print('TABLE products:\n')
        # Read products info from a data file (Products.csv) 
        products = pd.read_csv('./retail/Products.csv', header=None)
        
        # Generate an array of SQL's INSERT commands to add all entries in Products.csv to Retail DB
        Q = ["INSERT INTO products (product_name, category_ID, unit_price) \
              VALUES ('{}', '{}', '{}');"\
             .format(f[0], f[1], f[2]) for f in products.values]
        for q in Q:
            cursor.execute(q)
        
        """********** TABLE supply_stock **********"""
        print('\n', '* ' * 58, '\n')
        print('TABLE supply_stock:\n')
        # Read stocks info from a data file (SupplyStocks.csv) 
        stocks = pd.read_csv('./retail/SupplyStocks.csv', header=None)
        
        # Generate an array of SQL's INSERT commands to add all entries in SupplyStocks.csv to Retail DB
        Q = ["INSERT INTO supply_stock (vendor_ID, quantity) \
              VALUES ('{}', '{}');"\
             .format(f[0], f[1]) for f in stocks.values]
        for q in Q:
            cursor.execute(q)
      
        """********** TABLE buyers **********"""
        print('\n', '* ' * 58, '\n')
        print('TABLE buyers:\n')
        # Read buyers info from a data file (ClientInfo.csv) 
        client_info = pd.read_csv('./retail/ClientInfo.csv', header=None)
        
        # Generate an array of SQL's INSERT commands to add all entries in ClientInfo.csv to Retail DB
        Q = ["INSERT INTO buyers (first_name, last_name, login_ID, passw, phone, email, address) \
              VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');"\
             .format(f[0], f[1], f[2], f[3], f[4], f[5], f[6]) for f in client_info.values]
        for q in Q:
            cursor.execute(q)

except Error as e:
    print('Error while connecting to MySQL', e)

finally:
    if (connection.is_connected()):
        connection.commit()
        cursor.close()
        connection.close()
        print('\n', '* ' * 58, '\n')
        print('MySQL connection is closed.')