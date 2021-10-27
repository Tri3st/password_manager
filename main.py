import json
import tkinter.messagebox
from tkinter import *
from password_generator import PasswordGenerator

my_data = []


def save_data():
    global my_data
    with open("./data/pwfile.json", "w") as json_file:
        json.dump(my_data, json_file, indent=4)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    generated_password = PasswordGenerator(2, 8, 2)
    passw = generated_password.get_pass()
    input_password.delete(first=0, last=len(input_password.get()))
    input_password.insert(index=0, string=passw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def validate_website(website_string):
    if not (4 < len(website_string) < 50):
        return False
    return True


def validate_email(email_string):
    if not (2 < len(email_string) < 50):
        return False
    return True


def validate_password(password_string):
    if not (6 < len(password_string) < 20):
        return False
    return True


def add_info():
    global my_data
    while True:
        unvalidated_website = input_website.get()
        if validate_website(unvalidated_website):
            validated_website = unvalidated_website
            break
        else:
            input_website.delete(first=0, last=END)
            tkinter.messagebox.showerror("ERROR!", "INVALID WEBSITE FORMAT")

    unvalidated_email = input_username.get()
    if validate_email(unvalidated_email):
        validated_email = unvalidated_email
    else:
        validated_email = "INVALID EMAIL FORMAT"
    unvalidated_password = input_password.get()
    if validate_password(unvalidated_password):
        validated_password = unvalidated_password
    else:
        validated_password = "INVALID PASSWORD FORMAT"
    data_dict = {"website": validated_website, "email": validated_email, "password": validated_password}
    input_website.delete(first=0, last=END)
    my_data.append(data_dict)
    save_data()


def search_website():
    pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.maxsize(width=600, height=800)

canvas = Canvas(height=300, width=400, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
my_logo = canvas.create_image(100, 100, image=lock_img)
canvas.move(my_logo, 100, 0)
canvas.grid(row=0, column=0, columnspan=3)

# website
label1 = Label(text="Website")
label1.grid(row=1, column=0, sticky="e")

input_website = Entry(width=40)
input_website.grid(row=1, column=1)

search_button = Button(text="Search")
search_button.grid(row=1, column=2, sticky="ew")

# email/username
label2 = Label(text="Email/Username")
label2.grid(row=2, column=0, sticky="e")

input_username = Entry(width=60)
input_username.grid(row=2, column=1, columnspan=2)

# password
label3 = Label(text="Password")
label3.grid(row=3, column=0, sticky="e")

input_password = Entry(width=40)
input_password.grid(row=3, column=1)

generate_pw_button = Button(text="Generate Password", command=generate_random_password)
generate_pw_button.grid(row=3, column=2, sticky="ew")

# Add
add_button = Button(text="Add", command=add_info)
add_button.grid(row=4, column=1, columnspan=2, sticky="we")

with open("./data/pwfile.json", "r") as data_file:
    my_data = json.load(data_file)


canvas.mainloop()
