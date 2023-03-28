from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = ''.join(password_list)
    pw_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    get_email = email_entry.get()
    get_website = website_entry.get()
    get_pw = pw_entry.get()
    new_data = {
        get_website:{
            "email": get_email,
            "password": get_pw,
        }
    }

    if len(get_pw) == 0 or len(get_website)==0:
        messagebox.showwarning(title="Oops", message="You left some field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pw_entry.delete(0, END)

#------------------------------Find PW--------------------------------#

def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data_list = [key for key in data]
    except FileNotFoundError:
        print("No Data File Found")
    else:
        if website in data_list:
            messagebox.showinfo(title=website,
                                   message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title=website, message="No details for the website exists")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(width=200, height=200, padx=20, pady=20)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1,row=0)

label_website = Label(text="Website: ")
website_entry = Entry(width=35)
website_entry.focus()
label_website.grid(column=0, row=1)
website_entry.grid(column=1, row=1)
website_button = Button(text="Search", width=15, command=find_password)
website_button.grid(column=2, row=1)


label_email = Label(text="Email/Username: ")
email_entry = Entry(width=54)
email_entry.insert(index=0, string="piromi.ishikawa@gmail.com")
label_email.grid(column=0, row=2)
email_entry.grid(column=1, row=2, columnspan=2)

label_pw = Label(text="Password: ")
pw_entry = Entry(width=35)
button_pw = Button(text="Generate Password", command=generate_password)
label_pw.grid(column=0, row=3)
pw_entry.grid(column=1, row=3)
button_pw.grid(column=2, row=3)

button_add = Button(text="Add", width=46, command=save_info)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()