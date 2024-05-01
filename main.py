from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
#Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)



    password_list = ([choice(letters) for item in range(nr_letters)] +
                  ([choice(numbers) for item in range(nr_numbers)] +
                   [choice(symbols) for item in range(nr_symbols)]))

    shuffle(password_list)

    random_password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_credentials():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

#------------------------------SEARCH CREDENTIALS-------------------------#

def search_credentials():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            user_search = website_entry.get()
            user= data[user_search]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Error", message=f"No details of the {user_search} exists")
    else:
        messagebox.showinfo(title=f"{user_search}", message=f"Email: {user["email"]}\nPassword: {user["password"]}")


#---------------------------- UI SETUP ------------------------------- #
#Creating tkinter window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Creating Canvas and inserting image in that canvas
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entry
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=40,)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "madhavdahal4@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1,)

#Buttons
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(row=3, column=2)

add = Button(text="Add", width=34, command=store_credentials)
add.grid(row=4, column=1, columnspan=2)


search = Button(text="Search", command=search_credentials)
search.grid(row=1, column=2)















window.mainloop()