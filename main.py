from tkinter import *
from functools import partial
import login

UserName = ''
BuyerID = -1
Cart = {}
root = Tk()

def register_page(root):
    page = Frame(root)
    page.grid()
    title_lbl = Label(root, text="Registration page").grid(row=0, column=0, columnspan=2, pady=5)
    f_name_lbl = Label(root, text="First name: ").grid(row=1, column=0, padx=30)
    f_name_entry = Entry(root).grid(row=1,column=1)

    last_name_lbl = Label(root, text="Last name: ").grid(row=2, column=0)
    last_name_entry = Entry(root).grid(row=2, column=1, pady=10)

    login_id_lbl = Label(root, text="Login ID: ").grid(row=3, column=0)
    login_id_entry = Entry(root).grid(row=3, column=1, pady=10)

    password_lbl = Label(root, text="Password: ").grid(row=4, column=0)
    password_entry = Entry(root).grid(row=4, column=1, pady=10)

    next_button = Button(root, text="Next", width=10).grid(row=5,column=1)
    back_button = Button(root, text="Back", width=10, command=change_to_login_page).grid(row=5, column=0)

def change_to_reg_page():
    for widget in root.winfo_children():
        widget.destroy()
    register_page(root)


def login_page(root):
    welcome_lbl = Label(root, text="Welcome, please login").pack(pady=10)

    """ Login """
    username = StringVar()
    usr_name_box = Entry(root, textvariable=username).pack(pady=5)

    password = StringVar()
    password_box = Entry(root, textvariable=password, show='*').pack(pady=5)
   
    validateLogin = partial(login.validateLogin, username, password)
    login_button = Button(root, text="Login", command=validateLogin).pack(pady=5)

    reg_button = Button(root, text="Register", command=change_to_reg_page).pack(pady=5)

    root.geometry("300x300")


def change_to_login_page():
    for widget in root.winfo_children():
        widget.destroy()
    login_page(root)


def main():
    login_page(root)
    print('Global Cart:', Cart)
    root.mainloop()

if __name__ == "__main__":
    main()