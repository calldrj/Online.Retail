from tkinter import *
from functools import partial
import mysql.connector
from mysql.connector import Error

# Fill in the database you want to work on
working_database = 'Retail'

# Fill in your mySQL root pass
mysql_password = 'dinh9Thuan'

buyer, id, cart, what = '', -1, {}, ''
root = Tk()

""" HOME PAGE """
def home_page(root, buyer, id):
    page = Frame(root)
    page.grid()
    
    guest = buyer if len(buyer) > 0 else 'Guest. You have not logged in'
    w = Label(root, text='Welcome, {}.'.format(guest))
    w.grid(row=0, column=1)

    go_shop = partial(go_shop_page, id)
    shop_button = Button(root, text="Shop", width=15, height=5,bg='#bce5ec', command=go_shop).grid(row=1, column=0 , pady=30, padx=25)
    
    if len(buyer) > 0:
        guest = ''
        go_home = partial(change_to_home_page, guest, id)
        logout_button = Button(root, text="Logout", width=15, height =5, bg='#ecbcbc', command=go_home).grid(row=1, column=1)
        
        acct_setting = partial(change_to_account_setting, buyer, id, what)
        acc_Setting_button = Button(root, text="Account Settings", width=15, height =5, bg='#ebecbc', command=acct_setting).grid(row=2, column=0)

        checkout_button = Button(root, text="Checkout", width=15, height=5, bg='#bcecd5').grid(row=2, column=1)
    else:
        login_button = Button(root, text="Login", width=15, height =5, bg='#ecbcbc', command=change_to_login_page).grid(row=1, column=1)
    root.geometry("600x600")

def change_to_home_page(buyer, id):
    for widget in root.winfo_children():
        widget.destroy()
    home_page(root, buyer, id)

###############################################

""" SHOP PAGE """
def shop_page(root, id):
    welcome_lbl = Label(root, text="Welcome to our product catalog!").grid(row=0, column=1, padx=20, pady=20)
    cat = Button(root, text='Category', width=15, height=2, bg='#bce5ec').grid(row=1, column=1, padx=20)
    dis = Button(root, text='Discount Percent', width=15, height=2, bg='#bce5ec').grid(row=1, column=2, padx=20)

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database=working_database,
                                             user='root',
                                             password=mysql_password)
        if connection.is_connected():
            cursor = connection.cursor(buffered=True)
            cursor.execute('select database();')
        
            """ Queries to find Buyer ID and the Cart associated with the buyer """
            q = "SELECT  category, disc_percent FROM disc_category;"
            cursor.execute(q)
            k = 2
            for row in cursor:
                cat = Button(root, text=row[0], width=15, height=2, bg='#bce5ec').grid(row=k, column=1, padx=20)
                dis = Button(root, text=row[1], width=15, height=2, bg='#bce5ec').grid(row=k, column=2, padx=20)
                k = k + 1

    except Error as e:
        print('Error while connecting to MySQL', e)

    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
    
    root.geometry("600x600")

def go_shop_page(id):
    for widget in root.winfo_children():
        widget.destroy()
    shop_page(root, id)

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
def account_setting(root, buyer, id, what):
    page = Frame(root)
    page.grid()

    if what == 'bank':
        w = Label(root, text='{}, you have successfully added your new bank account!.'.format(buyer))
    elif what == 'pass':
        w = Label(root, text='{}, you have successfully changed your password!.'.format(buyer))
    elif what == 'mismatched':
        w = Label(root, text='{}, your new and confirmed passwords mismatched!.'.format(buyer))
    elif what == 'failed':
        w = Label(root, text='{}, your current password incorrect!.'.format(buyer))
    else:
        w = Label(root, text='Welcome, {}.'.format(buyer))
    w.grid(row=0, column=1)

    add_bank = partial(change_to_add_bank, buyer, id)
    add_bank_button = Button(root, text="Add Bank", width=15 , height =5,bg='#bce5ec',command=add_bank).grid(row=1, column=0, pady=30, padx=25)
    
    change_pass = partial(change_to_change_password, buyer, id)
    change_password_button = Button(root, text="Change Password", width=15 , height =5,bg='#bcecd5',command=change_pass).grid(row=1, column=1, pady=30, padx=25)
    
    go_home = partial(change_to_home_page, buyer, id)
    cancel_button = Button(root, text="Cancel", width=10, bg='#ebecbc', command=go_home).grid(row=2, column=1, pady=30)

def change_to_account_setting(buyer, id, what):
    for widget in root.winfo_children():
        widget.destroy()
    account_setting(root, buyer, id, what)

##########################################

