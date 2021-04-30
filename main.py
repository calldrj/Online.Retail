from tkinter import *
from functools import partial
import mysql.connector
from mysql.connector import Error

# Fill in the database you want to work on
working_database = 'Retail'

# Fill in your mySQL root pass
my_password = '*****'

buyer, id, cart = '', -1, {}
root = Tk()

""" HOME PAGE """
def home_page(root, buyer, id):
    page = Frame(root)
    page.grid()
    
    guest = buyer if len(buyer) > 0 else 'Guest. You have not logged in'
    w = Label(root, text='Welcome, {}.'.format(guest))
    w.grid(row=0, column=1)

    shop_button = Button(root, text="Shop", width=15, height=5,bg='#bce5ec').grid(row=1, column=0 , pady=30, padx=25)
    
    if len(buyer) > 0:
        guest = ''
        go_home = partial(change_to_home_page, guest, id)
        logout_button = Button(root, text="Logout", width=15, height =5, bg='#ecbcbc',command=go_home).grid(row=1, column=1)
        
        acct_setting = partial(change_to_account_setting, buyer, id)
        acc_Setting_button = Button(root, text="Account Settings", width=15 , height =5, bg='#ebecbc', command=acct_setting).grid(row=2, column=0)

        checkout_button = Button(root, text="Checkout", width=15, height=5,bg='#bcecd5').grid(row=2, column=1)
    else:
        login_button = Button(root, text="Login", width=15, height =5, bg='#ecbcbc',command=change_to_login_page).grid(row=1, column=1)
    root.geometry("600x600")

def change_to_home_page(buyer, id):
    for widget in root.winfo_children():
        widget.destroy()
    home_page(root, buyer, id)

###############################################

""" LOGIN PAGE """
def login_page(root, buyer, id):
    welcome_lbl = Label(root, text="Welcome, please login").pack(pady=10)

    """ Login """
    username = StringVar()
    usr_name_box = Entry(root, textvariable=username).pack(pady=5)

    password = StringVar()
    password_box = Entry(root, textvariable=password, show='*').pack(pady=5)

    validate = partial(validateLogin, username, password)
    login_button = Button(root, text="Login", command=validate).pack(pady=5)

    reg_button = Button(root, text="Register", command=change_to_reg_page).pack(pady=5)

    go_home = partial(change_to_home_page, buyer, id)
    cancel_button = Button(root, text="Cancel", command=go_home).pack(pady=10)

    root.geometry("400x400")

def change_to_login_page():
    for widget in root.winfo_children():
        widget.destroy()
    login_page(root, buyer, id)

############################################

"""REGISTER PAGE """
def register_page(root):
    page = Frame(root)
    page.grid()
    title_lbl = Label(root, text="Registration page").grid(row=0, column=0, columnspan=2, pady=5)

    first_name = StringVar()
    f_name_lbl = Label(root, text="First name: ").grid(row=1, column=0, padx=30)
    f_name_entry = Entry(root, textvariable=first_name).grid(row=1, column=1)

    last_name = StringVar()
    last_name_lbl = Label(root, text="Last name: ").grid(row=2, column=0)
    last_name_entry = Entry(root, textvariable=last_name).grid(row=2, column=1, pady=10)

    login_ID = StringVar()
    login_id_lbl = Label(root, text="Login ID: ").grid(row=3, column=0)
    login_id_entry = Entry(root, textvariable=login_ID).grid(row=3, column=1, pady=10)

    password = StringVar()
    password_lbl = Label(root, text="Password: ").grid(row=4, column=0)
    password_entry = Entry(root, textvariable=password, show='*').grid(row=4, column=1, pady=10)

    bank_name = StringVar()
    bank_name_lbl = Label(root, text="Bank Name : ").grid(row=5, column=0)
    bank_name_entry = Entry(root, textvariable=bank_name).grid(row=5, column=1, pady=10)

    account_num = StringVar()
    account_number_lbl = Label(root, text="Account # : ").grid(row=6, column=0)
    account_number_entry = Entry(root, textvariable=account_num).grid(row=6, column=1, pady=10)

    zip_code_lbl = Label(root, text="Zip Code : ").grid(row=7, column=0)
    zip_code_entry = Entry(root).grid(row=7, column=1, pady=10)

    register = partial(buyer_info, first_name, last_name, login_ID, password, account_num, bank_name)
    submit_button = Button(root, text="Submit", width=10, command=register).grid(row=8, column=1,pady=10)
    back_button = Button(root, text="Cancel", width=10, command=change_to_login_page).grid(row=10, column=1)
    
    root.geometry("600x800")

