import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk



root = Tk()
root.title('LOGIN')
root.geometry("1300x700")

def AjouterArticle():
    add_article_window = tk.Toplevel()
    add_article_window.title("Ajouter Article")
    add_article_window.geometry("1300x700")
    
    # Define the labels and entry fields
    code_art_label = ttk.Label(add_article_window, text="Code Article:")
    code_art_entry = ttk.Entry(add_article_window)
    compte_label = ttk.Label(add_article_window, text="Compte:")
    compte_entry = ttk.Entry(add_article_window)
    designation_label = ttk.Label(add_article_window, text="Designation:")
    designation_entry = ttk.Entry(add_article_window)
    init_qte_label = ttk.Label(add_article_window, text="Quantité Initial:")
    init_qte_entry = ttk.Entry(add_article_window)
    init_prix_label = ttk.Label(add_article_window, text="Prix U Initial:")
    init_prix_entry = ttk.Entry(add_article_window)
    code_mag_label = ttk.Label(add_article_window, text="Code Magasin:")
    code_mag_combobox = ttk.Combobox(add_article_window, values=["PDR", "FB", "MP", "PF"])




    
    code_art_label.grid(row=0, column=0, padx=10, pady=10)
    code_art_entry.grid(row=0, column=1, padx=10, pady=10)
    compte_label.grid(row=1, column=0, padx=10, pady=10)
    compte_entry.grid(row=1, column=1, padx=10, pady=10)
    designation_label.grid(row=2, column=0, padx=10, pady=10)
    designation_entry.grid(row=2, column=1, padx=10, pady=10)
    init_qte_label.grid(row=3, column=0, padx=10, pady=10)
    init_qte_entry.grid(row=3, column=1, padx=10, pady=10)
    init_prix_label.grid(row=4, column=0, padx=10, pady=10)
    init_prix_entry.grid(row=4, column=1, padx=10, pady=10)
    code_mag_label.grid(row=5, column=0, padx=10, pady=10)
    code_mag_combobox.grid(row=5, column=1, padx=10, pady=10)



    def save_article():

        conn = sqlite3.connect('stock.db')
        c = conn.cursor()


    
        code_art = code_art_entry.get()
        compte = compte_entry.get()
        designation = designation_entry.get()
        init_qte = init_qte_entry.get()
        init_prix = init_prix_entry.get()
        code_mag = code_mag_combobox.get()

        
        init_montant = float(init_prix) * float(init_qte)

        # Insert the new article into the database
        c.execute("INSERT INTO ARTICLES VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (code_art, compte, designation, init_qte, init_prix, init_montant, init_qte, init_prix, init_montant, code_mag))


        code_art_entry.delete(0, END)
        compte_entry.delete(0, END)
        designation_entry.delete(0, END)
        init_qte_entry.delete(0, END)
        init_prix_entry.delete(0, END)
        code_mag_combobox.delete(0, END)
        



       
        conn.commit()

        

    
    save_button = ttk.Button(add_article_window, text="Save", command=save_article)
    save_button.grid(row=6, column=1, padx=10, pady=10, columnspan=2)

    def annuler():
        add_article_window.destroy()


    exit_button = ttk.Button(add_article_window, text="Retour", command=annuler)
    exit_button.grid(row=7, column=1, padx=10, pady=10, columnspan=2)

# ajouter_article = Button(root, text='ajouter article', command=AjouterArticle)
# ajouter_article.config(bg="yellow", fg="white", font=("Arial", 16))
# ajouter_article.pack()


def Ajouter_BR():
    add_BR_window = tk.Toplevel()
    add_BR_window.title("Ajouter BR")
    add_BR_window.geometry("1300x700")
    
    # Define the labels and entry fields
    code_br_label = ttk.Label(add_BR_window, text="Code BR:")
    code_br_entry = ttk.Entry(add_BR_window)
    date_label = ttk.Label(add_BR_window, text="date:")
    date_entry = ttk.Entry(add_BR_window)
    nom_label = ttk.Label(add_BR_window, text="Nom :")
    nom_entry = ttk.Entry(add_BR_window)
    prenom_label = ttk.Label(add_BR_window, text="Prénom:")
    prenom_entry = ttk.Entry(add_BR_window)



    
    code_br_label.grid(row=0, column=0, padx=10, pady=10)
    code_br_entry.grid(row=0, column=1, padx=10, pady=10)
    date_label.grid(row=1, column=0, padx=10, pady=10)
    date_entry.grid(row=1, column=1, padx=10, pady=10)
    nom_label.grid(row=2, column=0, padx=10, pady=10)
    nom_entry.grid(row=2, column=1, padx=10, pady=10)
    prenom_label.grid(row=3, column=0, padx=10, pady=10)
    prenom_entry.grid(row=3, column=1, padx=10, pady=10)



    def save_br():

        conn = sqlite3.connect('stock.db')
        c = conn.cursor()


    
        code_br = code_br_entry.get()
        date = date_entry.get()
        nom = nom_entry.get()
        prenom = prenom_entry.get()
        
        

        # Insert the new article into the database
        c.execute("INSERT INTO BR VALUES (?, ?, ?, ?)",
                  (code_br,date,nom,prenom))


        code_br_entry.delete(0, END)
        date_entry.delete(0, END)
        nom_entry.delete(0, END)
        prenom_entry.delete(0, END)



       
        conn.commit()

        

    
    save_button = ttk.Button(add_BR_window, text="Save", command=save_br)
    save_button.grid(row=6, column=1, padx=10, pady=10, columnspan=2)


def Ajouter_BSM():
    add_BSM_window = tk.Toplevel()
    add_BSM_window.title("Ajouter BSM")
    add_BSM_window.geometry("1300x700")
    
    # Define the labels and entry fields
    code_bsm_label = ttk.Label(add_BSM_window, text="Code BSM:")
    code_bsm_entry = ttk.Entry(add_BSM_window)
    date_label = ttk.Label(add_BSM_window, text="date:")
    date_entry = ttk.Entry(add_BSM_window)
    nom_label = ttk.Label(add_BSM_window, text="Nom :")
    nom_entry = ttk.Entry(add_BSM_window)
    prenom_label = ttk.Label(add_BSM_window, text="Prénom:")
    prenom_entry = ttk.Entry(add_BSM_window)



    
    code_bsm_label.grid(row=0, column=0, padx=10, pady=10)
    code_bsm_entry.grid(row=0, column=1, padx=10, pady=10)
    date_label.grid(row=1, column=0, padx=10, pady=10)
    date_entry.grid(row=1, column=1, padx=10, pady=10)
    nom_label.grid(row=2, column=0, padx=10, pady=10)
    nom_entry.grid(row=2, column=1, padx=10, pady=10)
    prenom_label.grid(row=3, column=0, padx=10, pady=10)
    prenom_entry.grid(row=3, column=1, padx=10, pady=10)



    def save_bsm():

        conn = sqlite3.connect('stock.db')
        c = conn.cursor()


    
        code_bsm = code_bsm_entry.get()
        date = date_entry.get()
        nom = nom_entry.get()
        prenom = prenom_entry.get()
        
        

        # Insert the new article into the database
        c.execute("INSERT INTO BSM VALUES (?, ?, ?, ?)",
                  (code_bsm,date,nom,prenom))


        code_bsm_entry.delete(0, END)
        date_entry.delete(0, END)
        nom_entry.delete(0, END)
        prenom_entry.delete(0, END)



       
        conn.commit()

        

    
    save_button = ttk.Button(add_BSM_window, text="Save", command=save_bsm)
    save_button.grid(row=6, column=1, padx=10, pady=10, columnspan=2)




    def annuler():
        add_BSM_window.destroy()


    exit_button = ttk.Button(add_BSM_window, text="Retour", command=annuler)
    exit_button.grid(row=7, column=1, padx=10, pady=10, columnspan=2)


def show_articles():


    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    
    
    articles_window = tk.Toplevel()
    articles_window.title("Articles List")
    articles_window.geometry("1300x700")

    # Create a treeview widget to display the articles
    articles_treeview = ttk.Treeview(articles_window, columns=("compte", "designation", "init_qté", "init_prix", "init_montant","qté", "prix", "montant", "code_mag"))
    articles_treeview.heading("#0", text="Code Article")
    articles_treeview.heading("compte", text="Compte")
    articles_treeview.heading("designation", text="Designation")
    articles_treeview.heading("init_qté", text="Quantite initial")
    articles_treeview.heading("init_prix", text="Prix u initial")
    articles_treeview.heading("init_montant", text="Montant initial")
    articles_treeview.heading("qté", text="Quantite")
    articles_treeview.heading("prix", text="Prix")
    articles_treeview.heading("montant", text="Montant")
    articles_treeview.heading("code_mag", text="Code Magasin")
    articles_treeview.pack(fill="both", expand=True)

    articles_treeview.column("#0", width=100, stretch=NO)
    articles_treeview.column("compte", width=100, stretch=NO)
    articles_treeview.column("designation", width=100, stretch=NO)
    articles_treeview.column("init_qté", width=100, stretch=NO)
    articles_treeview.column("init_prix", width=100, stretch=NO)
    articles_treeview.column("init_montant", width=100, stretch=NO)
    articles_treeview.column("qté", width=100, stretch=NO)
    articles_treeview.column("prix", width=100, stretch=NO)
    articles_treeview.column("montant", width=100, stretch=NO)
    articles_treeview.column("code_mag", width=100, stretch=NO)
   

    
    c.execute("""SELECT * FROM ARTICLES""")
    articles = c.fetchall()

    
    for article in articles:
        code_art = article[0]
        compte = article[1]
        designation = article[2]
        init_qte = article[3]
        init_prix = article[4]
        init_montant = article[5]
        qte = article[6]
        prix = article[7]
        montant = article[8]
        code_mag = article[9]
        articles_treeview.insert("", "end", text=code_art, values=(compte, designation, init_qte, init_prix, init_montant,qte, prix, montant, code_mag))



# afficher_article = Button(root, text='Liste Articles', command=show_articles)
# afficher_article.config(bg="green", fg="white", font=("Arial", 16))
# afficher_article.pack()


def show_br():


    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    
    
    BR_window = tk.Toplevel()
    BR_window.title("List BR")
    BR_window.geometry("1300x700")

    # Create a treeview widget to display the articles
    BR_treeview = ttk.Treeview(BR_window, columns=("date", "nom", "prénom"))
    BR_treeview.heading("#0", text="Code BR")
    BR_treeview.heading("date", text="Date")
    BR_treeview.heading("nom", text="Nom")
    BR_treeview.heading("prénom", text="Prénom")
    BR_treeview.pack(fill="both", expand=True)

    BR_treeview.column("#0", width=100, stretch=NO)
    BR_treeview.column("date", width=100, stretch=NO)
    BR_treeview.column("nom", width=100, stretch=NO)
    BR_treeview.column("prénom", width=100, stretch=NO)
   

    
    c.execute("""SELECT * FROM BR""")
    BR = c.fetchall()

    
    for BR in BR:
        code_br = BR[0]
        date = BR[1]
        nom = BR[2]
        prenom = BR[3]
        
        BR_treeview.insert("", "end", text=code_br, values=(date, nom, prenom))



# afficher_article = Button(root, text='Liste Articles', command=show_articles)






def article_details():
    detail_window = tk.Toplevel()
    detail_window.title("Detail Article")
    detail_window.geometry("1300x700")
    
    # Define the labels and entry fields
    code_art_label = ttk.Label(detail_window, text="Code Article:")
    code_art_entry = ttk.Entry(detail_window)
    

    # Add the labels and entry fields to the window
    code_art_label.pack()
    code_art_entry.pack()
    


    def show_detail():

        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        s = conn.cursor()
        


    
        code_art = code_art_entry.get()
        

        
       

        
        c.execute("""SELECT * FROM ENTRES WHERE ENTRES.code_article=?""", (code_art,))
             
        entres=c.fetchall()

        s.execute("""SELECT * FROM SORTIES WHERE SORTIES.code_article=?""", (code_art,)) 

        sorties=s.fetchall()       

        entres_treeview = ttk.Treeview(detail_window, columns=("qté_entres", "prix_ent", "montant_ent", "code_br"))
        entres_treeview.heading("#0", text="code entré")
        entres_treeview.heading("qté_entres", text="qté entres")
        entres_treeview.heading("prix_ent", text="prix ent")
        entres_treeview.heading("montant_ent", text="montant ent")
        entres_treeview.heading("code_br", text="code br")
        entres_treeview.pack(fill="both", expand=True)

        sorties_treeview = ttk.Treeview(detail_window, columns=("qté_sort", "prix_sort", "montant_sort", "code_bs"))
        sorties_treeview.heading("#0", text="code sorties")
        sorties_treeview.heading("qté_sort", text="qté sorties")
        sorties_treeview.heading("prix_sort", text="prix sorties")
        sorties_treeview.heading("montant_sort", text="montant sorties")
        sorties_treeview.heading("code_bs", text="code bs")
        sorties_treeview.pack(fill="both", expand=True)
        

    
    
        for entre in entres :
            code_entré = entre[0]
            qté_ent = entre[1]
            prix_ent = entre[2]
            montant_ent = entre[3]
            code_br = entre[4]
        
            entres_treeview.insert("", "end", text=code_entré, values=(qté_ent, prix_ent, montant_ent, code_br))



        for sortie in sorties :
            code_sort = sortie[0]
            qté_sort = sortie[1]
            prix_sort = sortie[2]
            montant_sort = sortie[3]
            code_bs = sortie[4]
        
            sorties_treeview.insert("", "end", text=code_sort, values=(qté_sort, prix_sort, montant_sort, code_bs))


       
        



        
        conn.commit()

        

    
    detail_button = ttk.Button(detail_window, text="details", command=show_detail)
    detail_button.pack()






# detail_article = Button(root, text='detaile Articles', command=article_details)
# detail_article.config(bg="red", fg="white", font=("Arial", 16))
# detail_article.pack()




def AjouterEntres():
    add_entres_window = tk.Toplevel()
    add_entres_window.title("Ajouter Entré")
    add_entres_window.geometry("1300x700")
    
    # Define the labels and entry fields
    code_entre_label = ttk.Label(add_entres_window, text="Code Entré:")
    code_entre_entry = ttk.Entry(add_entres_window)
    qté_ent_label = ttk.Label(add_entres_window, text="Quantité Entré:")
    qté_ent_entry = ttk.Entry(add_entres_window)
    prix_ent_label = ttk.Label(add_entres_window, text="Prix U Entré:")
    prix_ent_entry = ttk.Entry(add_entres_window)
    code_br_label = ttk.Label(add_entres_window, text="Code BR:")
    code_br_entry = ttk.Entry(add_entres_window)
    code_article_label = ttk.Label(add_entres_window, text="Code Article:")
    code_article_entry = ttk.Entry(add_entres_window)

    # Add the labels and entry fields to the window
    code_entre_label.pack()
    code_entre_entry.pack()
    qté_ent_label.pack()
    qté_ent_entry.pack()
    prix_ent_label.pack()
    prix_ent_entry.pack()
    code_br_label.pack()
    code_br_entry.pack()
    code_article_label.pack()
    code_article_entry.pack()
    



    def save_entres():

        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        d = conn.cursor()


    
        code_entre = code_entre_entry.get()
        qté_ent = qté_ent_entry.get()
        prix_ent = prix_ent_entry.get()
        code_br = code_br_entry.get()
        code_article = code_article_entry.get()

        
        montant_ent = float(prix_ent) * float(qté_ent)

        
        c.execute("INSERT INTO ENTRES VALUES (?, ?, ?, ?, ?, ?)",
                  (code_entre, qté_ent, prix_ent, montant_ent, code_br, code_article))




        c.execute("""
        UPDATE ARTICLES
        SET qte = qte + (SELECT qte_ent FROM ENTRES WHERE ENTRES.code_entre = ?),
        prix = (SELECT prix_ent FROM ENTRES WHERE ENTRES.code_entre = ?),
        montant = (qte + (SELECT qte_ent FROM ENTRES WHERE ENTRES.code_entre = ?))*(SELECT prix_ent FROM ENTRES WHERE ENTRES.code_entre = ?)
        WHERE code_art = ?
        """, (code_entre,code_entre,code_entre,code_entre,code_article,))





        




        code_entre_entry.delete(0, END)
        qté_ent_entry.delete(0, END)
        prix_ent_entry.delete(0, END)
        code_br_entry.delete(0, END)
        code_article_entry.delete(0, END)
        



        
        conn.commit()

        

    
    save_button = ttk.Button(add_entres_window, text="Save", command=save_entres)
    save_button.pack()

    def annuler():
        add_entres_window.destroy()


    exit_button = ttk.Button(add_entres_window, text="Retour", command=annuler)
    exit_button.pack()


# ajouter_Entre = Button(root, text='Ajouter Entré ', command=AjouterEntres)
# ajouter_Entre.config(bg="blue", fg="white", font=("Arial", 16))
# ajouter_Entre.pack()

def AjouterSorties():
    add_sorties_window = tk.Toplevel()
    add_sorties_window.title("Ajouter Sortie")
    add_sorties_window.geometry("1300x700")
    
    # Define the labels and entry fields
    code_sortie_label = ttk.Label(add_sorties_window, text="Code Sortie:")
    code_sortie_entry = ttk.Entry(add_sorties_window)
    qté_sort_label = ttk.Label(add_sorties_window, text="Quantité Sortie:")
    qté_sort_entry = ttk.Entry(add_sorties_window)
    prix_sort_label = ttk.Label(add_sorties_window, text="Prix U Sortie:")
    prix_sort_entry = ttk.Entry(add_sorties_window)
    code_bs_label = ttk.Label(add_sorties_window, text="Code BSM:")
    code_bs_entry = ttk.Entry(add_sorties_window)
    code_article_label = ttk.Label(add_sorties_window, text="Code Article:")
    code_article_entry = ttk.Entry(add_sorties_window)

    # Add the labels and entry fields to the window
    code_sortie_label.pack()
    code_sortie_entry.pack()
    qté_sort_label.pack()
    qté_sort_entry.pack()
    prix_sort_label.pack()
    prix_sort_entry.pack()
    code_bs_label.pack()
    code_bs_entry.pack()
    code_article_label.pack()
    code_article_entry.pack()
    



    def save_sorties():

        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        d = conn.cursor()


    
        code_sort = code_sortie_entry.get()
        qté_sort = qté_sort_entry.get()
        prix_sort = prix_sort_entry.get()
        code_bs = code_bs_entry.get()
        code_article = code_article_entry.get()

        
        montant_sort = float(prix_sort) * float(qté_sort)

        
        c.execute("INSERT INTO SORTIES VALUES (?, ?, ?, ?, ?, ?)",
                  (code_sort, qté_sort, prix_sort, montant_sort, code_bs, code_article))




        c.execute("""
        UPDATE ARTICLES
        SET qte = qte - (SELECT qte_sort FROM SORTIES WHERE SORTIES.code_sortie = ?),
        prix = (SELECT prix_sort FROM SORTIES WHERE SORTIES.code_sortie = ?),
        montant = (qte - (SELECT qte_sort FROM SORTIES WHERE SORTIES.code_sortie = ?))*(SELECT prix_sort FROM SORTIES WHERE SORTIES.code_sortie = ?)
        WHERE code_art = ?
        """, (code_sort,code_sort,code_sort,code_sort,code_article,))





        




        code_sortie_entry.delete(0, END)
        qté_sort_entry.delete(0, END)
        prix_sort_entry.delete(0, END)
        code_bs_entry.delete(0, END)
        code_article_entry.delete(0, END)
        



        
        conn.commit()

        

    
    save_button = ttk.Button(add_sorties_window, text="Save", command=save_sorties)
    save_button.pack()

    def annuler():
        add_sorties_window.destroy()


    exit_button = ttk.Button(add_sorties_window, text="Retour", command=annuler)
    exit_button.pack()

def login():
    # Check if the username and password are correct
    if username_entry.get() == "admin" and password_entry.get() == "1234":
        # Clear the username and password fields
        username_entry.delete(0, END)
        password_entry.delete(0, END)

        # # Close the login window
        # root.destroy()


        # Open the options window
        options_window = Toplevel(root)
        options_window.title("Options")
        options_window.geometry("1300x700")


        ajouter_article = Button(options_window, text='ajouter article', command=AjouterArticle)
        ajouter_article.config(bg="yellow", fg="white", font=("Arial", 16))
        ajouter_article.pack()

        afficher_article = Button(options_window, text='Liste Articles', command=show_articles)
        afficher_article.config(bg="green", fg="white", font=("Arial", 16))
        afficher_article.pack()

        detail_article = Button(options_window, text='detaile Articles', command=article_details)
        detail_article.config(bg="red", fg="white", font=("Arial", 16))
        detail_article.pack()

        ajouter_Entre = Button(options_window, text='Ajouter Entré ', command=AjouterEntres)
        ajouter_Entre.config(bg="blue", fg="white", font=("Arial", 16))
        ajouter_Entre.pack()

        ajouter_Sortie = Button(options_window, text='Ajouter Sortie ', command=AjouterSorties)
        ajouter_Sortie.config(bg="pink", fg="white", font=("Arial", 16))
        ajouter_Sortie.pack()
     
        ajouter_br = Button(options_window, text='Ajouter BR ', command=Ajouter_BR)
        ajouter_br.config(bg="black", fg="white", font=("Arial", 16))
        ajouter_br.pack()     

        ajouter_bsm = Button(options_window, text='Ajouter BSM ', command=Ajouter_BSM)
        ajouter_bsm.config(bg="black", fg="white", font=("Arial", 16))
        ajouter_bsm.pack()

        afficher_br = Button(options_window, text='List BR ', command=show_br)
        afficher_br.config(bg="brown", fg="white", font=("Arial", 16))
        afficher_br.pack()

    else:
        # Show an error message if the username or password is incorrect
        error_label.config(text="Incorrect username or password")




# Create widgets for the login window
username_label = Label(root, text="Username:", font=("Times", 16, "bold"))
username_label.pack(pady=10)

username_entry = Entry(root)
username_entry.pack(pady=10)

password_label = Label(root, text="Password:", font=("Times", 16, "bold"))
password_label.pack(pady=10)

password_entry = Entry(root, show="*")
password_entry.pack(pady=10)

login_button = Button(root, text="Login", command=login, bg="white", font=("Arial", 14))
login_button.pack(padx=20, pady=20)

error_label = Label(root, fg="red")
error_label.pack()






root.mainloop()
