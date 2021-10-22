from tkinter import *
from password_generator import PasswordGenerator
from password import Password
import re

my_data = []


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    generated_password = PasswordGenerator(2, 8, 2)
    passw = generated_password.get_pass()
    input_password.delete(first=0, last=len(input_password.get()))
    input_password.insert(index=0, string=passw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def validate_website(website_string):
    site_pattern = r"^(https?://)?(\w+.)?\w+.(aero|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel|ac|ad|ae|af|ag|ai|al|am|an|ao|"+\
              "aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cu|cv|cx|cy|cz|cz|de|dj|dk|dm|"+\
              "do|dz|ec|ee|eg|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|"+\
              "je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mn|mn|mo|mp|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|n"+\
              "f|ng|ni|nl|no|np|nr|nu|nz|nom|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ra|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sj|sk|sl|sm|sn|so|sr|st|su|sv|sy|sz"+\
              "|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw|arpa)$"
    site = re.compile(site_pattern)
    if not (6 < len(website_string) < 50):
        return False
    return site.match(website_string) != None


def validate_email(email_string):
    if not (6 < len(email_string) < 50):
        return False
    mail_pattern = r"^(\w+.?\w*.?\w*)@\w+.(aero|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel|ac|ad|ae|af|ag|ai|al|am|an|ao|"+\
              "aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cu|cv|cx|cy|cz|cz|de|dj|dk|dm|"+\
              "do|dz|ec|ee|eg|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|"+\
              "je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mn|mn|mo|mp|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|n"+\
              "f|ng|ni|nl|no|np|nr|nu|nz|nom|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ra|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sj|sk|sl|sm|sn|so|sr|st|su|sv|sy|sz"+\
              "|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw|arpa)$"
    mail = re.compile(mail_pattern)
    return mail.match(email_string)


def validate_password(password_string):
    if not (6 < len(password_string) < 20):
        return False
    return True


def add_info():
    unvalidated_website = input_website.get()
    if validate_website(unvalidated_website):
        validated_website = unvalidated_website
    unvalidated_email = input_username.get()
    if validate_email(unvalidated_email):
        validated_email = unvalidated_email
    unvalidated_password = input_password.get()
    if validate_password(unvalidated_password):
        validated_password = unvalidated_password
    my_validated_info = Password()
    my_validated_info.set_all(validated_website, validated_email, validated_password)
    my_data.append(my_validated_info)
    print(my_data)
    print(my_validated_info)


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

canvas.mainloop()