""" ADD BANK INFO PAGE """
def add_bank(root, buyer, id):
    page = Frame(root)
    page.grid()

    title_lbl = Label(root, text="                 Add Bank Information").grid(row = 0, columnspan=2 , pady=10 )

    bank = StringVar()
    bank_name_lbl = Label(root, text="Bank Name: ").grid(row=1, column=0)
    bank_name_entry = Entry(root, textvariable=bank).grid(row=1, column=1)

    acct_num = StringVar()
    account_number_lbl = Label(root, text="Account #: ").grid(row=2, column=0)
    account_number_entry = Entry(root, textvariable=acct_num).grid(row=2, column=1)

    add_bank = partial(bank_info, buyer, id,  bank, acct_num)
    submit_button = Button(root, text="Submit", width=10, command=add_bank).grid(row=5, column=1)
    
    acct_setting = partial(change_to_account_setting, buyer, id, '')
    cancel_button = Button(root, text="Cancel", width=10, command=acct_setting).grid(row=5, column=0)

def change_to_add_bank(buyer, id):
    for widget in root.winfo_children():
        widget.destroy()
    add_bank(root, buyer, id)

############################################2

""" CHANGE PASSWORD PAGE """
def change_password(root, buyer, id):
    page = Frame(root)
    page.grid()

    current = StringVar()
    current_password_lbl = Label(root, text="Current Password: ").grid(row=1, column=0, padx=10, sticky=E)
    current_password_entry = Entry(root, textvariable=current, show='*' ).grid(row=1, column=1, pady=10)

    new_pass = StringVar()
    new_password_lbl = Label(root, text="New Password: ").grid(row=2, column=0, padx=10, sticky=E)
    new_password_entry = Entry(root, textvariable=new_pass, show='*').grid(row=2, column=1, pady=10)

    confirmed = StringVar()
    confirm_new_password_lbl = Label(root, text="Confirm New Password: ").grid(row=3, column=0, padx=10, sticky=E)
    confirm_new_password_entry = Entry(root, textvariable=confirmed, show='*').grid(row=3, column=1, pady=10)
    
    save_new = partial(update_password, buyer, id, '', new_pass, confirmed, current)
    save_new_password_button = Button(root, text="Submit", width=10, bg='#ebecbc', command=save_new).grid(row=4, column=2, padx=10, pady=10)

    acct_setting = partial(change_to_account_setting, buyer, id, '')
    cancel_button = Button(root, text="Cancel", width=10, command=acct_setting).grid(row=5, column=2)

def change_to_change_password(buyer, id):
    for widget in root.winfo_children():
        widget.destroy()
    change_password(root, buyer, id)

###############################################

""" LOGIN VALIDATE FUNC """
def validateLogin(username, password):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database=working_database,
                                             user='root',
                                             password=mysql_password)
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
                q = "SELECT item_ID FROM cart \
                    WHERE buyer_ID = '{}'".format(buyer_id)
                cursor.execute(q)
                item_IDs = [x[0] for x in cursor.fetchall()]
                change_to_home_page(username.get(), buyer_id)
                print('Item IDs found in Cart:', item_IDs)  

                """ DEBUG CODE HERE """
                print('Buyer ID:', buyer_id)

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
                                             password=mysql_password)
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
                q = "INSERT INTO banks (buyer_ID, account_num, bank_name) \
                    VALUES ('{}', '{}', '{}');".\
                    format(buyer_id, account_num.get(), bank_name.get())
                cursor.execute(q)
                change_to_home_page(login_ID.get(), buyer_id)

                """ DEBUG CODE HERE """
                print('Buyer ID:', buyer_id)

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
def bank_info(buyer, id,  bank, acct_num):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database=working_database,
                                             user='root',
                                             password=mysql_password)
        if connection.is_connected():
            cursor = connection.cursor(buffered=True)
            cursor.execute('select database();')
        
            """ Queries to add the buyer's bank info from Add Bank form into table banks """
            q = "INSERT INTO banks (buyer_ID, account_num, bank_name) \
                    VALUES ('{}', '{}', '{}');".\
                    format(id, acct_num.get(), bank.get())
            cursor.execute(q)
            change_to_account_setting(buyer, id, 'bank')

            """ DEBUG CODE HERE """
            print('Buyer ID:', id)
                 
    except Error as e:
        print('Error while connecting to MySQL', e)

    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()


###############################################

""" UPDATE PASSWORD FUNC """       
def update_password(buyer, id, what, new_pass, confirmed, current):
    print(new_pass.get(), confirmed.get())
    if new_pass.get() != confirmed.get():
        change_to_account_setting(buyer, id, 'mismatched')
    else:
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database=working_database,
                                                user='root',
                                                password=mysql_password)
            if connection.is_connected():
                cursor = connection.cursor(buffered=True)
                cursor.execute('select database();')

                """ Queries to get the buyer's current password from buyer ID """
                q = "SELECT passw FROM buyers WHERE buyer_ID = '{}'".format(id)
                cursor.execute(q)
                if current.get() != cursor.fetchall()[0][0]:
                    change_to_account_setting(buyer, id, 'failed')
                else:

                    """ Queries to update the buyer's password """
                    q = "UPDATE buyers SET passw = '{}' WHERE buyer_ID = '{}';".format(new_pass.get(), id)
                    cursor.execute(q)
                    change_to_account_setting(buyer, id, 'pass')

                    """ DEBUG CODE HERE """
                    print('Buyer ID:', id)
                    print('New pass:', new_pass.get())
            
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