def change_to_reg_page():
    for widget in root.winfo_children():
        widget.destroy()
    register_page(root)

##########################################
 
"""ACCOUNT SETTINGS PAGE """
def account_setting(root, buyer, id):
    page = Frame(root)
    page.grid()
    
    add_bank = partial(change_to_add_bank, buyer, id)
    add_bank_button = Button(root, text="Add Bank", width=15 , height =5,bg='#bce5ec',command=add_bank).grid(row=1, column=0, pady=30, padx=25)
    
    change_password_button = Button(root, text="Change Password", width=15 , height =5,bg='#bcecd5',command='').grid(row=1, column=1, pady=30, padx=25)
    
    go_home = partial(change_to_home_page, buyer, id)
    cancel_button = Button(root, text="Cancel", width=10, bg='#ebecbc', command=go_home).grid(row=2, column=1, pady=30)

def change_to_account_setting(buyer, id):
    for widget in root.winfo_children():
        widget.destroy()
    account_setting(root, buyer, id)

##########################################

"""ADD BANK INFO PAGE"""
def add_bank(root, buyer, id):
    page = Frame(root)
    page.grid()

    title_lbl = Label(root, text="                 Add Bank Information").grid(row = 0, columnspan=2 , pady=10 )

    bank = StringVar()
    bank_name_lbl = Label(root, text="Bank Name : ").grid(row=1, column=0)
    bank_name_entry = Entry(root, textvariable=bank).grid(row=1, column=1)

    acct_num = StringVar()
    account_number_lbl = Label(root, text="Account # : ").grid(row=2, column=0)
    account_number_entry = Entry(root, textvariable=acct_num).grid(row=2, column=1)

    zip = StringVar()
    zip_code_lbl = Label(root, text="Zip Code : ").grid(row=3, column=0)
    zip_code_entry = Entry(root, textvariable=zip).grid(row=3, column=1)

    submit_button = Button(root, text="Submit", width=10, command=bank_info).grid(row=5, column=1)
    acct_setting = partial(change_to_account_setting, buyer, id)
    cancel_button = Button(root, text="Cancel", width=10, command=acct_setting).grid(row=5, column=0)

def change_to_add_bank(buyer, id):
    for widget in root.winfo_children():
        widget.destroy()
    add_bank(root, buyer, id)

############################################2

""" CHANGE PASSWORD PAGE """
def change_password(root):
    page = Frame(root)
    page.grid()

    back_home_page_button = Button(root, text="Cancel", width=10,bg='#ebecbc',command=change_to_home_page).grid(row=0, column=0,pady=10)

    current_password_lbl = Label(root, text="Current Password : ").grid(row=1, column=0, sticky=E)
    current_password_entry = Entry(root).grid(row=1, column=1,pady=10,sticky=W)

    new_password_lbl = Label(root, text="New Password : ").grid(row=2, column=0 ,sticky=E)
    new_password_entry = Entry(root).grid(row=2, column=1, pady=10,sticky=W)

    confirm_new_password_lbl = Label(root, text="Confirm New Password : ").grid(row=3, column=0 ,sticky=E)
    confirm_new_password_entry = Entry(root).grid(row=3, column=1, pady=10,sticky=W)
    save_new_password_button = Button(root, text="Save ", width=30,bg='#ebecbc').grid(row=4, column=0,columnspan=4,padx=10,pady=10)

def change_to_change_password():
    for widget in root.winfo_children():
        widget.destroy()
    change_password(root)

###############################################

""" LOGIN VALIDATE FUNC """
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
                change_to_home_page(username.get(), buyer_id)
                print('Item IDs found in Cart:', item_IDs)  
            else:
                user, id = '', -1
                change_to_home_page(user, id)
            
    except Error as e:
        print('Error while connecting to MySQL', e)

    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()

###############################################

""" INSERT NEW BUYER INFO FUNC """           
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
                change_to_home_page(login_ID.get(), buyer_id)
            else:
                print('Buyer ID  not found! System Error.')
            
    except Error as e:
        print('Error while connecting to MySQL', e)

    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()

###############################################

""" ADD BANK INFO FUNC """       
def bank_info(first_name, last_name, login_ID, password, account_num, bank_name):
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
                change_to_home_page(login_ID, buyer_id)
            else:
                print('Buyer ID  not found! System Error.')
            
    except Error as e:
        print('Error while connecting to MySQL', e)

    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
                        
''' MAIN FUNC '''
def main():
    home_page(root, buyer, id)
    root.title("Online Retail")
    root.mainloop()

if __name__ == "__main__":
    main()