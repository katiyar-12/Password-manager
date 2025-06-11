# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    messagebox.showinfo(title="clipboard",message=f"password copied to clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write() :
    with open("data.txt", "a+") as file:
        email = email_entry.get()
        password = password_entry.get()
        website = website_entry.get()

        if len(email) == 0 or len(password) == 0 or len(website) == 0 :
            messagebox.showinfo(title="Error", message="Do not leave any fields Empty")

        else :
            is_ok = messagebox.askokcancel(title=website,
                                           message=f"Details\nEmail : {email}\nPassword : {password}\n\nPress OK to Save")
            if is_ok:
                file.write(f"{website} | {email} | {password}\n")
                reset()
            else:
                reset()



def reset() :
    password_entry.delete(0,END)
    website_entry.delete(0,END)
    email_entry.delete(0,END)
    email_entry.insert(0,DEFAULT_EMAIL)
    website_entry.focus()





# ---------------------------- UI SETUP ------------------------------- #
DEFAULT_EMAIL = "katiyar@gmail.com"

my_window = Tk()
my_window.title("Password Manager")
my_window.config(pady=50,padx=50)

my_canvas = Canvas(my_window,height=200,width=200)
image = PhotoImage(file="logo.png")
my_canvas.create_image(100,100,image=image)
my_canvas.grid(row=0,column=1)
my_canvas.grid(row=0,column=1)
my_canvas.image = image

website_label = Label(text="Website:",font=("Arial",10,"bold"))
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:",font=("Arial",10,"bold"))
email_label.grid(row=2,column=0)

password_label = Label(text="Password:",font=("Arial",10,"bold"))
password_label.grid(row=3,column=0)


website_entry = Entry(my_window ,width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry = Entry(my_window,width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,DEFAULT_EMAIL)

password_entry = Entry(my_window,width=35)
password_entry.grid(row=3,column=1,columnspan=2)

generate_button = Button(text="Generate Password",width=21,command=generate_password)
generate_button.grid(row=4,column=1)

add_button = Button(text="Add",width=14,command=write)
add_button.grid(row=4,column=2)














my_window.mainloop()