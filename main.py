from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

generate_pw_button = Button(text="Generate Password")
generate_pw_button.grid(row=3, column=2, sticky="ew")

# Add
add_button = Button(text="Add")
add_button.grid(row=4, column=1, columnspan=2, sticky="we")


canvas.mainloop()
