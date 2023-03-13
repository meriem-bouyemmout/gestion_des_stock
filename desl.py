from tkinter import *
from tkinter import ttk
import sqlite3




def article() :
    art = Toplevel()
    art.title("articles")

    # Créer le tableau
    table = ttk.Treeview(art, columns=("Id_article", "Code_comptable","Designation"))

    # Définir les en-têtes de colonnes
    table.heading("#0", text="ID")
    table.heading("Id_article", text="Id_article")
    table.heading("Code_comptable", text="Code_comptable")
    table.heading("Designation", text="Designation")


    conn = sqlite3.connect('classe.db')
    cur = conn.cursor()
    req = "select Id_aritcle from article"
    cur.execute(req)
    res = cur.fetchall()
    print(res)
    conn.commit()
    conn.close()

    

    for i in range(len(res)):
    # Supprimer l'élément existant avec le même identifiant
     table.delete(i)
    # Ajouter des données
     table.insert(parent="", index="end", iid=i, text=i+1, values=(res[i], 25, 15))
     table.insert(parent="", index="end", iid=i, text=i+2, values=(res[i], 30, 15))
     table.insert(parent="", index="end", iid=i, text=i+3, values=(res[i], 35, 15))
    

    # Afficher le tableau
    table.pack()



def year():
    ann = Toplevel()
    ann.title("activitée")
    listes_article = Button(ann, text="Liste d'articles",command=article, padx=50, pady=10)
    listes_article.pack(padx=40, pady=20)

    ajouter_article = Button(ann, text="Ajouter un article", padx=50, pady=10)
    ajouter_article.pack(padx=40, pady=20)

    mouvement = Button(ann, text="Mouvement", padx=50, pady=10)
    mouvement.pack(padx=40, pady=20)

    # Mettre à jour la géométrie de la fenêtre
    ann.update_idletasks()

    # Récupérer la largeur et la hauteur de la fenêtre
    width = ann.winfo_width()
    height = ann.winfo_height()

    # Récupérer la largeur et la hauteur de l'écran
    screen_width = ann.winfo_screenwidth()
    screen_height = ann.winfo_screenheight()

    # Calculer la position x et y pour centrer la fenêtre
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    # Définir la géométrie de la fenêtre centrée sur l'écran
    ann.wm_geometry("+{}+{}".format(x, y))

        
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
        option1_button = Button(options_window, text="2023",command=year, padx=50, pady=10)
        option1_button.pack(padx=40, pady=20)

        option2_button = Button(options_window, text="2022",command=year, padx=50, pady=10)
        option2_button.pack(padx=40, pady=20)

        option3_button = Button(options_window, text="2021",command=year, padx=50, pady=10)
        option3_button.pack(padx=40, pady=20)

        option4_button = Button(options_window, text="2020",command=year, padx=50, pady=10)
        option4_button.pack(padx=40, pady=20)



        # Mettre à jour la géométrie de la fenêtre
        options_window.update_idletasks()

        # Récupérer la largeur et la hauteur de la fenêtre
        width = options_window.winfo_width()
        height = options_window.winfo_height()

        # Récupérer la largeur et la hauteur de l'écran
        screen_width = options_window.winfo_screenwidth()
        screen_height = options_window.winfo_screenheight()

        # Calculer la position x et y pour centrer la fenêtre
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        # Définir la géométrie de la fenêtre centrée sur l'écran
        options_window.wm_geometry("+{}+{}".format(x, y))



    else:
        # Show an error message if the username or password is incorrect
        error_label.config(text="Incorrect username or password")





# Create the login window
login_window = Tk()
login_window.title("Login")
login_window.geometry("300x300")


# Create widgets for the login window
username_label = Label(login_window, text="Username:", font=("Times", 16, "bold"))
username_label.pack(pady=10)

username_entry = Entry(login_window)
username_entry.pack(pady=10)

password_label = Label(login_window, text="Password:", font=("Times", 16, "bold"))
password_label.pack(pady=10)

password_entry = Entry(login_window, show="*")
password_entry.pack(pady=10)

login_button = Button(login_window, text="Login", command=login, bg="white", font=("Arial", 14))
login_button.pack(padx=20, pady=20)

error_label = Label(login_window, fg="red")
error_label.pack()





# Mettre à jour la géométrie de la fenêtre
login_window.update_idletasks()

# Récupérer la largeur et la hauteur de la fenêtre
width = login_window.winfo_width()
height = login_window.winfo_height()

# Récupérer la largeur et la hauteur de l'écran
screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()

# Calculer la position x et y pour centrer la fenêtre
x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 2) - (height / 2))

# Définir la géométrie de la fenêtre centrée sur l'écran
login_window.wm_geometry("+{}+{}".format(x, y))





# Run the main loop
login_window.mainloop()
