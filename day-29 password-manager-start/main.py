from tkinter import *
from tkinter import messagebox
import password_generator as pwdGen
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = pwdGen.generate_password()
    print(password)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        is_empty = messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0,END)
            email_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, width=200, height= 200)

canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "cchen.co@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_generate_btn = Button(text="Generate Password", command=generate_password, highlightthickness=0)
password_generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save_info)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()