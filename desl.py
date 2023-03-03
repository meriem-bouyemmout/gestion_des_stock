from tkinter import *

def login():
    # Check if the username and password are correct
    if username_entry.get() == "admin" and password_entry.get() == "1234":
        # Clear the username and password fields
        username_entry.delete(0, END)
        password_entry.delete(0, END)

        # Close the login window
        login_window.destroy()

        # Open the options window
        options_window = Toplevel()
        options_window.title("Options")

        # Create some widgets for the options window
        option1_button = Button(options_window, text="Option 1")
        option1_button.pack()

        option2_button = Button(options_window, text="Option 2")
        option2_button.pack()

        option3_button = Button(options_window, text="Option 3")
        option3_button.pack()

        option4_button = Button(options_window, text="Option 4")
        option4_button.pack()

    else:
        # Show an error message if the username or password is incorrect
        error_label.config(text="Incorrect username or password")

# Create the login window
login_window = Tk()
login_window.title("Login")

# Create widgets for the login window
username_label = Label(login_window, text="Username:")
username_label.pack()

username_entry = Entry(login_window)
username_entry.pack()

password_label = Label(login_window, text="Password:")
password_label.pack()

password_entry = Entry(login_window, show="*")
password_entry.pack()

login_button = Button(login_window, text="Login", command=login)
login_button.pack()

error_label = Label(login_window, fg="red")
error_label.pack()

# Run the main loop
login_window.mainloop()
