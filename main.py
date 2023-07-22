from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    [password_list.append(choice(letters)) for char in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for char in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    #read info
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    inf = f'{website} | {email} | {password}'

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Ooops', message='Some field in empty!')

    else:
        confimation = messagebox.askokcancel(title=website, message=f'Email: {email} \n'
                                                      f'Password: {password} \n'
                                                      f'Is correct?')
        if confimation:
            with open('data.txt', mode='a') as file:
                file.write(f'{inf} \n')

            messagebox.showinfo(title='Confirmation', message='Info saved')

            #clear
            website_entry.delete(0, 'end')
            user_entry.delete(0, 'end')
            user_entry.insert(0, 'jogartista@gmail.com')
            password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manajer')
window.config(pady=50, padx=50)

#Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1,row=0)

#LABELS------------------------------------------
#website label
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

#user label
user_label = Label(text='Email/Username:')
user_label.grid(column=0, row=2)

#password label
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

#ENTRYS------------------------------------------
#website entry
website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

#user entry
user_entry = Entry(width=51)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, 'jogartista@gmail.com')

#password entry
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

#BUTTONS------------------------------------------
#generate button
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3)

#add button
add_button = Button(text='Add', width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
