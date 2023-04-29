from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


def article() :
    art = Toplevel()
    art.title("articles")

    # Créer le tableau
    table = ttk.Treeview(art, columns=("Id_article", "Code_comptable","Designation"))

    # Définir les en-têtes de colonnes
    table.heading("#0", text="Num")
    table.heading("Id_article", text="Id_article")
    table.heading("Code_comptable", text="Code_comptable")
    table.heading("Designation", text="Designation")


    conn = sqlite3.connect('classe.db')
    cur = conn.cursor()
    req = "select Id_aritcle from article"
    req1 = "select code_comptable from article"
    req2 = "select designation from article"
    cur.execute(req)
    res = cur.fetchall()
    cur.execute(req1)
    res1 = cur.fetchall()
    cur.execute(req2)
    res2 = cur.fetchall()
    print(res)
    print(res1)
    print(res2)
    conn.commit()
    conn.close()



    for i in range(len(res)):
     table.insert(parent="", index="end", iid=i, text=str(i+1), values=(res[i], res1[i], res2[i]))
    
    

    # Afficher le tableau
    table.pack()



def ajouter():
    ajt = Toplevel()
    ajt.title("Ajouter article")
    
    global Id_article_entry,Code_comptable_entry,Designation_entry
   
    Id_article = Label(ajt, text="Id_article:", font=("Times", 16, "bold"))  
    Id_article.pack(pady=10)
 
    Id_article_entry = Entry(ajt)
    Id_article_entry.pack(pady=10)

    Code_comptable = Label(ajt, text="Code_comptable:", font=("Times", 16, "bold"))
    Code_comptable.pack(pady=10)

    Code_comptable_entry = Entry(ajt)
    Code_comptable_entry.pack(pady=10)

    Designation = Label(ajt, text="Designation", font=("Times", 16, "bold"))  
    Designation.pack(pady=10)
 
    Designation_entry = Entry(ajt)
    Designation_entry.pack(pady=10)

    bouton_ajouter = Button(ajt, text="Ajouter", command = ajouter_dans_bd)
    bouton_ajouter.pack(pady=10)

    boutton_annuler = Button(ajt, text="Annuler", command = annuler)
    boutton_annuler.pack()  


def ajouter_dans_bd():
    # Connexion à la base de données
    conn = sqlite3.connect('classe.db')
    cur = conn.cursor()

    # Récupération des valeurs des champs de saisie
    id_article = Id_article_entry.get()
    code_comptable = Code_comptable_entry.get()
    designation = Designation_entry.get()

    # Insertion des valeurs dans la base de données
    cur.execute("INSERT INTO article (Id_aritcle, code_comptable, designation) VALUES (?, ?, ?)", (id_article, code_comptable, designation))
    
    # Message de confirmation
    messagebox.showinfo("Ajouté", "L'article a été ajouté avec succès !")

    # Validation de la transaction et fermeture de la connexion
    conn.commit()
    conn.close()

def annuler():
    Id_article_entry.delete(0, END)
    Code_comptable_entry.delete(0, END)
    Designation_entry.delete(0, END)   


def num_BR():
    num_BR = Toplevel()
    num_BR.title("Numéro BR")
    global Numéro_entry
   
    Numéro = Label(num_BR, text="Donner un numéro BR", font=("Times", 16, "bold"))  
    Numéro.pack(pady=10)
 
    Numéro_entry = Entry(num_BR)
    Numéro_entry.pack(pady=10)
   
    OK = Button(num_BR, text="OK", command=BR, padx=50, pady=10)
    OK.pack()

def BR():
    BR = Toplevel()
    BR.title("BR")
    BR_label = Label(BR, text=Numéro_entry.get(), font=("Times", 16, "bold"))
    BR_label.pack()
    Numéro_entry.delete(0, END)

    # Créer le tableau
    global table2
    table2 = ttk.Treeview(BR, columns=("Id_article","Designation"))

    # Définir les en-têtes de colonnes
    table2.heading("Id_article", text="Id_article")
    table2.heading("Designation", text="Designation")

    # Afficher le tableau
    table2.pack()
    
    Ajouter_BR = Button(BR, text="Ajouter BR", command=ajouter_br)
    Ajouter_BR.pack()
    Enregistrer_BR = Button(BR, text="Valider", command=ajouter_BR_dansBD)
    Enregistrer_BR.pack()

def ajouter_br():
    ajt_BR = Toplevel()
    ajt_BR.title("Ajouter BR")
    
    global Id_article_entry,Designation_entry
   
    Id_article = Label(ajt_BR, text="Id_article:", font=("Times", 16, "bold"))  
    Id_article.pack(pady=10)
 
    Id_article_entry = Entry(ajt_BR)
    Id_article_entry.pack(pady=10)


    Designation = Label(ajt_BR, text="Designation", font=("Times", 16, "bold"))  
    Designation.pack(pady=10)
 
    Designation_entry = Entry(ajt_BR)
    Designation_entry.pack(pady=10)

    bouton_ajouter = Button(ajt_BR, text="Ajouter BR", command=Entrer_table)
    bouton_ajouter.pack(pady=10)

def Entrer_table():

    # Ajouter les valeurs entrées à table2
    table2.insert(parent="", index="end", iid=None, text="", values=(Id_article_entry.get(), Designation_entry.get()))

    # Copier les valeurs de table2 dans res
    global ses
    ses = []
    for item in table2.get_children():
        ses.append(table2.item(item)['values'])


    # Effacer les entrées dans la fenêtre "Ajouter BR"
    Id_article_entry.delete(0, END)
    Designation_entry.delete(0, END)

def ajouter_BR_dansBD():
    # Connexion à la base de données
    conn = sqlite3.connect('classe.db')
    cur = conn.cursor()    
    
    for row in ses:
     id = row[0]
     des = row[1]

     req = "INSERT INTO BR(ID_article, Designation) VALUES (?, ?)"
     cur.execute(req, (id, des))

    # Validation de la transaction et fermeture de la connexion
    conn.commit()
    conn.close()
    
    # Message de confirmation
    messagebox.showinfo("Ajouté", "Le BR a été ajouté avec succès !")
                

def year():
    ann = Toplevel()
    ann.title("activitée")
    listes_article = Button(ann, text="Liste d'articles",command=article, padx=50, pady=10)
    listes_article.pack(padx=40, pady=20)

    


    ajouter_article = Button(ann, text="Ajouter un article", command=ajouter, padx=50, pady=10)
    ajouter_article.pack(padx=40, pady=20)

    BR = Button(ann, text="BR",command=num_BR, padx=50, pady=10)
    BR.pack(padx=40, pady=20)

    BS = Button(ann, text="BS", padx=50, pady=10)
    BS.pack(padx=40, pady=20)



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

        option2_button = Button(options_window, text="2022", padx=50, pady=10)
        option2_button.pack(padx=40, pady=20)

        option3_button = Button(options_window, text="2021", padx=50, pady=10)
        option3_button.pack(padx=40, pady=20)

        option4_button = Button(options_window, text="2020", padx=50, pady=10)
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
