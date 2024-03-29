from tkinter import *
import sqlite3
import tkinter as tk
# from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkcalendar import DateEntry
import re

root = Tk()
root.title("Se connecter")
root.geometry('1166x718')
root.state('zoomed')     #Une fenetre plain de l'ecran
root.resizable(0,0)    # annuler la minimisation de la fenetre
root.title("Gestion de stock")
root.iconbitmap('C:\\Users\\pc\\version1-main\\star.ico')

root.config(background='#ACE5F3')
# root.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')
        
#=============================== Dectionnaire pour stocker les identifiants ===============================================

# identifiants = {
#     "magasinier PDR": "magasinpdr",
#     "magasinier FB": "magasinfb",
#     "magasinier MP": "magasinmp",
#     "magasinier PF": "magasinpf",
#     "administrateur": "admin",
#     "22": "22"
# }

def verifier_identifiants():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password =="1234" :
        
        message_label.config(text="")
        ouvrir_fenetre_bienvenue()
        root.mainloop()
    else: 
        if  username == "magasinier MP" and password =="1234" :
        
              message_label.config(text="")
              ouvrir_fenetre_bienvenue_mag_MP()
              root.mainloop()  
        else:
            if  username == "magasinier PDR" and password =="1234" :
        
               message_label.config(text="")
               ouvrir_fenetre_bienvenue_mag_PDR()
               root.mainloop()
            else:  
                if  username == "magasinier FB" and password =="1234" :
        
                   message_label.config(text="")
                   ouvrir_fenetre_bienvenue_mag_FB()
                   root.mainloop()   
                else:
                    if username == "magasinier PF" and password =="1234" :
        
                       message_label.config(text="")
                       ouvrir_fenetre_bienvenue_mag_PF()
                       root.mainloop()
                    else:        
                      message_label.config(text="Identifiants incorrect",fg="red")



#============================== Fonction pour vérifier les identifiants de l'utilisateur====================================
# def verifier_identifiants():
#     username = username_entry.get()
#     password = password_entry.get()
#     if identifiants.get(username) == password:
        
#         message_label.config(text="Vous êtes connecté(e) !")
#         ouvrir_fenetre_bienvenue()
#         root.mainloop()
#     else:
#         message_label.config(text="Identifiants incorrect",fg="red")
    
#================================Ajouter Article================================================================
def ajouter():
    ajou = Toplevel()
    ajou.geometry('1000x1000')
    ajou.title("Ajouter Article")
    ajou.state('zoomed')
    # ajou.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    ajou.resizable(0,0) 
    ajou.config(bg="#ACE5F3")
    ajou_frame = Frame(ajou,bg='#067790', width='500', height='600')
    ajou_frame.place(x=380, y=30)

    label = Label(ajou_frame, text="Ajouter un nouveau article ",bg='#067790',font=('yu gothic ui', 25,'bold'),fg='white')
    label.place(x=50, y=30)

    global id_article_entry, code_comptable_entry, designation_entry

    code_article_label = Label(ajou_frame, text="Code Article* ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    code_article_label.place(x=110, y=115)

    code_article_entry = Entry(ajou_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    code_article_entry.place(x=250, y=115, width=120)

    code_article_line =Canvas(ajou_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    code_article_line.place(x=250, y=140)

    designation_label = Label(ajou_frame, text="Designation* ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    designation_label.place(x=110, y=180)

    designation_entry = Entry(ajou_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    designation_entry.place(x=250, y=180, width=120)

    designation_line =Canvas(ajou_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    designation_line.place(x=250, y=205)


    qte_label = Label(ajou_frame, text="Quantité*",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    qte_label.place(x=110, y=245)

    qte_entry = Entry(ajou_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    qte_entry.place(x=250, y=245, width=120)

    qte_line =Canvas(ajou_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    qte_line.place(x=250, y=270)

    prix_label = Label(ajou_frame, text="Prix*",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    prix_label.place(x=110, y=310)

    prix_entry = Entry(ajou_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    prix_entry.place(x=250, y=310, width=120)

    prix_line =Canvas(ajou_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    prix_line.place(x=250, y=335)


    code_catg_label = Label(ajou_frame, text="Catégorie*",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    code_catg_label.place(x=110, y=375)

    code_catg_combobox = ttk.Combobox(ajou_frame, values=["PDR", "FB", "MP", "PF"], state='readonly')
    code_catg_combobox.place(x=250, y=375, width=120)

    code_catg_line =Canvas(ajou_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    code_catg_line.place(x=250, y=395)

    
    def save_article():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        code_art = code_article_entry.get()
        designation = designation_entry.get()
        qte = qte_entry.get()
        prix = prix_entry.get()
        code_catg = code_catg_combobox.get()
        montant = float(prix) * int(qte)

        # Vérifier si les champs obligatoires sont remplis
        if not code_art or not designation or not qte or not prix or not code_catg:
            messagebox.showerror(title="Erreur", message="Veuillez remplir tous les champs obligatoires (*)", parent=ajou_frame)
            return


        # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM ARTICLE WHERE code_article=?", (code_art,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le code article existe déjà dans la base de données", parent=ajou_frame)
            return


        c.execute("INSERT INTO ARTICLE VALUES (?, ?, ?, ?, ?, ?)",
             (code_art, designation, qte, prix, montant, code_catg))

        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=ajou_frame)


        
    

        code_article_entry.delete(0, END)
        designation_entry.delete(0, END)
        qte_entry.delete(0, END)
        prix_entry.delete(0, END)
        code_catg_combobox.set("")
        
        
        conn.commit()
    save_button = Button(ajou, text="Ajouter",width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_article)
    save_button.place(x=660,y=500)
        

    def annuler():
        code_article_entry.delete(0, END)
        designation_entry.delete(0, END)
        qte_entry.delete(0, END)
        prix_entry.delete(0, END)
        code_catg_combobox.set("")
    exit_button = Button(ajou, text="Annuler", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=450,y=500)


    def annuler():
        ajou.destroy()
    exit_button = Button(ajou, text="Retour", width='20', cursor='hand2', command=annuler)
    exit_button.place(x=10,y=630)

#===========================================supprimer article=====================================
def supprimer():
    supr = Toplevel()
    supr.geometry('1000x1000')
    supr.title("Suprimer article")
    supr.state('zoomed')  
    # supr.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')  
    supr.resizable(0,0) 
    supr.config(bg="#ACE5F3")
    supr_frame = Frame(supr,bg='#067790', width='500', height='600')
    supr_frame.place(x=380, y=30)

    label = Label(supr_frame, text="Supprimer un article ",bg='#067790',font=('yu gothic ui', 25,'bold'),fg='white')
    label.place(x=100, y=80)

    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT code_article FROM ARTICLE")
    values = [row[0] for row in c.fetchall()]

    code_art_label = Label(supr_frame, text="Code Article: ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    code_art_label.place(x=140, y=200)

    code_art_combobox = ttk.Combobox(supr_frame, text="Code Article:",width='15', state='readonly', values=values)
    code_art_combobox.place(x=250, y=200, width=110)

    code_art_line =Canvas(supr_frame, width=110, height=2.0,bg='white',highlightthickness=0)
    code_art_line.place(x=250, y=220)

    conn.close()

    def save_suprimer():
        code_art = code_art_combobox.get()

        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()
        c.execute("DELETE FROM ARTICLE WHERE code_article = ?",(code_art,))
        messagebox.showinfo(title="Succès",message="L'article a été suprimmer avec succès", parent=supr_frame)
        

        c.execute("SELECT code_article FROM ARTICLE")
        new_values = [row[0] for row in c.fetchall()]

        code_art_combobox.configure(values=new_values)
        code_art_combobox.set("")

        conn.commit()
        conn.close()

        



    save_button = Button(supr, text="Supprimer",width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_suprimer)
    save_button.place(x=660,y=450)
        

    def annuler():
        code_art_combobox.set("")
    exit_button = Button(supr, text="Annuler", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=450,y=450)


    def annuler():
        supr.destroy()
    exit_button = Button(supr, text="Retour", width='20', cursor='hand2', command=annuler)
    exit_button.place(x=10,y=630)

#========================================MP   PDR   FB    PF=======================================
def articles_type():
    
    articles = Toplevel()
    articles.geometry('500x500')
    articles.title("Articles")
    articles.state('zoomed')
    # articles.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
    articles.resizable(0,0) 
    articles.config(background='#ACE5F3')
    articles_frame = Frame(articles,bg='#067790', width='500', height='600')
    articles_frame.place(x=380, y=30)
    btn = Button(articles_frame,text="MP",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=articleMP)
    btn.place(x=120,y=120)
    btn1 = Button(articles_frame,text="PDR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=articlePDR)
    btn1.place(x=120,y=220)
    btn2 = Button(articles_frame,text="FB",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=articleFB)
    btn2.place(x=120,y=320)
    btn3 = Button(articles_frame,text="PF",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=articlePF)
    btn3.place(x=120,y=420)
   
    def annuler():
        articles.destroy()


    exit_button = Button(articles, text="Retour",width='20', cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)



#=========================Liste article=======================================================================

def articleMP() :

    conn = sqlite3.connect('stock1.db')
    cur = conn.cursor()

    art = Toplevel()
    art.title("Liste des aticles MP")
    art.state('zoomed') 
    # art.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    art.resizable(0,0) 
    art.config(bg='#ACE5F3')
    art_frame = Frame(art,bg='#067790',)
    art_frame.place(x=180, y=70)

    article_label = Label(art, text="Liste des articles MP", font=('yu gothic ui', 23,'bold'),fg="white",bg='#ACE5F3')
    article_label.place(x=500, y=20)

    # Créer le tableau
    table = ttk.Treeview(art_frame, columns=("designation","qte","prix","montant", "code_catg"), height='25')
    # Définir les en-têtes de colonnes
    table.heading("#0", text="Code Article")
    table.heading("designation", text="Designation")
    table.heading("qte", text="Quantite")
    table.heading("prix", text="Prix")
    table.heading("montant", text="Montant")
    table.heading("code_catg", text="Catégorie")
    
    table.pack(fill="both", expand=True)

    table.column("#0", width=150, stretch=NO)
    table.column("designation", width=170, stretch=NO)
    table.column("qte", width=150, stretch=NO)
    table.column("prix", width=150, stretch=NO)
    table.column("montant", width=150, stretch=NO)
    table.column("code_catg", width=150, stretch=NO)
   
    cur.execute("""SELECT * FROM ARTICLE WHERE code_catg='MP'
    """)
    articles = cur.fetchall()

    for article in articles:
        code_art = article[0]
        designation = article[1]
        qte = article[2]
        prix = article[3]
        montant = article[4]
        code_mag = article[5]
        table.insert("", "end", text=code_art, values=(designation,qte, prix, montant, code_mag))

    def annuler():
        art.destroy()

    exit_button = Button(art, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)



def articlePDR() :

    conn = sqlite3.connect('stock1.db')
    cur = conn.cursor()

    art = Toplevel()
    art.title("Liste des aticles PDR")
    art.state('zoomed') 
    # art.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    art.resizable(0,0) 
    art.config(background='#ACE5F3')
    art_frame = Frame(art,bg='#067790', width='900', height='600')
    art_frame.place(x=200, y=70)

    article_label = Label(art, text="Liste des articles PDR", font=('yu gothic ui', 23,'bold'),fg="white",bg="#ACE5F3")
    article_label.place(x=500, y=20)

    # Créer le tableau
    table = ttk.Treeview(art_frame, columns=("designation","qte","prix","montant", "code_catg"), height='25')
    # Définir les en-têtes de colonnes
    table.heading("#0", text="Code Article")
    table.heading("designation", text="Designation")
    table.heading("qte", text="Quantite")
    table.heading("prix", text="Prix")
    table.heading("montant", text="Montant")
    table.heading("code_catg", text="Catégorie")
    
    table.pack(fill="both", expand=True)

    table.column("#0", width=150, stretch=NO)
    table.column("designation", width=180, stretch=NO)
    table.column("qte", width=150, stretch=NO)
    table.column("prix", width=150, stretch=NO)
    table.column("montant", width=150, stretch=NO)
    table.column("code_catg", width=150, stretch=NO)
   
    cur.execute("""SELECT * FROM ARTICLE WHERE code_catg='PDR'
    """)
    articles = cur.fetchall()

    for article in articles:
        code_art = article[0]
        designation = article[1]
        qte = article[2]
        prix = article[3]
        montant = article[4]
        code_mag = article[5]
        table.insert("", "end", text=code_art, values=(designation,qte, prix, montant, code_mag))

    def annuler():
        art.destroy()

    exit_button = Button(art, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)



def articleFB() :

    conn = sqlite3.connect('stock1.db')
    cur = conn.cursor()

    art = Toplevel()
    art.title("Liste des aticles FB")
    art.state('zoomed') 
    # art.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    art.resizable(0,0) 
    art.config(background='#ACE5F3')
    art_frame = Frame(art,bg='#067790', width='900', height='600')
    art_frame.place(x=200, y=70)

    article_label = Label(art, text="Liste des articles FB", font=('yu gothic ui', 23,'bold'),fg="white",bg="#ACE5F3")
    article_label.place(x=500, y=20)

    # Créer le tableau
    table = ttk.Treeview(art_frame, columns=("designation","qte","prix","montant", "code_catg"), height='25')
    # Définir les en-têtes de colonnes
    table.heading("#0", text="Code Article")
    table.heading("designation", text="Designation")
    table.heading("qte", text="Quantite")
    table.heading("prix", text="Prix")
    table.heading("montant", text="Montant")
    table.heading("code_catg", text="Catégorie")
    
    table.pack(fill="both", expand=True)

    table.column("#0", width=150, stretch=NO)
    table.column("designation", width=170, stretch=NO)
    table.column("qte", width=150, stretch=NO)
    table.column("prix", width=150, stretch=NO)
    table.column("montant", width=150, stretch=NO)
    table.column("code_catg", width=150, stretch=NO)
   
    cur.execute("""SELECT * FROM ARTICLE WHERE code_catg='FB'
    """)
    articles = cur.fetchall()

    for article in articles:
        code_art = article[0]
        designation = article[1]
        qte = article[2]
        prix = article[3]
        montant = article[4]
        code_mag = article[5]
        table.insert("", "end", text=code_art, values=(designation,qte, prix, montant, code_mag))

    def annuler():
        art.destroy()

    exit_button = Button(art, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)




def articlePF() :

    conn = sqlite3.connect('stock1.db')
    cur = conn.cursor()

    art = Toplevel()
    art.title("Liste des aticles PF")
    art.state('zoomed')
    # art.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    art.resizable(0,0) 
    art.config(background='#ACE5F3')
    art_frame = Frame(art,bg='#067790', width='900', height='600')
    art_frame.place(x=200, y=70)

    article_label = Label(art, text="Liste des articles PF", font=('yu gothic ui', 23,'bold'),fg="white",bg="#ACE5F3")
    article_label.place(x=500, y=20)

    # Créer le tableau
    table = ttk.Treeview(art_frame, columns=("designation","qte","prix","montant", "code_catg"), height='25')
    # Définir les en-têtes de colonnes
    table.heading("#0", text="Code Article")
    table.heading("designation", text="Designation")
    table.heading("qte", text="Quantite")
    table.heading("prix", text="Prix")
    table.heading("montant", text="Montant")
    table.heading("code_catg", text="Catégorie")
    
    table.pack(fill="both", expand=True)

    table.column("#0", width=150, stretch=NO)
    table.column("designation", width=170, stretch=NO)
    table.column("qte", width=150, stretch=NO)
    table.column("prix", width=150, stretch=NO)
    table.column("montant", width=150, stretch=NO)
    table.column("code_catg", width=150, stretch=NO)
   
    cur.execute("""SELECT * FROM ARTICLE WHERE code_catg='PF'
    """)
    articles = cur.fetchall()

    for article in articles:
        code_art = article[0]
        designation = article[1]
        qte = article[2]
        prix = article[3]
        montant = article[4]
        code_mag = article[5]
        table.insert("", "end", text=code_art, values=(designation,qte, prix, montant, code_mag))

    def annuler():
        art.destroy()

    exit_button = Button(art, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)




#==================================Detail Article================================
def article_details():
    detail_window = Toplevel()
    detail_window.title("Detail Article")
    detail_window.geometry("1300x700")
   
    # detail_window.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    
    detail_window.config(background='#ACE5F3')

    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT code_article FROM ARTICLE")
    values = [row[0] for row in c.fetchall()]


    # Créer les widgets de la fenêtre
    label = Label(detail_window, text="Code Article:", bg='#ACE5F3', font=('yu gothic ui', 14,'bold'), fg='black')
    label.place(x=50, y=30)

    code_art_combobox = ttk.Combobox(detail_window, text="Code Article",width='20', state='readonly', values=values)
    code_art_combobox.place(x=170, y=35, width=80)

    

    result_frame = Frame(detail_window, bg='#ACE5F3', width='600', height='600')
    result_frame.place(x=140, y=100)

    entres_label = Label(result_frame, text="ENTRES", bg='#ACE5F3', font=('yu gothic ui', 10,'bold'))
    entres_label.grid(row=0, column=0)

    sorties_label = Label(result_frame, text="SORTIES", bg='#ACE5F3', font=('yu gothic ui', 10,'bold'))
    sorties_label.grid(row=2, column=0)

    entres_treeview = ttk.Treeview(result_frame, columns=("qte_ent", "prix_ent", "montant_ent", "code_br"))
    sorties_treeview = ttk.Treeview(result_frame, columns=("qte_sort", "prix_sort", "montant_sort", "code_bsm"))

    entres_treeview.heading("#0", text="Code Entree")
    entres_treeview.heading("qte_ent", text="Quantite")
    entres_treeview.heading("prix_ent", text="Prix")
    entres_treeview.heading("montant_ent", text="Montant")
    entres_treeview.heading("code_br", text="Code BR")

    sorties_treeview.heading("#0", text="Code Sortie")
    sorties_treeview.heading("qte_sort", text="Quantite")
    sorties_treeview.heading("prix_sort", text="Prix")
    sorties_treeview.heading("montant_sort", text="Montant")
    sorties_treeview.heading("code_bsm", text="Code BSM")

    entres_treeview.grid(row=1, column=0, padx=10, pady=10)
    sorties_treeview.grid(row=3, column=0, padx=10, pady=10)

    # Fonction pour afficher les détails
    def show_details():
        # Effacer les anciennes données
        entres_treeview.delete(*entres_treeview.get_children())
        sorties_treeview.delete(*sorties_treeview.get_children())

        # Récupérer le code article entré par l'utilisateur
        code_article = code_art_combobox.get()

        # Connexion à la base de données
        conn = sqlite3.connect('stock1.db')
        cursor = conn.cursor()

        # Récupérer les données de la table ENTRES pour le code article entré
        cursor.execute("SELECT * FROM Entrées WHERE code_article=?", (code_article,))
        entres = cursor.fetchall()

        # Afficher les données de la table ENTRES dans le tableau
        for i, entre in enumerate(entres):
            entres_treeview.insert("", "end", text=entre[0], values=entre[1:])

        # Récupérer les données de la table SORTIES pour le code article entré
        cursor.execute("SELECT * FROM Sorties WHERE code_article=?", (code_article,))
        sorties = cursor.fetchall()

        # Afficher les données de la table SORTIES dans le tableau
        for i, sortie in enumerate(sorties):
            sorties_treeview.insert("", "end", text=sortie[0], values=sortie[1:])

    

    # Créer le bouton pour afficher les détails
    show_button = Button(detail_window, text="Voir les détails", width='20',bg='#067790',cursor='hand2',font=('yu gothic ui', 12,'bold'),fg='white', command=show_details)
    show_button.place(x=350, y=30)

    def annuler():
        code_art_combobox.set("")
        detail_window.destroy()

    exit_button = Button(detail_window, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)


#======================================Ajouter BR==================================================================================
def AjouterBR():
    add_br_window = tk.Toplevel()
    add_br_window.title("Ajouter BR")
    add_br_window.state('zoomed') 
    # add_br_window.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    add_br_window.resizable(0,0)
    add_br_window.config(bg="#ACE5F3")
    add_br_frame = Frame(add_br_window,bg='#067790', width='900', height='600')
    add_br_frame.place(x=200, y=30)

    add_br_window.geometry("1300x700")
    


    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT Num_fournisseur FROM Fournisseurs")
    values = [row[0] for row in c.fetchall()]

    label = Label(add_br_frame, text="BON DE RECEPTION ",bg='#067790',font=('yu gothic ui', 20,'bold'),fg='white')
    label.place(x=15, y=10)
    
    code_br_label = Label(add_br_frame, text="Code BR :",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    code_br_label.place(x=380, y=70)

    code_br_entry = Entry(add_br_frame, highlightthickness=0, relief=FLAT, bg='#067790', fg='black',font=('yu gothic ui',12,'bold'))
    code_br_entry.place(x=465, y=70, width=90)

    code_br_line =Canvas(add_br_frame, width=90, height=2.0,bg='white',highlightthickness=0)
    code_br_line.place(x=465, y=93)

    date_label = Label(add_br_frame, text="Date : ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    date_label.place(x=700, y=120)

    date_entry = DateEntry(add_br_frame, width=1, background='#067790', foreground='white', borderwidth=1, font=('yu gothic ui',12,'bold'), state='readonly', date_pattern="dd/mm/yyyy")
    date_entry.place(x=750, y=120, width=130)
    date_entry.place(x=750, y=120, width=130)


    nom_label = Label(add_br_frame, text="Fournisseur :",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    nom_label.place(x=30, y=120)

    Num_fournisseur_combobox = ttk.Combobox(add_br_frame, text="Num fournisseur",width='15', state='readonly', values=values)
    Num_fournisseur_combobox.place(x=135, y=125, width=120)

    nom_line =Canvas(add_br_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    nom_line.place(x=135, y=145)

    conn.close()

    def save_BR():

        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        code_br = code_br_entry.get()
        date = date_entry.get()
        Num_fournisseur = Num_fournisseur_combobox.get()

        #Vérifier si tous les champs sont remplis
        if not code_br or not date or not Num_fournisseur:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_br_frame)
            return
    

        c.execute("INSERT INTO BR VALUES (?, ?, ?)",
                  (code_br, date, Num_fournisseur))

        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=add_br_frame)

        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_br.delete(0, END)
        

        code_br_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_fournisseur_combobox.set("")
        

        conn.commit()
        conn.close()
    
    

    

    def annuler():
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_br.delete(0, END)
        

        code_br_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_fournisseur_combobox.set("")
        e_code_entre.delete(0, tk.END)
        e_qte_ent.delete(0, tk.END)
        e_prix_ent.delete(0, tk.END)   
        e_code_combobox.set("")


    exit_button = Button(add_br_frame, text="Annuler",  width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=150,y=500)

    
    tableau = None

    def ajouter_ligne():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        # Récupération des valeurs saisies par l'utilisateur
        code_entre = e_code_entre.get()
        qte_ent = int(e_qte_ent.get())
        prix_ent = float(e_prix_ent.get())
        montant_ent = qte_ent * prix_ent
        code_br = e_code_br.get()
        code_article = e_code_combobox.get()

        # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM Entrées WHERE code_ent=?", (code_entre,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le code d'entrée existe déjà dans la base de données", parent=add_br_frame)
            return

        #Vérifier si tous les champs sont remplis
        if not code_entre or not qte_ent or not prix_ent or not montant_ent or not code_br or not code_article:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_br_frame)
            return
    
        # Insertion des données dans la base de données
        c.execute("INSERT INTO Entrées VALUES (?, ?, ?, ?, ?, ?)",
                (code_entre, qte_ent, prix_ent, montant_ent, code_br, code_article))


        c.execute("""
        UPDATE ARTICLE
        SET Quantité = Quantité + (SELECT Quantité_ent FROM entrées WHERE entrées.code_ent = ?),
        prix = (SELECT Prix_ent FROM entrées WHERE entrées.code_ent = ?),
        montant = (Quantité + (SELECT Quantité_ent FROM entrées WHERE entrées.code_ent = ?))*(SELECT Prix_ent FROM entrées WHERE entrées.code_ent = ?)
        WHERE code_article = ?
        """, (code_entre,code_entre,code_entre,code_entre,code_article,))
        conn.commit()
        conn.close()
    
        # Ajout des données dans le tableau
        tableau.insert("", tk.END, values=(code_entre, qte_ent, prix_ent, montant_ent, code_br, code_article))
    
        # Effacement des champs de saisie
        e_code_entre.delete(0, tk.END)
        e_qte_ent.delete(0, tk.END)
        e_prix_ent.delete(0, tk.END)   
        e_code_combobox.set("")

    # Création du tableau
    tableau = tk.ttk.Treeview(add_br_frame, columns=("code_entre", "qte_ent", "prix_ent", "montant_ent", "code_br", "code_article"))

    # Configuration des colonnes
    tableau.column("#0", width=0, stretch=tk.NO)
    tableau.column("code_entre", width=100)
    tableau.column("qte_ent", width=100)
    tableau.column("prix_ent", width=100)
    tableau.column("montant_ent", width=100)
    tableau.column("code_br", width=100)
    tableau.column("code_article", width=100)

    # Titres des colonnes
    tableau.heading("code_entre", text="Code Entrée")
    tableau.heading("qte_ent", text="Quantité Entrée")
    tableau.heading("prix_ent", text="Prix Entrée")
    tableau.heading("montant_ent", text="Montant Entrée")
    tableau.heading("code_br", text="Code BR")
    tableau.heading("code_article", text="Code Article")

    # Ajout d'une ligne vide pour la saisie
    tableau.insert("", tk.END, values=("", "", "", "", "", ""))

    # Placement du tableau dans la fenêtre
    tableau.place(x=150, y=250)
    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT code_article FROM ARTICLE")
    values2 = [row[0] for row in c.fetchall()]

    # Création des champs de saisie
    e_code_entre = tk.Entry(add_br_frame)
    e_qte_ent = tk.Entry(add_br_frame)
    e_prix_ent = tk.Entry(add_br_frame)
    e_code_br = tk.Entry(add_br_frame)
    e_code_combobox = ttk.Combobox(add_br_frame, text="Code Article",width='15', state='readonly', values=values2)


    


    # Placement des champs de saisie dans la fenêtre
    e_code_entre.place(x=150, y=220)
    e_qte_ent.place(x=250, y=220)
    e_prix_ent.place(x=350, y=220)
    e_code_br.place(x=450, y=220)
    e_code_combobox.place(x=550, y=219)

    # Création des étiquettes pour les champs de saisie
    tk.Label(add_br_frame, text="Code Entrée",bg="#067790").place(x=150, y=195)
    tk.Label(add_br_frame, text="Quantité Entrée",bg="#067790").place(x=250, y=195)
    tk.Label(add_br_frame, text="Prix Entrée",bg="#067790").place(x=350, y=195)
    tk.Label(add_br_frame, text="Code BR",bg="#067790").place(x=450, y=195)
    tk.Label(add_br_frame, text="Code Article",bg="#067790").place(x=550, y=195)

    # Bouton pour ajouter une ligne
    btn_ajouter = tk.Button(add_br_frame, text="Ajouter Entré",width='10', bg='#ACE5F3',cursor='hand2', command=ajouter_ligne)
    btn_ajouter.place(x=670, y=218)


    

    save_button = Button(add_br_frame, text="Ajouter", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_BR)
    save_button.place(x=610,y=500)

    

    def update_fields(event):
        value = code_br_entry.get()
        e_code_br.delete(0, END)
        e_code_br.insert(0, value)

    code_br_entry.bind("<KeyRelease>", update_fields)


    def annuler():
        add_br_window.destroy()

    exit_button = Button(add_br_window, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)
#==========================================Ajouter BR MP============================================
def AjouterBR_MP():
    add_br_window = tk.Toplevel()
    add_br_window.title("Ajouter BR")
    add_br_window.state('zoomed')  
    # add_br_window.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')  
    add_br_window.resizable(0,0)
    add_br_window.config(bg="#ACE5F3")
    add_br_frame = Frame(add_br_window,bg='#067790', width='900', height='600')
    add_br_frame.place(x=200, y=30)

    add_br_window.geometry("1300x700")



    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT Num_fournisseur FROM Fournisseurs")
    values = [row[0] for row in c.fetchall()]

    label = Label(add_br_frame, text="BON DE RECEPTION ",bg='#067790',font=('yu gothic ui', 20,'bold'),fg='white')
    label.place(x=15, y=10)
    
    code_br_label = Label(add_br_frame, text="Code BR :",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    code_br_label.place(x=380, y=70)

    code_br_entry = Entry(add_br_frame, highlightthickness=0, relief=FLAT, bg='#067790', fg='black',font=('yu gothic ui',12,'bold'))
    code_br_entry.place(x=465, y=70, width=90)

    code_br_line =Canvas(add_br_frame, width=90, height=2.0,bg='white',highlightthickness=0)
    code_br_line.place(x=465, y=93)

    date_label = Label(add_br_frame, text="Date : ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    date_label.place(x=700, y=120)

    date_entry = DateEntry(add_br_frame, width=1, background='#067790', foreground='white', borderwidth=1, font=('yu gothic ui',12,'bold'))
    date_entry.place(x=750, y=120, width=130)


    nom_label = Label(add_br_frame, text="Fournisseur :",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    nom_label.place(x=30, y=120)

    Num_fournisseur_combobox = ttk.Combobox(add_br_frame, text="Num fournisseur",width='15', state='readonly', values=values)
    Num_fournisseur_combobox.place(x=135, y=125, width=125)

    # nom_line =Canvas(add_br_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    # nom_line.place(x=135, y=145)

    conn.close()

    def save_BR():

        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        code_br = code_br_entry.get()
        date = date_entry.get()
        Num_fournisseur = Num_fournisseur_combobox.get()

        #Vérifier si tous les champs sont remplis
        if not code_br or not date or not Num_fournisseur:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_br_frame)
            return
    

        c.execute("INSERT INTO BR VALUES (?, ?, ?)",
                  (code_br, date, Num_fournisseur))
        
        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=add_br_frame)

        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_br.delete(0, END)
        

        code_br_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_fournisseur_combobox.set("")

        conn.commit()
        conn.close()
    
    save_button = Button(add_br_frame, text="Ajouter", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_BR)
    save_button.place(x=610,y=500)

    def annuler():
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_br.delete(0, END)
     

        code_br_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_fournisseur_combobox.set("")
        e_code_entre.delete(0, tk.END)
        e_qte_ent.delete(0, tk.END)
        e_prix_ent.delete(0, tk.END)   
        e_code_combobox.set("")


    exit_button = Button(add_br_frame, text="Annuler",  width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=150,y=500)

    tableau = None


    def ajouter_ligne():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        # Récupération des valeurs saisies par l'utilisateur
        code_entre = e_code_entre.get()
        qte_ent = int(e_qte_ent.get())
        prix_ent = float(e_prix_ent.get())
        montant_ent = qte_ent * prix_ent
        code_br = e_code_br.get()
        code_article = e_code_combobox.get()

        # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM Entrées WHERE code_ent=?", (code_entre,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le code d'entrée existe déjà dans la base de données", parent=add_br_frame)
            return

        #Vérifier si tous les champs sont remplis
        if not code_entre or not qte_ent or not prix_ent or not montant_ent or not code_br or not code_article:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_br_frame)
            return
    
        # Insertion des données dans la base de données
        c.execute("INSERT INTO Entrées VALUES (?, ?, ?, ?, ?, ?)",
                (code_entre, qte_ent, prix_ent, montant_ent, code_br, code_article))


        c.execute("""
        UPDATE ARTICLE
        SET Quantité = Quantité + (SELECT Quantité_ent FROM entrées WHERE entrées.code_ent = ?),
        prix = (SELECT Prix_ent FROM entrées WHERE entrées.code_ent = ?),
        montant = (Quantité + (SELECT Quantité_ent FROM entrées WHERE entrées.code_ent = ?))*(SELECT Prix_ent FROM entrées WHERE entrées.code_ent = ?)
        WHERE code_article = ?
        """, (code_entre,code_entre,code_entre,code_entre,code_article,))
        conn.commit()
        conn.close()
    
        # Ajout des données dans le tableau
        tableau.insert("", tk.END, values=(code_entre, qte_ent, prix_ent, montant_ent, code_br, code_article))
    
        # Effacement des champs de saisie
        e_code_entre.delete(0, tk.END)
        e_qte_ent.delete(0, tk.END)
        e_prix_ent.delete(0, tk.END)   
        e_code_combobox.set("")

    # Création du tableau
    tableau = tk.ttk.Treeview(add_br_frame, columns=("code_entre", "qte_ent", "prix_ent", "montant_ent", "code_br", "code_article"))

    # Configuration des colonnes
    tableau.column("#0", width=0, stretch=tk.NO)
    tableau.column("code_entre", width=100)
    tableau.column("qte_ent", width=100)
    tableau.column("prix_ent", width=100)
    tableau.column("montant_ent", width=100)
    tableau.column("code_br", width=100)
    tableau.column("code_article", width=100)

    # Titres des colonnes
    tableau.heading("code_entre", text="Code Entrée")
    tableau.heading("qte_ent", text="Quantité Entrée")
    tableau.heading("prix_ent", text="Prix Entrée")
    tableau.heading("montant_ent", text="Montant Entrée")
    tableau.heading("code_br", text="Code BR")
    tableau.heading("code_article", text="Code Article")

    # Ajout d'une ligne vide pour la saisie
    tableau.insert("", tk.END, values=("", "", "", "", "", ""))

    # Placement du tableau dans la fenêtre
    tableau.place(x=150, y=250)
    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT code_article FROM ARTICLE WHERE Code_catg = 'MP'")
    values2 = [row[0] for row in c.fetchall()]

    # Création des champs de saisie
    e_code_entre = tk.Entry(add_br_frame)
    e_qte_ent = tk.Entry(add_br_frame)
    e_prix_ent = tk.Entry(add_br_frame)
    e_code_br = tk.Entry(add_br_frame)
    e_code_combobox = ttk.Combobox(add_br_frame, text="Code Article",width='15', state='readonly', values=values2)


    


    # Placement des champs de saisie dans la fenêtre
    e_code_entre.place(x=150, y=220)
    e_qte_ent.place(x=250, y=220)
    e_prix_ent.place(x=350, y=220)
    e_code_br.place(x=450, y=220)
    e_code_combobox.place(x=550, y=219)

    # Création des étiquettes pour les champs de saisie
    tk.Label(add_br_frame, text="Code Entrée",bg="#067790").place(x=150, y=195)
    tk.Label(add_br_frame, text="Quantité Entrée",bg="#067790").place(x=250, y=195)
    tk.Label(add_br_frame, text="Prix Entrée",bg="#067790").place(x=350, y=195)
    tk.Label(add_br_frame, text="Code BR",bg="#067790").place(x=450, y=195)
    tk.Label(add_br_frame, text="Code Article",bg="#067790").place(x=550, y=195)

    # Bouton pour ajouter une ligne
    btn_ajouter = tk.Button(add_br_frame, text="Ajouter Entré",width='10', bg='#ACE5F3',cursor='hand2', command=ajouter_ligne)
    btn_ajouter.place(x=670, y=218)

    def update_fields(event):
        value = code_br_entry.get()
        e_code_br.delete(0, END)
        e_code_br.insert(0, value)

    code_br_entry.bind("<KeyRelease>", update_fields)

    def annuler():
        Num_fournisseur_combobox.set("")
        add_br_window.destroy()

    exit_button = Button(add_br_window, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)   

#============================================Ajouter BR PDR=========================================
def AjouterBR_PDR():
    add_br_window = tk.Toplevel()
    add_br_window.title("Ajouter BR")
    add_br_window.state('zoomed')
    # add_br_window.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    add_br_window.resizable(0,0)
    add_br_window.config(bg="#ACE5F3")
    add_br_frame = Frame(add_br_window,bg='#067790', width='900', height='600')
    add_br_frame.place(x=200, y=30)

    add_br_window.geometry("1300x700")
    


    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT Num_fournisseur FROM Fournisseurs")
    values = [row[0] for row in c.fetchall()]

    label = Label(add_br_frame, text="BON DE RECEPTION ",bg='#067790',font=('yu gothic ui', 20,'bold'),fg='white')
    label.place(x=15, y=10)
    
    code_br_label = Label(add_br_frame, text="Code BR :",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    code_br_label.place(x=380, y=70)

    code_br_entry = Entry(add_br_frame, highlightthickness=0, relief=FLAT, bg='#067790', fg='black',font=('yu gothic ui',12,'bold'))
    code_br_entry.place(x=465, y=70, width=90)

    code_br_line =Canvas(add_br_frame, width=90, height=2.0,bg='white',highlightthickness=0)
    code_br_line.place(x=465, y=93)

    date_label = Label(add_br_frame, text="Date : ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    date_label.place(x=700, y=120)

    date_entry = DateEntry(add_br_frame, width=1, background='#067790', foreground='white', borderwidth=1, font=('yu gothic ui',12,'bold'), date_pattern="dd/mm/yyyy")
    date_entry.place(x=750, y=120, width=130)


    nom_label = Label(add_br_frame, text="Fournisseur :",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    nom_label.place(x=30, y=120)

    Num_fournisseur_combobox = ttk.Combobox(add_br_frame, text="Num fournisseur",width='15', state='readonly', values=values)
    Num_fournisseur_combobox.place(x=135, y=125, width=120)

    nom_line =Canvas(add_br_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    nom_line.place(x=135, y=145)

    conn.close()

    def save_BR():

        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        code_br = code_br_entry.get()
        date = date_entry.get()
        Num_fournisseur = Num_fournisseur_combobox.get()
    
        #Vérifier si tous les champs sont remplis
        if not code_br or not date or not Num_fournisseur:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_br_frame)
            return
    

        c.execute("INSERT INTO BR VALUES (?, ?, ?)",
                  (code_br, date, Num_fournisseur))
        
        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=add_br_frame)

        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_br.delete(0, END)
        

        code_br_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_fournisseur_combobox.set("")

        conn.commit()
        conn.close()
    
    save_button = Button(add_br_frame, text="Ajouter", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_BR)
    save_button.place(x=610,y=500)

    def annuler():
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_br.delete(0, END)
        

        code_br_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_fournisseur_combobox.set("")
        e_code_entre.delete(0, tk.END)
        e_qte_ent.delete(0, tk.END)
        e_prix_ent.delete(0, tk.END)   
        e_code_combobox.set("")


    exit_button = Button(add_br_frame, text="Annuler",  width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=150,y=500)

    
    tableau = None

    def ajouter_ligne():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        # Récupération des valeurs saisies par l'utilisateur
        code_entre = e_code_entre.get()
        qte_ent = int(e_qte_ent.get())
        prix_ent = float(e_prix_ent.get())
        montant_ent = qte_ent * prix_ent
        code_br = e_code_br.get()
        code_article = e_code_combobox.get()

        # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM Entrées WHERE code_ent=?", (code_entre,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le code d'entrée existe déjà dans la base de données", parent=add_br_frame)
            return

        #Vérifier si tous les champs sont remplis
        if not code_entre or not qte_ent or not prix_ent or not montant_ent or not code_br or not code_article:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_br_frame)
            return
    
        # Insertion des données dans la base de données
        c.execute("INSERT INTO Entrées VALUES (?, ?, ?, ?, ?, ?)",
                (code_entre, qte_ent, prix_ent, montant_ent, code_br, code_article))


        c.execute("""
        UPDATE ARTICLE
        SET Quantité = Quantité + (SELECT Quantité_ent FROM entrées WHERE entrées.code_ent = ?),
        prix = (SELECT Prix_ent FROM entrées WHERE entrées.code_ent = ?),
        montant = (Quantité + (SELECT Quantité_ent FROM entrées WHERE entrées.code_ent = ?))*(SELECT Prix_ent FROM entrées WHERE entrées.code_ent = ?)
        WHERE code_article = ?
        """, (code_entre,code_entre,code_entre,code_entre,code_article,))
        conn.commit()
        conn.close()
    
        # Ajout des données dans le tableau
        tableau.insert("", tk.END, values=(code_entre, qte_ent, prix_ent, montant_ent, code_br, code_article))
    
        # Effacement des champs de saisie
        e_code_entre.delete(0, tk.END)
        e_qte_ent.delete(0, tk.END)
        e_prix_ent.delete(0, tk.END)   
        e_code_combobox.set("")

    # Création du tableau
    tableau = tk.ttk.Treeview(add_br_frame, columns=("code_entre", "qte_ent", "prix_ent", "montant_ent", "code_br", "code_article"))

    # Configuration des colonnes
    tableau.column("#0", width=0, stretch=tk.NO)
    tableau.column("code_entre", width=100)
    tableau.column("qte_ent", width=100)
    tableau.column("prix_ent", width=100)
    tableau.column("montant_ent", width=100)
    tableau.column("code_br", width=100)
    tableau.column("code_article", width=100)

    # Titres des colonnes
    tableau.heading("code_entre", text="Code Entrée")
    tableau.heading("qte_ent", text="Quantité Entrée")
    tableau.heading("prix_ent", text="Prix Entrée")
    tableau.heading("montant_ent", text="Montant Entrée")
    tableau.heading("code_br", text="Code BR")
    tableau.heading("code_article", text="Code Article")

    # Ajout d'une ligne vide pour la saisie
    tableau.insert("", tk.END, values=("", "", "", "", "", ""))

    # Placement du tableau dans la fenêtre
    tableau.place(x=150, y=250)
    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT code_article FROM ARTICLE WHERE Code_catg = 'PDR'")
    values2 = [row[0] for row in c.fetchall()]

    # Création des champs de saisie
    e_code_entre = tk.Entry(add_br_frame)
    e_qte_ent = tk.Entry(add_br_frame)
    e_prix_ent = tk.Entry(add_br_frame)
    e_code_br = tk.Entry(add_br_frame)
    e_code_combobox = ttk.Combobox(add_br_frame, text="Code Article",width='15', state='readonly', values=values2)


    


    # Placement des champs de saisie dans la fenêtre
    e_code_entre.place(x=150, y=220)
    e_qte_ent.place(x=250, y=220)
    e_prix_ent.place(x=350, y=220)
    e_code_br.place(x=450, y=220)
    e_code_combobox.place(x=550, y=219)

    # Création des étiquettes pour les champs de saisie
    tk.Label(add_br_frame, text="Code Entrée",bg="#067790").place(x=150, y=195)
    tk.Label(add_br_frame, text="Quantité Entrée",bg="#067790").place(x=250, y=195)
    tk.Label(add_br_frame, text="Prix Entrée",bg="#067790").place(x=350, y=195)
    tk.Label(add_br_frame, text="Code BR",bg="#067790").place(x=450, y=195)
    tk.Label(add_br_frame, text="Code Article",bg="#067790").place(x=550, y=195)

    # Bouton pour ajouter une ligne
    btn_ajouter = tk.Button(add_br_frame, text="Ajouter Entré",width='10', bg='#ACE5F3',cursor='hand2', command=ajouter_ligne)
    btn_ajouter.place(x=670, y=218)

    def update_fields(event):
        value = code_br_entry.get()
        e_code_br.delete(0, END)
        e_code_br.insert(0, value)

    code_br_entry.bind("<KeyRelease>", update_fields)

    def annuler():
        add_br_window.destroy()

    exit_button = Button(add_br_window, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)   

#==============================================Ajouter BR FB=========================================
def AjouterBR_FB():
    add_br_window = tk.Toplevel()
    add_br_window.title("Ajouter BR")
    add_br_window.state('zoomed')
    # add_br_window.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    add_br_window.resizable(0,0)
    add_br_window.config(bg="#ACE5F3")
    add_br_frame = Frame(add_br_window,bg='#067790', width='900', height='600')
    add_br_frame.place(x=200, y=30)

    add_br_window.geometry("1300x700")
    


    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT Num_fournisseur FROM Fournisseurs")
    values = [row[0] for row in c.fetchall()]

    label = Label(add_br_frame, text="BON DE RECEPTION ",bg='#067790',font=('yu gothic ui', 20,'bold'),fg='white')
    label.place(x=15, y=10)
    
    code_br_label = Label(add_br_frame, text="Code BR :",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    code_br_label.place(x=380, y=70)

    code_br_entry = Entry(add_br_frame, highlightthickness=0, relief=FLAT, bg='#067790', fg='black',font=('yu gothic ui',12,'bold'))
    code_br_entry.place(x=465, y=70, width=90)

    code_br_line =Canvas(add_br_frame, width=90, height=2.0,bg='white',highlightthickness=0)
    code_br_line.place(x=465, y=93)

    date_label = Label(add_br_frame, text="Date : ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    date_label.place(x=700, y=120)

    date_entry = DateEntry(add_br_frame, width=1, background='#067790', foreground='white', borderwidth=1, font=('yu gothic ui',12,'bold'))
    date_entry.place(x=750, y=120, width=130)


    nom_label = Label(add_br_frame, text="Fournisseur    :",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    nom_label.place(x=30, y=120)

    Num_fournisseur_combobox = ttk.Combobox(add_br_frame, text="Num fournisseur",width='15', state='readonly', values=values)
    Num_fournisseur_combobox.place(x=135, y=125, width=120)

    nom_line =Canvas(add_br_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    nom_line.place(x=135, y=145)

    conn.close()

    def save_BR():

        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        code_br = code_br_entry.get()
        date = date_entry.get()
        Num_fournisseur = Num_fournisseur_combobox.get()
    
        #Vérifier si tous les champs sont remplis
        if not code_br or not date or not Num_fournisseur:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_br_frame)
            return
    

        c.execute("INSERT INTO BR VALUES (?, ?, ?)",
                  (code_br, date, Num_fournisseur))

        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=add_br_frame)

        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_br.delete(0, END)
        

        code_br_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_fournisseur_combobox.set("")

        conn.commit()
        conn.close()
    
    save_button = Button(add_br_frame, text="Ajouter", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_BR)
    save_button.place(x=610,y=500)

    def annuler():
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_br.delete(0, END)
        

        code_br_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_fournisseur_combobox.set("")
        e_code_entre.delete(0, tk.END)
        e_qte_ent.delete(0, tk.END)
        e_prix_ent.delete(0, tk.END)   
        e_code_combobox.set("")


    exit_button = Button(add_br_frame, text="Annuler",  width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=150,y=500)

    
    tableau = None

    def ajouter_ligne():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        # Récupération des valeurs saisies par l'utilisateur
        code_entre = e_code_entre.get()
        qte_ent = int(e_qte_ent.get())
        prix_ent = float(e_prix_ent.get())
        montant_ent = qte_ent * prix_ent
        code_br = e_code_br.get()
        code_article = e_code_combobox.get()

        # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM Entrées WHERE code_ent=?", (code_entre,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le code d'entrée existe déjà dans la base de données", parent=add_br_frame)
            return

        #Vérifier si tous les champs sont remplis
        if not code_entre or not qte_ent or not prix_ent or not montant_ent or not code_br or not code_article:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_br_frame)
            return
    
        # Insertion des données dans la base de données
        c.execute("INSERT INTO Entrées VALUES (?, ?, ?, ?, ?, ?)",
                (code_entre, qte_ent, prix_ent, montant_ent, code_br, code_article))


        c.execute("""
        UPDATE ARTICLE
        SET Quantité = Quantité + (SELECT Quantité_ent FROM entrées WHERE entrées.code_ent = ?),
        prix = (SELECT Prix_ent FROM entrées WHERE entrées.code_ent = ?),
        montant = (Quantité + (SELECT Quantité_ent FROM entrées WHERE entrées.code_ent = ?))*(SELECT Prix_ent FROM entrées WHERE entrées.code_ent = ?)
        WHERE code_article = ?
        """, (code_entre,code_entre,code_entre,code_entre,code_article,))
        conn.commit()
        conn.close()
    
        # Ajout des données dans le tableau
        tableau.insert("", tk.END, values=(code_entre, qte_ent, prix_ent, montant_ent, code_br, code_article))
    
        # Effacement des champs de saisie
        e_code_entre.delete(0, tk.END)
        e_qte_ent.delete(0, tk.END)
        e_prix_ent.delete(0, tk.END)   
        e_code_combobox.set("")

    # Création du tableau
    tableau = tk.ttk.Treeview(add_br_frame, columns=("code_entre", "qte_ent", "prix_ent", "montant_ent", "code_br", "code_article"))

    # Configuration des colonnes
    tableau.column("#0", width=0, stretch=tk.NO)
    tableau.column("code_entre", width=100)
    tableau.column("qte_ent", width=100)
    tableau.column("prix_ent", width=100)
    tableau.column("montant_ent", width=100)
    tableau.column("code_br", width=100)
    tableau.column("code_article", width=100)

    # Titres des colonnes
    tableau.heading("code_entre", text="Code Entrée")
    tableau.heading("qte_ent", text="Quantité Entrée")
    tableau.heading("prix_ent", text="Prix Entrée")
    tableau.heading("montant_ent", text="Montant Entrée")
    tableau.heading("code_br", text="Code BR")
    tableau.heading("code_article", text="Code Article")

    # Ajout d'une ligne vide pour la saisie
    tableau.insert("", tk.END, values=("", "", "", "", "", ""))

    # Placement du tableau dans la fenêtre
    tableau.place(x=150, y=250)
    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT code_article FROM ARTICLE WHERE Code_catg = 'FB'")
    values2 = [row[0] for row in c.fetchall()]

    # Création des champs de saisie
    e_code_entre = tk.Entry(add_br_frame)
    e_qte_ent = tk.Entry(add_br_frame)
    e_prix_ent = tk.Entry(add_br_frame)
    e_code_br = tk.Entry(add_br_frame)
    e_code_combobox = ttk.Combobox(add_br_frame, text="Code Article",width='15', state='readonly', values=values2)


    


    # Placement des champs de saisie dans la fenêtre
    e_code_entre.place(x=150, y=220)
    e_qte_ent.place(x=250, y=220)
    e_prix_ent.place(x=350, y=220)
    e_code_br.place(x=450, y=220)
    e_code_combobox.place(x=550, y=219)

    # Création des étiquettes pour les champs de saisie
    tk.Label(add_br_frame, text="Code Entrée",bg="#067790").place(x=150, y=195)
    tk.Label(add_br_frame, text="Quantité Entrée",bg="#067790").place(x=250, y=195)
    tk.Label(add_br_frame, text="Prix Entrée",bg="#067790").place(x=350, y=195)
    tk.Label(add_br_frame, text="Code BR",bg="#067790").place(x=450, y=195)
    tk.Label(add_br_frame, text="Code Article",bg="#067790").place(x=550, y=195)

    # Bouton pour ajouter une ligne
    btn_ajouter = tk.Button(add_br_frame, text="Ajouter Entré",width='10', bg='#ACE5F3',cursor='hand2', command=ajouter_ligne)
    btn_ajouter.place(x=670, y=218)

    def update_fields(event):
        value = code_br_entry.get()
        e_code_br.delete(0, END)
        e_code_br.insert(0, value)

    code_br_entry.bind("<KeyRelease>", update_fields)

    def annuler():
        add_br_window.destroy()

    exit_button = Button(add_br_window, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)   


#=============================================Ajouter BR PF=============================================    
def AjouterBR_PF():
    add_br_window = tk.Toplevel()
    add_br_window.title("Ajouter BR")
    add_br_window.state('zoomed') 
    # add_br_window.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    add_br_window.resizable(0,0)
    add_br_window.config(bg="#ACE5F3")
    add_br_frame = Frame(add_br_window,bg='#067790', width='900', height='600')
    add_br_frame.place(x=200, y=30)

    add_br_window.geometry("1300x700")

    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT Num_carte FROM Employé WHERE Département='Production'")
    values = [row[0] for row in c.fetchall()]

    label = Label(add_br_frame, text="BON DE RECEPTION ",bg='#067790',font=('yu gothic ui', 20,'bold'),fg='white')
    label.place(x=15, y=10)
    
    code_br_label = Label(add_br_frame, text="Code BR :",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    code_br_label.place(x=380, y=70)

    code_br_entry = Entry(add_br_frame, highlightthickness=0, relief=FLAT, bg='#067790', fg='black',font=('yu gothic ui',12,'bold'))
    code_br_entry.place(x=465, y=70, width=90)

    code_br_line =Canvas(add_br_frame, width=90, height=2.0,bg='white',highlightthickness=0)
    code_br_line.place(x=465, y=93)

    date_label = Label(add_br_frame, text="Date : ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    date_label.place(x=700, y=120)

    date_entry = DateEntry(add_br_frame, width=1, background='#067790', foreground='white', borderwidth=1, font=('yu gothic ui',12,'bold'))
    date_entry.place(x=750, y=120, width=130)


    nom_label = Label(add_br_frame, text="Employé:",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    nom_label.place(x=30, y=120)

    Num_carte_combobox = ttk.Combobox(add_br_frame, text="Num carte",width='15', state='readonly', values=values)
    Num_carte_combobox.place(x=135, y=125, width=120)

    nom_line =Canvas(add_br_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    nom_line.place(x=135, y=145)

    conn.close()

    def save_BR():

        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        code_br = code_br_entry.get()
        date = date_entry.get()
        Num_carte = Num_carte_combobox.get()

        #Vérifier si tous les champs sont remplis
        if not code_br or not date or not Num_carte:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_br_frame)
            return
    

        c.execute("INSERT INTO BR VALUES (?, ?, ?)",
                  (code_br, date, Num_carte))
        
        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=add_br_frame)

        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_br.delete(0, END)

        code_br_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_carte_combobox.set("")
        

        conn.commit()
        conn.close()
    
    save_button = Button(add_br_frame, text="Ajouter", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_BR)
    save_button.place(x=610,y=500)

    def annuler():
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_br.delete(0, END)
        code_br_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_carte_combobox.set("")
        e_code_entre.delete(0, tk.END)
        e_qte_ent.delete(0, tk.END)
        e_prix_ent.delete(0, tk.END)   
        e_code_combobox.set("")


    exit_button = Button(add_br_frame, text="Annuler",  width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=150,y=500)

    
    tableau = None

    def ajouter_ligne():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        # Récupération des valeurs saisies par l'utilisateur
        code_entre = e_code_entre.get()
        qte_ent = int(e_qte_ent.get())
        prix_ent = float(e_prix_ent.get())
        montant_ent = qte_ent * prix_ent
        code_br = e_code_br.get()
        code_article = e_code_combobox.get()

        # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM Entrées WHERE code_ent=?", (code_entre,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le code d'entrée existe déjà dans la base de données", parent=add_br_frame)
            return

        #Vérifier si tous les champs sont remplis
        if not code_entre or not qte_ent or not prix_ent or not montant_ent or not code_br or not code_article:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_br_frame)
            return
    
        # Insertion des données dans la base de données
        c.execute("INSERT INTO Entrées VALUES (?, ?, ?, ?, ?, ?)",
                (code_entre, qte_ent, prix_ent, montant_ent, code_br, code_article))


        c.execute("""
        UPDATE ARTICLE
        SET Quantité = Quantité + (SELECT Quantité_ent FROM entrées WHERE entrées.code_ent = ?),
        prix = (SELECT Prix_ent FROM entrées WHERE entrées.code_ent = ?),
        montant = (Quantité + (SELECT Quantité_ent FROM entrées WHERE entrées.code_ent = ?))*(SELECT Prix_ent FROM entrées WHERE entrées.code_ent = ?)
        WHERE code_article = ?
        """, (code_entre,code_entre,code_entre,code_entre,code_article,))
        conn.commit()
        conn.close()
    
        # Ajout des données dans le tableau
        tableau.insert("", tk.END, values=(code_entre, qte_ent, prix_ent, montant_ent, code_br, code_article))
    
        # Effacement des champs de saisie
        e_code_entre.delete(0, tk.END)
        e_qte_ent.delete(0, tk.END)
        e_prix_ent.delete(0, tk.END)   
        e_code_combobox.set("")

    # Création du tableau
    tableau = tk.ttk.Treeview(add_br_frame, columns=("code_entre", "qte_ent", "prix_ent", "montant_ent", "code_br", "code_article"))

    # Configuration des colonnes
    tableau.column("#0", width=0, stretch=tk.NO)
    tableau.column("code_entre", width=100)
    tableau.column("qte_ent", width=100)
    tableau.column("prix_ent", width=100)
    tableau.column("montant_ent", width=100)
    tableau.column("code_br", width=100)
    tableau.column("code_article", width=100)

    # Titres des colonnes
    tableau.heading("code_entre", text="Code Entrée")
    tableau.heading("qte_ent", text="Quantité Entrée")
    tableau.heading("prix_ent", text="Prix Entrée")
    tableau.heading("montant_ent", text="Montant Entrée")
    tableau.heading("code_br", text="Code BR")
    tableau.heading("code_article", text="Code Article")

    # Ajout d'une ligne vide pour la saisie
    tableau.insert("", tk.END, values=("", "", "", "", "", ""))

    # Placement du tableau dans la fenêtre
    tableau.place(x=150, y=250)
    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT code_article FROM ARTICLE WHERE Code_catg='PF' ")
    values2 = [row[0] for row in c.fetchall()]

    # Création des champs de saisie
    e_code_entre = tk.Entry(add_br_frame)
    e_qte_ent = tk.Entry(add_br_frame)
    e_prix_ent = tk.Entry(add_br_frame)
    e_code_br = tk.Entry(add_br_frame)
    e_code_combobox = ttk.Combobox(add_br_frame, text="Code Article",width='15', state='readonly', values=values2)


    


    # Placement des champs de saisie dans la fenêtre
    e_code_entre.place(x=150, y=220)
    e_qte_ent.place(x=250, y=220)
    e_prix_ent.place(x=350, y=220)
    e_code_br.place(x=450, y=220)
    e_code_combobox.place(x=550, y=219)

    # Création des étiquettes pour les champs de saisie
    tk.Label(add_br_frame, text="Code Entrée",bg="#067790").place(x=150, y=195)
    tk.Label(add_br_frame, text="Quantité Entrée",bg="#067790").place(x=250, y=195)
    tk.Label(add_br_frame, text="Prix Entrée",bg="#067790").place(x=350, y=195)
    tk.Label(add_br_frame, text="Code BR",bg="#067790").place(x=450, y=195)
    tk.Label(add_br_frame, text="Code Article",bg="#067790").place(x=550, y=195)

    # Bouton pour ajouter une ligne
    btn_ajouter = tk.Button(add_br_frame, text="Ajouter Entré",width='10', bg='#ACE5F3',cursor='hand2', command=ajouter_ligne)
    btn_ajouter.place(x=670, y=218)

    def update_fields(event):
        value = code_br_entry.get()
        e_code_br.delete(0, END)
        e_code_br.insert(0, value)

    code_br_entry.bind("<KeyRelease>", update_fields) 

    def annuler():
        add_br_window.destroy()

    exit_button = Button(add_br_window, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)   

#===========================================Ajouter BSM====================================================
def AjouterBSM():

    add_bsm_window = tk.Toplevel()
    add_bsm_window.title("Ajouter BSM")
    add_bsm_window.state('zoomed')   
    # add_bsm_window.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico') 
    add_bsm_window.resizable(0,0)
    add_bsm_window.config(bg="#ACE5F3")
    add_bsm_frame = Frame(add_bsm_window,bg='#067790', width='900', height='600')
    add_bsm_frame.place(x=200, y=30)

    add_bsm_window.geometry("1300x700")


    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT Num_carte FROM Employé")
    values = [row[0] for row in c.fetchall()]

    label = Label(add_bsm_frame, text="BON DE SORTIE ",bg='#067790',font=('yu gothic ui', 20,'bold'),fg='white')
    label.place(x=15, y=10)
    
    code_bsm_label = Label(add_bsm_frame, text="Code BSM:",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    code_bsm_label.place(x=380, y=70)

    code_bsm_entry = Entry(add_bsm_frame, highlightthickness=0, relief=FLAT, bg='#067790', fg='black',font=('yu gothic ui',12,'bold'))
    code_bsm_entry.place(x=465, y=70, width=90)

    code_bsm_line =Canvas(add_bsm_frame, width=90, height=2.0,bg='white',highlightthickness=0)
    code_bsm_line.place(x=465, y=93)

    date_label = Label(add_bsm_frame, text="Date : ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    date_label.place(x=700, y=120)

    date_entry = DateEntry(add_bsm_frame, width=1, background='#067790', foreground='white', borderwidth=1, font=('yu gothic ui',12,'bold'), state='readonly')
    date_entry.place(x=750, y=120, width=130)


    nom_label = Label(add_bsm_frame, text="Employé :",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    nom_label.place(x=30, y=120)

    Num_carte_combobox = ttk.Combobox(add_bsm_frame, text="Numéro carte",width='15', state='readonly', values=values)
    Num_carte_combobox.place(x=135, y=125, width=120)

    nom_line =Canvas(add_bsm_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    nom_line.place(x=135, y=145)

    conn.close()

    def save_BSM():

        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        code_bsm = code_bsm_entry.get()
        date = date_entry.get()
        Num_carte = Num_carte_combobox.get()

        #Vérifier si tous les champs sont remplis
        if not code_bsm or not date or not Num_carte:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_bsm_frame)
            return
    

        c.execute("INSERT INTO BSM VALUES (?, ?, ?)",
                  (code_bsm, date, Num_carte))

        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=add_bsm_frame)

        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_bsm.delete(0, END)
        

        code_bsm_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_carte_combobox.set("")

        e_code_sort.delete(0, tk.END)
        e_qte_sort.delete(0, tk.END)
        e_prix_sort.delete(0, tk.END)   
        e_code_combobox.set("")
        

        conn.commit()
        conn.close()
    
    save_button = Button(add_bsm_frame, text="Ajouter", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_BSM)
    save_button.place(x=610,y=500)

    def annuler():
        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_bsm.delete(0, END)
        code_bsm_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_carte_combobox.set("")
        e_code_sort.delete(0, tk.END)
        e_qte_sort.delete(0, tk.END)
        e_prix_sort.delete(0, tk.END)   
        e_code_combobox.set("")


    exit_button = Button(add_bsm_frame, text="Annuler",  width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=150,y=500)

    tableau = None


    def ajouter_ligne():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        # Récupération des valeurs saisies par l'utilisateur
        code_sort = e_code_sort.get()
        qte_sort = int(e_qte_sort.get())
        prix_sort = float(e_prix_sort.get())
        montant_sort = qte_sort * prix_sort
        code_bsm = e_code_bsm.get()
        code_article = e_code_combobox.get()

        # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM SORTIES WHERE code_sort=?", (code_sort,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le code de sortie existe déjà dans la base de données", parent=add_bsm_window)
            return

        #Vérifier si tous les champs sont remplis
        if not code_sort or not qte_sort or not prix_sort or not montant_sort or not code_bsm or not code_article:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_bsm_window)
            return

        # Vérification de la quantité disponible dans le stock
        c.execute("SELECT Quantité FROM Article WHERE code_article = ?", (code_article,))
        qte_dispo = c.fetchone()[0]
        if qte_sort > qte_dispo:
            messagebox.showerror(title="Erreur", message=f"La quantité disponible pour l'article {code_article} est insuffisante pour effectuer une sortie de {qte_sort} unité(s).", parent=add_bsm_frame)
            return
    
        # Insertion des données dans la base de données
        c.execute("INSERT INTO Sorties VALUES (?, ?, ?, ?, ?, ?)",
                (code_sort, qte_sort, prix_sort, montant_sort, code_bsm, code_article))


        c.execute("""
        UPDATE Article
        SET Quantité = Quantité - ?,
            prix = ?,
            montant = (Quantité - ?) * ?
        WHERE code_article = ?
        """, (qte_sort, prix_sort, qte_sort, prix_sort, code_article,))


        conn.commit()
        conn.close()
    
        # Ajout des données dans le tableau
        tableau.insert("", tk.END, values=(code_sort, qte_sort, prix_sort, montant_sort, code_bsm, code_article))
    
        # Effacement des champs de saisie
        e_code_sort.delete(0, tk.END)
        e_qte_sort.delete(0, tk.END)
        e_prix_sort.delete(0, tk.END)   
        e_code_combobox.set("")

    # Création du tableau
    tableau = tk.ttk.Treeview(add_bsm_frame, columns=("code_sort", "qte_sort", "prix_sort", "montant_sort", "code_bsm", "code_article"))

    # Configuration des colonnes
    tableau.column("#0", width=0, stretch=tk.NO)
    tableau.column("code_sort", width=100)
    tableau.column("qte_sort", width=100)
    tableau.column("prix_sort", width=100)
    tableau.column("montant_sort", width=100)
    tableau.column("code_bsm", width=100)
    tableau.column("code_article", width=100)

    # Titres des colonnes
    tableau.heading("code_sort", text="Code Sortie")
    tableau.heading("qte_sort", text="Quantité Sortie")
    tableau.heading("prix_sort", text="Prix Sortie")
    tableau.heading("montant_sort", text="Montant Sortie")
    tableau.heading("code_bsm", text="Code BSM")
    tableau.heading("code_article", text="Code Article")

    # Ajout d'une ligne vide pour la saisie
    tableau.insert("", tk.END, values=("", "", "", "", "", ""))

    # Placement du tableau dans la fenêtre
    tableau.place(x=150, y=250)
    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT code_article FROM ARTICLE")
    values2 = [row[0] for row in c.fetchall()]

    # Création des champs de saisie
    e_code_sort = tk.Entry(add_bsm_frame)
    e_qte_sort = tk.Entry(add_bsm_frame)
    e_prix_sort = tk.Entry(add_bsm_frame)
    e_code_bsm = tk.Entry(add_bsm_frame)
    e_code_combobox = ttk.Combobox(add_bsm_frame, text="Code Article",width='15', state='readonly', values=values2)


    


    # Placement des champs de saisie dans la fenêtre
    e_code_sort.place(x=150, y=220)
    e_qte_sort.place(x=250, y=220)
    e_prix_sort.place(x=350, y=220)
    e_code_bsm.place(x=450, y=220)
    e_code_combobox.place(x=550, y=219)

    # Création des étiquettes pour les champs de saisie
    tk.Label(add_bsm_frame, text="Code Sortie",bg="#067790").place(x=150, y=195)
    tk.Label(add_bsm_frame, text="Quantité Sortie",bg="#067790").place(x=250, y=195)
    tk.Label(add_bsm_frame, text="Prix Sorties",bg="#067790").place(x=350, y=195)
    tk.Label(add_bsm_frame, text="Code BSM",bg="#067790").place(x=450, y=195)
    tk.Label(add_bsm_frame, text="Code Article",bg="#067790").place(x=550, y=195)

    # Bouton pour ajouter une ligne
    btn_ajouter = tk.Button(add_bsm_frame, text="Ajouter Sortie",width='10', bg='#ACE5F3',cursor='hand2', command=ajouter_ligne)
    btn_ajouter.place(x=670, y=218)

    def update_fields(event):
        value = code_bsm_entry.get()
        e_code_bsm.delete(0, END)
        e_code_bsm.insert(0, value)

    code_bsm_entry.bind("<KeyRelease>", update_fields)

    def annuler():
        add_bsm_window.destroy()

    exit_button = Button(add_bsm_window, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)
#===========================================Ajouter BSM MP  ====================================
def AjouterBSM_MP():

    add_bsm_window = tk.Toplevel()
    add_bsm_window.title("Ajouter BSM")
    add_bsm_window.state('zoomed') 
    # add_bsm_window.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    add_bsm_window.resizable(0,0)
    add_bsm_window.config(bg="#ACE5F3")
    add_bsm_frame = Frame(add_bsm_window,bg='#067790', width='900', height='600')
    add_bsm_frame.place(x=200, y=30)

    add_bsm_window.geometry("1300x700")


    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT Num_carte FROM Employé")
    values = [row[0] for row in c.fetchall()]

    label = Label(add_bsm_frame, text="BON DE SORTIE ",bg='#067790',font=('yu gothic ui', 20,'bold'),fg='white')
    label.place(x=15, y=10)
    
    code_bsm_label = Label(add_bsm_frame, text="Code BSM:",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    code_bsm_label.place(x=380, y=70)

    code_bsm_entry = Entry(add_bsm_frame, highlightthickness=0, relief=FLAT, bg='#067790', fg='black',font=('yu gothic ui',12,'bold'))
    code_bsm_entry.place(x=465, y=70, width=90)

    code_bsm_line =Canvas(add_bsm_frame, width=90, height=2.0,bg='white',highlightthickness=0)
    code_bsm_line.place(x=465, y=93)

    date_label = Label(add_bsm_frame, text="Date : ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    date_label.place(x=700, y=120)

    date_entry = DateEntry(add_bsm_frame, width=1, background='#067790', foreground='white', borderwidth=1, font=('yu gothic ui',12,'bold'))
    date_entry.place(x=750, y=120, width=130)


    nom_label = Label(add_bsm_frame, text="Employé :",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    nom_label.place(x=30, y=120)

    Num_carte_combobox = ttk.Combobox(add_bsm_frame, text="Numéro carte",width='15', state='readonly', values=values)
    Num_carte_combobox.place(x=125, y=125, width=120)

    nom_line =Canvas(add_bsm_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    nom_line.place(x=125, y=145)

    conn.close()

    def save_BSM():

        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        code_bsm = code_bsm_entry.get()
        date = date_entry.get()
        Num_carte = Num_carte_combobox.get()

        #Vérifier si tous les champs sont remplis
        if not code_bsm or not date or not Num_carte:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_bsm_frame)
            return
    

        c.execute("INSERT INTO BSM VALUES (?, ?, ?)",
                  (code_bsm, date, Num_carte))


        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=add_bsm_frame)

        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_bsm.delete(0, END)
        

        code_bsm_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_carte_combobox.set("")

        conn.commit()
        conn.close()
    
    save_button = Button(add_bsm_frame, text="Ajouter", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_BSM)
    save_button.place(x=610,y=500)

    def annuler():
        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_bsm.delete(0, END)
        code_bsm_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_carte_combobox.set("")
        e_code_sort.delete(0, tk.END)
        e_qte_sort.delete(0, tk.END)
        e_prix_sort.delete(0, tk.END)   
        e_code_combobox.set("")


    exit_button = Button(add_bsm_frame, text="Annuler",  width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=150,y=500)

    tableau = None


    def ajouter_ligne():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        # Récupération des valeurs saisies par l'utilisateur
        code_sort = e_code_sort.get()
        qte_sort = int(e_qte_sort.get())
        prix_sort = float(e_prix_sort.get())
        montant_sort = qte_sort * prix_sort
        code_bsm = e_code_bsm.get()
        code_article = e_code_combobox.get()

        # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM SORTIES WHERE code_sort=?", (code_sort,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le code de sortie existe déjà dans la base de données", parent=add_bsm_frame)
            return

        #Vérifier si tous les champs sont remplis
        if not code_sort or not qte_sort or not prix_sort or not montant_sort or not code_bsm or not code_article:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_bsm_frame)
            return

        # Vérification de la quantité disponible dans le stock
        c.execute("SELECT Quantité FROM Article WHERE code_article = ?", (code_article,))
        qte_dispo = c.fetchone()[0]
        if qte_sort > qte_dispo:
            messagebox.showerror(title="Erreur", message=f"La quantité disponible pour l'article {code_article} est insuffisante pour effectuer une sortie de {qte_sort} unité(s).", parent=add_bsm_frame)
            return

    
        # Insertion des données dans la base de données
        c.execute("INSERT INTO Sorties VALUES (?, ?, ?, ?, ?, ?)",
                (code_sort, qte_sort, prix_sort, montant_sort, code_bsm, code_article))


        c.execute("""
        UPDATE Article
        SET Quantité = Quantité - ?,
            prix = ?,
            montant = (Quantité - ?) * ?
        WHERE code_article = ?
        """, (qte_sort, prix_sort, qte_sort, prix_sort, code_article,))


        conn.commit()
        conn.close()
    
        # Ajout des données dans le tableau
        tableau.insert("", tk.END, values=(code_sort, qte_sort, prix_sort, montant_sort, code_bsm, code_article))
    
        # Effacement des champs de saisie
        e_code_sort.delete(0, tk.END)
        e_qte_sort.delete(0, tk.END)
        e_prix_sort.delete(0, tk.END)   
        e_code_combobox.set("")

    # Création du tableau
    tableau = tk.ttk.Treeview(add_bsm_frame, columns=("code_sort", "qte_sort", "prix_sort", "montant_sort", "code_bsm", "code_article"))

    # Configuration des colonnes
    tableau.column("#0", width=0, stretch=tk.NO)
    tableau.column("code_sort", width=100)
    tableau.column("qte_sort", width=100)
    tableau.column("prix_sort", width=100)
    tableau.column("montant_sort", width=100)
    tableau.column("code_bsm", width=100)
    tableau.column("code_article", width=100)

    # Titres des colonnes
    tableau.heading("code_sort", text="Code Sortie")
    tableau.heading("qte_sort", text="Quantité Sortie")
    tableau.heading("prix_sort", text="Prix Sortie")
    tableau.heading("montant_sort", text="Montant Sortie")
    tableau.heading("code_bsm", text="Code BSM")
    tableau.heading("code_article", text="Code Article")

    # Ajout d'une ligne vide pour la saisie
    tableau.insert("", tk.END, values=("", "", "", "", "", ""))

    # Placement du tableau dans la fenêtre
    tableau.place(x=150, y=250)
    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT code_article FROM ARTICLE WHERE Code_catg='MP'")
    values2 = [row[0] for row in c.fetchall()]

    # Création des champs de saisie
    e_code_sort = tk.Entry(add_bsm_frame)
    e_qte_sort = tk.Entry(add_bsm_frame)
    e_prix_sort = tk.Entry(add_bsm_frame)
    e_code_bsm = tk.Entry(add_bsm_frame)
    e_code_combobox = ttk.Combobox(add_bsm_frame, text="Code Article",width='15', state='readonly', values=values2)


    


    # Placement des champs de saisie dans la fenêtre
    e_code_sort.place(x=150, y=220)
    e_qte_sort.place(x=250, y=220)
    e_prix_sort.place(x=350, y=220)
    e_code_bsm.place(x=450, y=220)
    e_code_combobox.place(x=550, y=219)

    # Création des étiquettes pour les champs de saisie
    tk.Label(add_bsm_frame, text="Code Sortie",bg="#067790").place(x=150, y=195)
    tk.Label(add_bsm_frame, text="Quantité Sortie",bg="#067790").place(x=250, y=195)
    tk.Label(add_bsm_frame, text="Prix Sorties",bg="#067790").place(x=350, y=195)
    tk.Label(add_bsm_frame, text="Code BSM",bg="#067790").place(x=450, y=195)
    tk.Label(add_bsm_frame, text="Code Article",bg="#067790").place(x=550, y=195)

    # Bouton pour ajouter une ligne
    btn_ajouter = tk.Button(add_bsm_frame, text="Ajouter Sortie",width='10', bg='#ACE5F3',cursor='hand2', command=ajouter_ligne)
    btn_ajouter.place(x=670, y=218)

    def update_fields(event):
        value = code_bsm_entry.get()
        e_code_bsm.delete(0, END)
        e_code_bsm.insert(0, value)

    code_bsm_entry.bind("<KeyRelease>", update_fields)  
    def annuler():
        add_bsm_window.destroy()

    exit_button = Button(add_bsm_window, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)
#==========================================Ajouter BSM PDR==================================================
def AjouterBSM_PDR():

    add_bsm_window = tk.Toplevel()
    add_bsm_window.title("Ajouter BSM")
    add_bsm_window.state('zoomed')
    # add_bsm_window.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    add_bsm_window.resizable(0,0)
    add_bsm_window.config(bg="#ACE5F3")
    add_bsm_frame = Frame(add_bsm_window,bg='#067790', width='900', height='600')
    add_bsm_frame.place(x=200, y=30)

    add_bsm_window.geometry("1300x700")


    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT Num_carte FROM Employé")
    values = [row[0] for row in c.fetchall()]

    label = Label(add_bsm_frame, text="BON DE SORTIE ",bg='#067790',font=('yu gothic ui', 20,'bold'),fg='white')
    label.place(x=15, y=10)
    
    code_bsm_label = Label(add_bsm_frame, text="Code BSM:",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    code_bsm_label.place(x=380, y=70)

    code_bsm_entry = Entry(add_bsm_frame, highlightthickness=0, relief=FLAT, bg='#067790', fg='black',font=('yu gothic ui',12,'bold'))
    code_bsm_entry.place(x=465, y=70, width=90)

    code_bsm_line =Canvas(add_bsm_frame, width=90, height=2.0,bg='white',highlightthickness=0)
    code_bsm_line.place(x=465, y=93)

    date_label = Label(add_bsm_frame, text="Date : ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    date_label.place(x=700, y=120)

    date_entry = DateEntry(add_bsm_frame, width=1, background='#067790', foreground='white', borderwidth=1, font=('yu gothic ui',12,'bold'))
    date_entry.place(x=750, y=120, width=130)


    nom_label = Label(add_bsm_frame, text="Employé    :",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    nom_label.place(x=30, y=120)

    Num_carte_combobox = ttk.Combobox(add_bsm_frame, text="Numéro carte",width='15', state='readonly', values=values)
    Num_carte_combobox.place(x=135, y=125, width=120)

    nom_line =Canvas(add_bsm_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    nom_line.place(x=135, y=145)

    conn.close()

    def save_BSM():

        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        code_bsm = code_bsm_entry.get()
        date = date_entry.get()
        Num_carte = Num_carte_combobox.get()

        #Vérifier si tous les champs sont remplis
        if not code_bsm or not date or not Num_carte:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_bsm_frame)
            return
    

        c.execute("INSERT INTO BSM VALUES (?, ?, ?)",
                  (code_bsm, date, Num_carte))

        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=add_bsm_frame)

        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_bsm.delete(0, END)
        

        code_bsm_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_carte_combobox.set("")

        conn.commit()
        conn.close()
    
    save_button = Button(add_bsm_frame, text="Ajouter", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_BSM)
    save_button.place(x=610,y=500)

    def annuler():
        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_bsm.delete(0, END)
        code_bsm_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_carte_combobox.set("")
        e_code_sort.delete(0, tk.END)
        e_qte_sort.delete(0, tk.END)
        e_prix_sort.delete(0, tk.END)   
        e_code_combobox.set("")


    exit_button = Button(add_bsm_frame, text="Annuler",  width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=150,y=500)

    
    tableau = None


    def ajouter_ligne():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        # Récupération des valeurs saisies par l'utilisateur
        code_sort = e_code_sort.get()
        qte_sort = int(e_qte_sort.get())
        prix_sort = float(e_prix_sort.get())
        montant_sort = qte_sort * prix_sort
        code_bsm = e_code_bsm.get()
        code_article = e_code_combobox.get()

        # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM SORTIES WHERE code_sort=?", (code_sort,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le code sortie existe déjà dans la base de données", parent=add_bsm_frame)
            return

        #Vérifier si tous les champs sont remplis
        if not code_sort or not qte_sort or not prix_sort or not montant_sort or not code_bsm or not code_article:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_bsm_frame)
            return
    
        # Vérification de la quantité disponible dans le stock
        c.execute("SELECT Quantité FROM Article WHERE code_article = ?", (code_article,))
        qte_dispo = c.fetchone()[0]
        if qte_sort > qte_dispo:
            messagebox.showerror(title="Erreur", message=f"La quantité disponible pour l'article {code_article} est insuffisante pour effectuer une sortie de {qte_sort} unité(s).", parent=add_bsm_frame)
            return

        # Insertion des données dans la base de données
        c.execute("INSERT INTO Sorties VALUES (?, ?, ?, ?, ?, ?)",
                (code_sort, qte_sort, prix_sort, montant_sort, code_bsm, code_article))


        c.execute("""
        UPDATE Article
        SET Quantité = Quantité - ?,
            prix = ?,
            montant = (Quantité - ?) * ?
        WHERE code_article = ?
        """, (qte_sort, prix_sort, qte_sort, prix_sort, code_article,))
        conn.commit()
        conn.close()
    
        # Ajout des données dans le tableau
        tableau.insert("", tk.END, values=(code_sort, qte_sort, prix_sort, montant_sort, code_bsm, code_article))
    
        # Effacement des champs de saisie
        e_code_sort.delete(0, tk.END)
        e_qte_sort.delete(0, tk.END)
        e_prix_sort.delete(0, tk.END)   
        e_code_combobox.set("")

    # Création du tableau
    tableau = tk.ttk.Treeview(add_bsm_frame, columns=("code_sort", "qte_sort", "prix_sort", "montant_sort", "code_bsm", "code_article"))

    # Configuration des colonnes
    tableau.column("#0", width=0, stretch=tk.NO)
    tableau.column("code_sort", width=100)
    tableau.column("qte_sort", width=100)
    tableau.column("prix_sort", width=100)
    tableau.column("montant_sort", width=100)
    tableau.column("code_bsm", width=100)
    tableau.column("code_article", width=100)

    # Titres des colonnes
    tableau.heading("code_sort", text="Code Sortie")
    tableau.heading("qte_sort", text="Quantité Sortie")
    tableau.heading("prix_sort", text="Prix Sortie")
    tableau.heading("montant_sort", text="Montant Sortie")
    tableau.heading("code_bsm", text="Code BSM")
    tableau.heading("code_article", text="Code Article")

    # Ajout d'une ligne vide pour la saisie
    tableau.insert("", tk.END, values=("", "", "", "", "", ""))

    # Placement du tableau dans la fenêtre
    tableau.place(x=150, y=250)
    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT code_article FROM ARTICLE WHERE Code_catg='PDR'")
    values2 = [row[0] for row in c.fetchall()]

    # Création des champs de saisie
    e_code_sort = tk.Entry(add_bsm_frame)
    e_qte_sort = tk.Entry(add_bsm_frame)
    e_prix_sort = tk.Entry(add_bsm_frame)
    e_code_bsm = tk.Entry(add_bsm_frame)
    e_code_combobox = ttk.Combobox(add_bsm_frame, text="Code Article",width='15', state='readonly', values=values2)


    


    # Placement des champs de saisie dans la fenêtre
    e_code_sort.place(x=150, y=220)
    e_qte_sort.place(x=250, y=220)
    e_prix_sort.place(x=350, y=220)
    e_code_bsm.place(x=450, y=220)
    e_code_combobox.place(x=550, y=219)

    # Création des étiquettes pour les champs de saisie
    tk.Label(add_bsm_frame, text="Code Sortie",bg="#067790").place(x=150, y=195)
    tk.Label(add_bsm_frame, text="Quantité Sortie",bg="#067790").place(x=250, y=195)
    tk.Label(add_bsm_frame, text="Prix Sorties",bg="#067790").place(x=350, y=195)
    tk.Label(add_bsm_frame, text="Code BSM",bg="#067790").place(x=450, y=195)
    tk.Label(add_bsm_frame, text="Code Article",bg="#067790").place(x=550, y=195)

    # Bouton pour ajouter une ligne
    btn_ajouter = tk.Button(add_bsm_frame, text="Ajouter Sortie",width='10', bg='#ACE5F3',cursor='hand2', command=ajouter_ligne)
    btn_ajouter.place(x=670, y=218)

    def update_fields(event):
        value = code_bsm_entry.get()
        e_code_bsm.delete(0, END)
        e_code_bsm.insert(0, value)

    code_bsm_entry.bind("<KeyRelease>", update_fields)      
    def annuler():
        add_bsm_window.destroy()

    exit_button = Button(add_bsm_window, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)
#===========================================Ajouter BSM FB =================================================

def AjouterBSM_FB():

    add_bsm_window = tk.Toplevel()
    add_bsm_window.title("Ajouter BSM")
    add_bsm_window.state('zoomed')  
    # add_bsm_window.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')  
    add_bsm_window.resizable(0,0)
    add_bsm_window.config(bg="#ACE5F3")
    add_bsm_frame = Frame(add_bsm_window,bg='#067790', width='900', height='600')
    add_bsm_frame.place(x=200, y=30)

    add_bsm_window.geometry("1300x700")



    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT Num_carte FROM Employé")
    values = [row[0] for row in c.fetchall()]

    label = Label(add_bsm_frame, text="BON DE SORTIE ",bg='#067790',font=('yu gothic ui', 20,'bold'),fg='white')
    label.place(x=15, y=10)
    
    code_bsm_label = Label(add_bsm_frame, text="Code BSM:",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    code_bsm_label.place(x=380, y=70)

    code_bsm_entry = Entry(add_bsm_frame, highlightthickness=0, relief=FLAT, bg='#067790', fg='black',font=('yu gothic ui',12,'bold'))
    code_bsm_entry.place(x=465, y=70, width=90)

    code_bsm_line =Canvas(add_bsm_frame, width=90, height=2.0,bg='white',highlightthickness=0)
    code_bsm_line.place(x=465, y=93)

    date_label = Label(add_bsm_frame, text="Date : ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    date_label.place(x=700, y=120)

    date_entry = DateEntry(add_bsm_frame, width=1, background='#067790', foreground='white', borderwidth=1, font=('yu gothic ui',12,'bold'))
    date_entry.place(x=750, y=120, width=130)


    nom_label = Label(add_bsm_frame, text="Employé    :",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    nom_label.place(x=30, y=120)

    Num_carte_combobox = ttk.Combobox(add_bsm_frame, text="Numéro carte",width='15', state='readonly', values=values)
    Num_carte_combobox.place(x=135, y=125, width=120)

    nom_line =Canvas(add_bsm_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    nom_line.place(x=135, y=145)

    conn.close()

    def save_BSM():

        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        code_bsm = code_bsm_entry.get()
        date = date_entry.get()
        Num_carte = Num_carte_combobox.get()

        #Vérifier si tous les champs sont remplis
        if not code_bsm or not date or not Num_carte:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_bsm_frame)
            return
    

        c.execute("INSERT INTO BSM VALUES (?, ?, ?)",
                  (code_bsm, date, Num_carte))
        
        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=add_bsm_frame)

        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_bsm.delete(0, END)
        


        code_bsm_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_carte_combobox.set("")

        conn.commit()
        conn.close()
    
    save_button = Button(add_bsm_frame, text="Ajouter", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_BSM)
    save_button.place(x=610,y=500)

    def annuler():
        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_bsm.delete(0, END)
        code_bsm_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_carte_combobox.set("")
        e_code_sort.delete(0, tk.END)
        e_qte_sort.delete(0, tk.END)
        e_prix_sort.delete(0, tk.END)   
        e_code_combobox.set("")


    exit_button = Button(add_bsm_frame, text="Annuler",  width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=150,y=500)

    tableau = None


    def ajouter_ligne():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        # Récupération des valeurs saisies par l'utilisateur
        code_sort = e_code_sort.get()
        qte_sort = int(e_qte_sort.get())
        prix_sort = float(e_prix_sort.get())
        montant_sort = qte_sort * prix_sort
        code_bsm = e_code_bsm.get()
        code_article = e_code_combobox.get()

        # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM SORTIES WHERE code_sort=?", (code_sort,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le code de sortie existe déjà dans la base de données", parent=add_bsm_window)
            return

        #Vérifier si tous les champs sont remplis
        if not code_sort or not qte_sort or not prix_sort or not montant_sort or not code_bsm or not code_article:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_bsm_window)
            return
    
        # Vérification de la quantité disponible dans le stock
        c.execute("SELECT Quantité FROM Article WHERE code_article = ?", (code_article,))
        qte_dispo = c.fetchone()[0]
        if qte_sort > qte_dispo:
            messagebox.showerror(title="Erreur", message=f"La quantité disponible pour l'article {code_article} est insuffisante pour effectuer une sortie de {qte_sort} unité(s).", parent=add_bsm_frame)
            return
    
        # Insertion des données dans la base de données
        c.execute("INSERT INTO SORTIES VALUES (?, ?, ?, ?, ?, ?)",
                (code_sort, qte_sort, prix_sort, montant_sort, code_bsm, code_article))

        c.execute("""
        UPDATE Article
        SET Quantité = Quantité - ?,
            prix = ?,
            montant = (Quantité - ?) * ?
        WHERE code_article = ?
        """, (qte_sort, prix_sort, qte_sort, prix_sort, code_article,))

        conn.commit()
        conn.close()
    
        # Ajout des données dans le tableau
        tableau.insert("", tk.END, values=(code_sort, qte_sort, prix_sort, montant_sort, code_bsm, code_article))
    
        # Effacement des champs de saisie
        e_code_sort.delete(0, tk.END)
        e_qte_sort.delete(0, tk.END)
        e_prix_sort.delete(0, tk.END)   
        e_code_combobox.set("")

    # Création du tableau
    tableau = tk.ttk.Treeview(add_bsm_frame, columns=("code_sort", "qte_sort", "prix_sort", "montant_sort", "code_bsm", "code_article"))

    # Configuration des colonnes
    tableau.column("#0", width=0, stretch=tk.NO)
    tableau.column("code_sort", width=100)
    tableau.column("qte_sort", width=100)
    tableau.column("prix_sort", width=100)
    tableau.column("montant_sort", width=100)
    tableau.column("code_bsm", width=100)
    tableau.column("code_article", width=100)

    # Titres des colonnes
    tableau.heading("code_sort", text="Code Sortie")
    tableau.heading("qte_sort", text="Quantité Sortie")
    tableau.heading("prix_sort", text="Prix Sortie")
    tableau.heading("montant_sort", text="Montant Sortie")
    tableau.heading("code_bsm", text="Code BSM")
    tableau.heading("code_article", text="Code Article")

    # Ajout d'une ligne vide pour la saisie
    tableau.insert("", tk.END, values=("", "", "", "", "", ""))

    # Placement du tableau dans la fenêtre
    tableau.place(x=150, y=250)
    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT code_article FROM ARTICLE WHERE Code_catg='FB'")
    values2 = [row[0] for row in c.fetchall()]

    # Création des champs de saisie
    e_code_sort = tk.Entry(add_bsm_frame)
    e_qte_sort = tk.Entry(add_bsm_frame)
    e_prix_sort = tk.Entry(add_bsm_frame)
    e_code_bsm = tk.Entry(add_bsm_frame)
    e_code_combobox = ttk.Combobox(add_bsm_frame, text="Code Article",width='15', state='readonly', values=values2)


    


    # Placement des champs de saisie dans la fenêtre
    e_code_sort.place(x=150, y=220)
    e_qte_sort.place(x=250, y=220)
    e_prix_sort.place(x=350, y=220)
    e_code_bsm.place(x=450, y=220)
    e_code_combobox.place(x=550, y=219)

    # Création des étiquettes pour les champs de saisie
    tk.Label(add_bsm_frame, text="Code Sortie",bg="#067790").place(x=150, y=195)
    tk.Label(add_bsm_frame, text="Quantité Sortie",bg="#067790").place(x=250, y=195)
    tk.Label(add_bsm_frame, text="Prix Sorties",bg="#067790").place(x=350, y=195)
    tk.Label(add_bsm_frame, text="Code BSM",bg="#067790").place(x=450, y=195)
    tk.Label(add_bsm_frame, text="Code Article",bg="#067790").place(x=550, y=195)

    # Bouton pour ajouter une ligne
    btn_ajouter = tk.Button(add_bsm_frame, text="Ajouter Sortie",width='10', bg='#ACE5F3',cursor='hand2', command=ajouter_ligne)
    btn_ajouter.place(x=670, y=218)

    def update_fields(event):
        value = code_bsm_entry.get()
        e_code_bsm.delete(0, END)
        e_code_bsm.insert(0, value)

    code_bsm_entry.bind("<KeyRelease>", update_fields)      
    def annuler():
        add_bsm_window.destroy()

    exit_button = Button(add_bsm_window, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)

#===========================================Ajouter BSM PF =================================================

def AjouterBSM_PF():

    add_bsm_pf_window = tk.Toplevel()
    add_bsm_pf_window.title("Ajouter BSM")
    add_bsm_pf_window.state('zoomed') 
    # add_bsm_pf_window.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    add_bsm_pf_window.resizable(0,0)
    add_bsm_pf_window.config(bg="#ACE5F3")
    add_bsm_pf_frame = Frame(add_bsm_pf_window,bg='#067790', width='900', height='600')
    add_bsm_pf_frame.place(x=200, y=30)

    add_bsm_pf_window.geometry("1300x700")



    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT Num_représantant FROM Représantant")
    values = [row[0] for row in c.fetchall()]

    label = Label(add_bsm_pf_frame, text="BON DE SORTIE ",bg='#067790',font=('yu gothic ui', 20,'bold'),fg='white')
    label.place(x=15, y=10)
    
    code_bsm_label = Label(add_bsm_pf_frame, text="Code BSM:",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    code_bsm_label.place(x=380, y=70)

    code_bsm_entry = Entry(add_bsm_pf_frame, highlightthickness=0, relief=FLAT, bg='#067790', fg='black',font=('yu gothic ui',12,'bold'))
    code_bsm_entry.place(x=465, y=70, width=90)

    code_bsm_line =Canvas(add_bsm_pf_frame, width=90, height=2.0,bg='white',highlightthickness=0)
    code_bsm_line.place(x=465, y=93)

    date_label = Label(add_bsm_pf_frame, text="Date : ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    date_label.place(x=700, y=120)

    date_entry = DateEntry(add_bsm_pf_frame, width=1, background='#067790', foreground='white', borderwidth=1, font=('yu gothic ui',12,'bold'))
    date_entry.place(x=750, y=120, width=130)


    nom_label = Label(add_bsm_pf_frame, text="Représentant:",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    nom_label.place(x=30, y=120)

    Num_représantant_combobox = ttk.Combobox(add_bsm_pf_frame, text="Numméro représentant",width='15', state='readonly', values=values)
    Num_représantant_combobox.place(x=145, y=125, width=120)

    nom_line =Canvas(add_bsm_pf_frame, width=120, height=2.0,bg='white',highlightthickness=0)
    nom_line.place(x=145, y=145)

    conn.close()

    def save_BSM_PF():

        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        code_bsm = code_bsm_entry.get()
        date = date_entry.get()
        Num_représantant = Num_représantant_combobox.get()


        


        #Vérifier si tous les champs sont remplis
        if not code_bsm or not date or not Num_représantant:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_bsm_pf_frame)
            return
    

        c.execute("INSERT INTO BSM VALUES (?, ?, ?)",
                  (code_bsm, date, Num_représantant))
        

        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=add_bsm_pf_frame)

        # Vider le tableau
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_bsm.delete(0, END)

        code_bsm_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_représantant_combobox.set("")

        conn.commit()
        conn.close()
    
    save_button = Button(add_bsm_pf_frame, text="Ajouter", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_BSM_PF)
    save_button.place(x=610,y=500)

    def annuler():
        tableau.delete(*tableau.get_children())
        # Ajouter une ligne vide pour la saisie
        tableau.insert("", tk.END, values=("", "", "", "", "", ""))
        e_code_bsm.delete(0, END)

        code_bsm_entry.delete(0, END)
        date_entry.delete(0, END)
        Num_représantant_combobox.set("")


        e_code_sort.delete(0, tk.END)
        e_qte_sort.delete(0, tk.END)
        e_prix_sort.delete(0, tk.END)   
        e_code_combobox.set("")


    exit_button = Button(add_bsm_pf_frame, text="Annuler",  width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=150,y=500)

    tableau = None


    def ajouter_ligne():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        # Récupération des valeurs saisies par l'utilisateur
        code_sort = e_code_sort.get()
        qte_sort = int(e_qte_sort.get())
        prix_sort = float(e_prix_sort.get())
        montant_sort = qte_sort * prix_sort
        code_bsm = e_code_bsm.get()
        code_article = e_code_combobox.get()

        # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM SORTIES WHERE code_sort=?", (code_sort,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le code de sortie existe déjà dans la base de données", parent=add_bsm_pf_frame)
            return


        #Vérifier si tous les champs sont remplis
        if not code_sort or not qte_sort or not prix_sort or not montant_sort or not code_bsm or not code_article:
            messagebox.showerror(title="Erreur", message="Tous les champs doivent être remplis", parent=add_bsm_pf_frame)
            return
    
        # Vérification de la quantité disponible dans le stock
        c.execute("SELECT Quantité FROM Article WHERE code_article = ?", (code_article,))
        qte_dispo = c.fetchone()[0]
        if qte_sort > qte_dispo:
            messagebox.showerror(title="Erreur", message=f"La quantité disponible pour l'article {code_article} est insuffisante pour effectuer une sortie de {qte_sort} unité(s).", parent=add_bsm_pf_frame)
            return
    
        # Insertion des données dans la base de données
        c.execute("INSERT INTO SORTIES VALUES (?, ?, ?, ?, ?, ?)",
                (code_sort, qte_sort, prix_sort, montant_sort, code_bsm, code_article))

        c.execute("""
        UPDATE Article
        SET Quantité = Quantité - ?,
            prix = ?,
            montant = (Quantité - ?) * ?
        WHERE code_article = ?
        """, (qte_sort, prix_sort, qte_sort, prix_sort, code_article,))

        conn.commit()
        conn.close()
    
        # Ajout des données dans le tableau
        tableau.insert("", tk.END, values=(code_sort, qte_sort, prix_sort, montant_sort, code_bsm, code_article))
    
        # Effacement des champs de saisie
        e_code_sort.delete(0, tk.END)
        e_qte_sort.delete(0, tk.END)
        e_prix_sort.delete(0, tk.END)   
        e_code_combobox.set("")

    # Création du tableau
    tableau = tk.ttk.Treeview(add_bsm_pf_frame, columns=("code_sort", "qte_sort", "prix_sort", "montant_sort", "code_bsm", "code_article"))

    # Configuration des colonnes
    tableau.column("#0", width=0, stretch=tk.NO)
    tableau.column("code_sort", width=100)
    tableau.column("qte_sort", width=100)
    tableau.column("prix_sort", width=100)
    tableau.column("montant_sort", width=100)
    tableau.column("code_bsm", width=100)
    tableau.column("code_article", width=100)

    # Titres des colonnes
    tableau.heading("code_sort", text="Code Sortie")
    tableau.heading("qte_sort", text="Quantité Sortie")
    tableau.heading("prix_sort", text="Prix Sortie")
    tableau.heading("montant_sort", text="Montant Sortie")
    tableau.heading("code_bsm", text="Code BSM")
    tableau.heading("code_article", text="Code Article")

    # Ajout d'une ligne vide pour la saisie
    tableau.insert("", tk.END, values=("", "", "", "", "", ""))

    # Placement du tableau dans la fenêtre
    tableau.place(x=150, y=250)
    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT code_article FROM ARTICLE WHERE code_catg ='PF' ")
    values2 = [row[0] for row in c.fetchall()]

    # Création des champs de saisie
    e_code_sort = tk.Entry(add_bsm_pf_frame)
    e_qte_sort = tk.Entry(add_bsm_pf_frame)
    e_prix_sort = tk.Entry(add_bsm_pf_frame)
    e_code_bsm = tk.Entry(add_bsm_pf_frame)
    e_code_combobox = ttk.Combobox(add_bsm_pf_frame, text="Code Article",width='15', state='readonly', values=values2)


    


    # Placement des champs de saisie dans la fenêtre
    e_code_sort.place(x=150, y=220)
    e_qte_sort.place(x=250, y=220)
    e_prix_sort.place(x=350, y=220)
    e_code_bsm.place(x=450, y=220)
    e_code_combobox.place(x=550, y=219)

    # Création des étiquettes pour les champs de saisie
    tk.Label(add_bsm_pf_frame, text="Code Sortie",bg="#067790").place(x=150, y=195)
    tk.Label(add_bsm_pf_frame, text="Quantité Sortie",bg="#067790").place(x=250, y=195)
    tk.Label(add_bsm_pf_frame, text="Prix Sorties",bg="#067790").place(x=350, y=195)
    tk.Label(add_bsm_pf_frame, text="Code BSM",bg="#067790").place(x=450, y=195)
    tk.Label(add_bsm_pf_frame, text="Code Article",bg="#067790").place(x=550, y=195)

    # Bouton pour ajouter une ligne
    btn_ajouter = tk.Button(add_bsm_pf_frame, text="Ajouter Sortie",width='10', bg='#ACE5F3',cursor='hand2', command=ajouter_ligne)
    btn_ajouter.place(x=670, y=218)

    def update_fields(event):
        value = code_bsm_entry.get()
        e_code_bsm.delete(0, END)
        e_code_bsm.insert(0, value)

    code_bsm_entry.bind("<KeyRelease>", update_fields)
    def annuler():
        add_bsm_pf_window.destroy()

    exit_button = Button(add_bsm_pf_window, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)

#===========================================Liste BR======================================================================================
def liste_br() :

    conn = sqlite3.connect('stock1.db')
    cur = conn.cursor()

    art = Toplevel()
    art.title("Liste BR")
    art.state('zoomed')
    # art.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    art.resizable(0,0) 
    art.config(bg="#ACE5F3")
    art_frame = Frame(art, bg='#ACE5F3', width='900', height='600')
    art_frame.place(x=480, y=100)

    label = Label(art, text="Liste BR", font=('yu gothic ui', 23,'bold'),fg="white",bg="#ACE5F3")
    label.place(x=550, y=20)

    # Créer le tableau
    table = ttk.Treeview(art_frame, columns=("date", "fournisseur"))
    # Définir les en-têtes de colonnes
    table.heading("#0", text="Code BR")
    table.heading("date", text="Date")
    table.heading("fournisseur", text="Fournisseur")
    
    
    table.pack(fill="both", expand=True)

    table.column("#0", width=100, stretch=NO)
    table.column("date", width=100, stretch=NO)
    table.column("fournisseur", width=100, stretch=NO)
    
   
    cur.execute("""SELECT * FROM BR""")
    articles = cur.fetchall()

    for article in articles:
        code_br = article[0]
        date = article[1]
        num_fournisseur = article[2]
        
        table.insert("", "end", text=code_br, values=(date, num_fournisseur))

    def annuler():
        art.destroy()

    exit_button = Button(art, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)

    
#===========================================Liste BSM=======================================================================================  
def liste_bsm() :

    conn = sqlite3.connect('stock1.db')
    cur = conn.cursor()

    art = Toplevel()
    art.title("Liste BSM")
    art.state('zoomed')  
    # art.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')  
    art.resizable(0,0) 
    art.config(bg="#ACE5F3")
    art_frame = Frame(art, bg='#ACE5F3', width='900', height='600')
    art_frame.place(x=480, y=100)

    label = Label(art, text="Liste BSM", font=('yu gothic ui', 23,'bold'),fg="white",bg="#ACE5F3")
    label.place(x=550, y=20)

    # Créer le tableau
    table = ttk.Treeview(art_frame, columns=("date", "employé"))
    # Définir les en-têtes de colonnes
    table.heading("#0", text="Code BSM")
    table.heading("date", text="Date")
    table.heading("employé", text="Employé")
    
    
    table.pack(fill="both", expand=True)

    table.column("#0", width=100, stretch=NO)
    table.column("date", width=100, stretch=NO)
    table.column("employé", width=100, stretch=NO)
    
    
   
    cur.execute("""SELECT * FROM BSM""")
    articles = cur.fetchall()

    for article in articles:
        code_bsm = article[0]
        date = article[1]
        employé = article[2]
        
        table.insert("", "end", text=code_bsm, values=(date, employé))

    def annuler():
        art.destroy()

    exit_button = Button(art, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)

#=============================

# SELECT b.Code_bsm, b.Date_bsm, b.ID
# FROM BSM b
# JOIN Sorties s ON b.Code_bsm = s.Code_bsm
# JOIN Article a ON a.Code_article = s.Code_article
# WHERE Code_catg = 'PF'


#================================ajouter fournisseur================================================================================

def Ajouter_fournisseur():
    ajou_four = Toplevel() 
    ajou_four.geometry('1000x1000')
    ajou_four.title("Ajouter Fournisseur")
    ajou_four.state('zoomed') 
    # ajou_four.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    ajou_four.resizable(0,0) 
    ajou_four.config(bg="#ACE5F3")
    ajou_four_frame = Frame(ajou_four,bg='#067790', width='500', height='600')
    ajou_four_frame.place(x=380, y=30)


    label = Label(ajou_four_frame, text="Ajouter un nouveau fournisseur ",bg='#067790',font=('yu gothic ui', 25,'bold'),fg='white')
    label.place(x=10, y=30)

    Num_fournisseur_label = Label(ajou_four_frame, text="Code fournisseur * ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Num_fournisseur_label.place(x=70, y=115)

    Num_fournisseur_entry = Entry(ajou_four_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Num_fournisseur_entry.place(x=280, y=115, width=160)

    Num_fournisseur_line =Canvas(ajou_four_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Num_fournisseur_line.place(x=280, y=140)

    Nom_label = Label(ajou_four_frame, text="Nom * ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Nom_label.place(x=70, y=180)

    Nom_entry = Entry(ajou_four_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Nom_entry.place(x=280, y=180, width=160)

    Nom_line =Canvas(ajou_four_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Nom_line.place(x=280, y=205)


    Prénom_label = Label(ajou_four_frame, text="Prénom * ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Prénom_label.place(x=70, y=245)

    Prénom_entry = Entry(ajou_four_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Prénom_entry.place(x=280, y=245, width=160)

    Prénom_line =Canvas(ajou_four_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Prénom_line.place(x=280, y=270)

    Num_tel_label = Label(ajou_four_frame, text="Numéro de téléphone *",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Num_tel_label.place(x=70, y=310)

    Num_tel_entry = Entry(ajou_four_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Num_tel_entry.place(x=280, y=310, width=160)

    Num_tel_line =Canvas(ajou_four_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Num_tel_line.place(x=280, y=335)


    Email_label = Label(ajou_four_frame, text="Adresse e-mail *",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Email_label.place(x=70, y=375)

    Email_entry = Entry(ajou_four_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Email_entry.place(x=280, y=375, width=160)

    Email_line =Canvas(ajou_four_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Email_line.place(x=280, y=400)


    def validate_email(Email):
        """Valide le format de l'adresse e-mail."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # expression régulière pour valider le format de l'adresse e-mail
        return re.match(pattern, Email) is not None
    
    

    def validate_num_tel(num_tel):
        """
        Vérifie si le numéro de telephone est valide.
        """
        if len(num_tel) != 10:
            return False
        if not num_tel.isdigit():
            return False
        return True


    def save_fournisseur():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        Num_fournisseur = Num_fournisseur_entry.get()
        Nom = Nom_entry.get()
        Prénom = Prénom_entry.get()
        Num_tel = Num_tel_entry.get()
        Email = Email_entry.get()


         # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM Fournisseurs WHERE Num_fournisseur=?", (Num_fournisseur,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le numémero de fournisseur existe déjà dans la base de données", parent=ajou_four_frame)
            return


        # Vérifier si les champs obligatoires sont remplis
        if not Num_fournisseur or not Nom or not Prénom or not Num_tel or not Email:
            messagebox.showerror(title="Erreur", message="Veuillez remplir tous les champs obligatoires (*)", parent=ajou_four_frame)
            return


        # Vérifier si le numéro de fournisseur est correct
        if not validate_num_tel(Num_tel):
            messagebox.showerror(title="Erreur", message="Le numéro de téléphone est incorrect", parent=ajou_four_frame)
            return

        

        # Vérifier si l'adresse e-mail est valide
        if not validate_email(Email):
            messagebox.showerror(title="Erreur", message="Adresse e-mail invalide", parent=ajou_four_frame)
            return

        c.execute("INSERT INTO Fournisseurs VALUES (?, ?, ?, ?, ?)",
             (Num_fournisseur, Nom, Prénom, Num_tel, Email))

        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=ajou_four)       
    

        Num_fournisseur_entry.delete(0, END)
        Nom_entry.delete(0, END)
        Prénom_entry.delete(0, END)
        Num_tel_entry.delete(0, END)
        Email_entry.delete(0, END)
        
        
        conn.commit()
        conn.close()

    save_button = Button(ajou_four, text="Ajouter",width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_fournisseur)
    save_button.place(x=680,y=500)
        

    def annuler():
        Num_fournisseur_entry.delete(0, END)
        Nom_entry.delete(0, END)
        Prénom_entry.delete(0, END)
        Num_tel_entry.delete(0, END)
        Email_entry.delete(0, END)
    exit_button = Button(ajou_four, text="Annuler", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=440,y=500)


    def annuler():
        ajou_four.destroy()

    exit_button = Button(ajou_four, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)



#======================================liste fournisseur====================================================
def Liste_fournisseur():
    conn = sqlite3.connect('stock1.db')
    cur = conn.cursor()

    four = Toplevel()
    four.title("Liste des fournisseur ")
    four.state('zoomed') 
    # four.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    four.resizable(0,0) 
    four.config(background='#ACE5F3')
    four_frame = Frame(four,bg='#067790', width='1900', height='600')
    four_frame.place(x=350, y=70)

    article_label = Label(four, text="Liste des fournisseur", font=('yu gothic ui', 23,'bold'),fg="white",bg="#ACE5F3")
    article_label.place(x=500, y=20)

    # Créer le tableau
    table = ttk.Treeview(four_frame, columns=("nom","prenom","num_tel","email"))
    # Définir les en-têtes de colonnes
    table.heading("#0", text="Numéro fournisseur")
    table.heading("nom", text="Nom")
    table.heading("prenom", text="Prénom")
    table.heading("num_tel", text="Numéro de tel")
    table.heading("email", text="Adresse email")
    
    table.pack(fill="both", expand=True)

    table.column("#0", width=100, stretch=NO)
    table.column("nom", width=100, stretch=NO)
    table.column("prenom", width=100, stretch=NO)
    table.column("num_tel", width=100, stretch=NO)
    table.column("email", width=150, stretch=NO)
   
    cur.execute("""SELECT * FROM Fournisseurs""")
    fournisseurs = cur.fetchall()

    for fournisseur in fournisseurs:
        num_fournisseur = fournisseur[0]
        nom = fournisseur[1]
        prenom = fournisseur[2]
        num_tel = fournisseur[3]
        email = fournisseur[4]
        table.insert("", "end", text=num_fournisseur , values=(nom, prenom, num_tel, email))

    def annuler():
        four.destroy()

    exit_button = Button(four, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)

#======================================Ajouter employé======================================================

def Ajouter_empl():
    ajou_empl = Toplevel()
    ajou_empl.geometry('1000x1000')
    ajou_empl.title("Ajouter employé")
    ajou_empl.state('zoomed')
    # ajou_empl.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    ajou_empl.resizable(0,0) 
    ajou_empl.config(bg="#ACE5F3")
    ajou_empl_frame = Frame(ajou_empl,bg='#067790', width='500', height='600')
    ajou_empl_frame.place(x=380, y=30)

    label = Label(ajou_empl_frame, text="Ajouter un employé ",bg='#067790',font=('yu gothic ui', 20,'bold'),fg='white')
    label.place(x=100, y=0)

    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT Nom_département FROM Département")
    values = [row[0] for row in c.fetchall()]

    Num_carte_label = Label(ajou_empl_frame, text="Numéro de carte* ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Num_carte_label.place(x=80, y=50)

    Num_carte_entry = Entry(ajou_empl_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Num_carte_entry.place(x=280, y=50, width=160)

    Num_carte_line =Canvas(ajou_empl_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Num_carte_line.place(x=280, y=75)

    Nom_label = Label(ajou_empl_frame, text="Nom* ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Nom_label.place(x=80, y=115)

    Nom_entry = Entry(ajou_empl_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Nom_entry.place(x=280, y=115, width=160)

    Nom_line =Canvas(ajou_empl_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Nom_line.place(x=280, y=140)

    Prénom_label = Label(ajou_empl_frame, text="Prénom* ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Prénom_label.place(x=80, y=180)

    Prénom_entry = Entry(ajou_empl_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Prénom_entry.place(x=280, y=180, width=160)

    Prénom_line =Canvas(ajou_empl_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Prénom_line.place(x=280, y=205)

    Num_tel_label = Label(ajou_empl_frame, text="Numéro de téléphone*",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Num_tel_label.place(x=80, y=245)

    Num_tel_entry = Entry(ajou_empl_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Num_tel_entry.place(x=280, y=245, width=160)

    Num_tel_line =Canvas(ajou_empl_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Num_tel_line.place(x=280, y=270)


    Email_label = Label(ajou_empl_frame, text="Adresse e-mail*",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Email_label.place(x=80, y=310)

    Email_entry = Entry(ajou_empl_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Email_entry.place(x=280, y=310, width=160)

    Email_line =Canvas(ajou_empl_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Email_line.place(x=280, y=335)



    Grade_label = Label(ajou_empl_frame, text="Grade*",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Grade_label.place(x=80, y=375)

    Grade_combobox = ttk.Combobox(ajou_empl_frame, text="Grade",width='15', state='readonly', values=["Chef département", "Chef service"])
    Grade_combobox.place(x=280, y=382, width=160)

    Grade_line =Canvas(ajou_empl_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Grade_line.place(x=280, y=400)



    Département_label = Label(ajou_empl_frame, text="Département*",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Département_label.place(x=80, y=440)

    Département_combobox = ttk.Combobox(ajou_empl_frame, text="Département",width='15', state='readonly', values=values)
    Département_combobox.place(x=280, y=445, width=160)

    Département_line =Canvas(ajou_empl_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Département_line.place(x=280, y=465)

    conn.close()

    def validate_email(Email):
        """Valide le format de l'adresse e-mail."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # expression régulière pour valider le format de l'adresse e-mail
        return re.match(pattern, Email) is not None
    
    

    def validate_num_tel(num_tel):
        """
        Vérifie si le numéro de telephone est valide.
        """
        if len(num_tel) != 10:
            return False
        if not num_tel.isdigit():
            return False
        return True


    def save_employé():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()
        d = conn.cursor()

        Num_carte = Num_carte_entry.get()
        Nom = Nom_entry.get()
        Prénom = Prénom_entry.get()
        Num_tel = Num_tel_entry.get()
        Email = Email_entry.get()
        Grade = Grade_combobox.get()
        Département = Département_combobox.get()


        # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM employé WHERE Num_carte=?", (Num_carte,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le numémero de carte existe déjà dans la base de données", parent=ajou_empl_frame)
            return

        # Vérifier si les champs obligatoires sont remplis
        if not Num_carte or not Nom or not Prénom or not Num_tel or not Email or not Grade or not Département:
            messagebox.showerror(title="Erreur", message="Veuillez remplir tous les champs obligatoires (*)", parent=ajou_empl_frame)
            return

        # Vérifier si le numéro de fournisseur est correct
        if not validate_num_tel(Num_tel):
            messagebox.showerror(title="Erreur", message="Le numéro de téléphone est incorrect", parent=ajou_empl_frame)
            return

        # Vérifier si l'adresse e-mail est valide
        if not validate_email(Email):
            messagebox.showerror(title="Erreur", message="Adresse e-mail invalide", parent=ajou_empl_frame)
            return


        c.execute("INSERT INTO Personne VALUES (?, ?, ?, ?, ?)",
             (Num_carte, Nom, Prénom, Num_tel, Email))
        d.execute("INSERT INTO Employé VALUES (?, ?, ?)",
             (Num_carte, Grade, Département))      

        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=ajou_empl_frame)       
    

        Num_carte_entry.delete(0, END)
        Nom_entry.delete(0, END)
        Prénom_entry.delete(0, END)
        Num_tel_entry.delete(0, END)
        Email_entry.delete(0, END)
        Grade_combobox.set("")
        Département_combobox.set("")
        
        
        conn.commit()
        conn.close()

    save_button = Button(ajou_empl, text="Ajouter",width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_employé)
    save_button.place(x=680,y=550)
        

    def annuler():
        Num_carte_entry.delete(0, END)
        Nom_entry.delete(0, END)
        Prénom_entry.delete(0, END)
        Num_tel_entry.delete(0, END)
        Email_entry.delete(0, END)
        Grade_combobox.set("")
        Département_combobox.set("")
    exit_button = Button(ajou_empl, text="Annuler", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=450,y=550)

    def annuler():
        ajou_empl.destroy()
    exit_button = Button(ajou_empl, text="Retour", width='15',cursor='hand2', command=annuler)
    exit_button.place(x=10,y=630)

#====================================Liste Employé==========================================    
def Liste_employé():
    conn = sqlite3.connect('stock1.db')
    cur = conn.cursor()

    empl = Toplevel()
    empl.title("Liste des Employés ")
    empl.state('zoomed') 
    # empl.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    empl.resizable(0,0) 
    empl.config(background='#ACE5F3')
    empl_frame = Frame(empl,bg='#067790', width='900', height='600')
    empl_frame.place(x=250, y=70)

    article_label = Label(empl, text="Liste des employés", font=('yu gothic ui', 23,'bold'),fg="white",bg="#ACE5F3")
    article_label.place(x=500, y=20)

    # Créer le tableau
    table = ttk.Treeview(empl_frame, columns=("nom","prenom","num_tel","email","grade","departement"))
    # Définir les en-têtes de colonnes
    table.heading("#0", text="Numéro de carte")
    table.heading("nom", text="Nom")
    table.heading("prenom", text="Prénom")
    table.heading("num_tel", text="Numéro de tel")
    table.heading("email", text="Adresse email")
    table.heading("grade", text="Grade")
    table.heading("departement", text="Département")
    
    table.pack(fill="both", expand=True)

    table.column("#0", width=100, stretch=NO)
    table.column("nom", width=100, stretch=NO)
    table.column("prenom", width=100, stretch=NO)
    table.column("num_tel", width=100, stretch=NO)
    table.column("email", width=150, stretch=NO)
    table.column("grade", width=100, stretch=NO)
    table.column("departement", width=100, stretch=NO)
   
    cur.execute("""SELECT * FROM Personne p
                    JOIN Employé e ON p.ID = e.Num_carte""")
    employés = cur.fetchall()

    for employé in employés:
        num_carte = employé[0]
        nom = employé[1]
        prenom = employé[2]
        num_tel = employé[3]
        email = employé[4]
        ID = employé[5]
        grade = employé[6]
        departement = employé[7]

        table.insert("", "end", text=num_carte , values=(nom, prenom, num_tel, email, grade, departement))

    def annuler():
        empl.destroy()

    exit_button = Button(empl, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)

#===================================Ajouter représantant================================================

def Ajouter_représantant():

    ajou_repr = Toplevel()
    ajou_repr.geometry('1000x1000')
    ajou_repr.title("Ajouter Représentant")
    ajou_repr.state('zoomed') 
    # ajou_repr.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    ajou_repr.resizable(0,0) 
    ajou_repr.config(bg="#ACE5F3")
    ajou_repr_frame = Frame(ajou_repr,bg='#067790', width='500', height='600')
    ajou_repr_frame.place(x=380, y=30)

    label = Label(ajou_repr_frame, text="Ajouter un représentant ",bg='#067790',font=('yu gothic ui', 20,'bold'),fg='white')
    label.place(x=100, y=30)

    conn = sqlite3.connect('stock1.db')
    c = conn.cursor()
    c.execute("SELECT Nom_entreprise FROM Entreprise")
    values = [row[0] for row in c.fetchall()]

    Num_représantant_label = Label(ajou_repr_frame, text="Numéro Représentant* ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Num_représantant_label.place(x=80, y=100)

    Num_représantant_entry = Entry(ajou_repr_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Num_représantant_entry.place(x=280, y=100, width=150)

    Num_représantant_line =Canvas(ajou_repr_frame, width=150, height=2.0,bg='white',highlightthickness=0)
    Num_représantant_line.place(x=280, y=125)

    Nom_label = Label(ajou_repr_frame, text="Nom*",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Nom_label.place(x=80, y=165)

    Nom_entry = Entry(ajou_repr_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Nom_entry.place(x=280, y=165, width=150)

    Nom_line =Canvas(ajou_repr_frame, width=150, height=2.0,bg='white',highlightthickness=0)
    Nom_line.place(x=280, y=190)

    Prénom_label = Label(ajou_repr_frame, text="Prénom* ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Prénom_label.place(x=80, y=230)

    Prénom_entry = Entry(ajou_repr_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Prénom_entry.place(x=280, y=230, width=150)

    Prénom_line =Canvas(ajou_repr_frame, width=150, height=2.0,bg='white',highlightthickness=0)
    Prénom_line.place(x=280, y=255)

    Num_tel_label = Label(ajou_repr_frame, text="Numéro de téléphone*",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Num_tel_label.place(x=80, y=295)

    Num_tel_entry = Entry(ajou_repr_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Num_tel_entry.place(x=280, y=295, width=150)

    Num_tel_line =Canvas(ajou_repr_frame, width=150, height=2.0,bg='white',highlightthickness=0)
    Num_tel_line.place(x=280, y=320)


    Email_label = Label(ajou_repr_frame, text="Adress email*",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Email_label.place(x=80, y=360)

    Email_entry = Entry(ajou_repr_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Email_entry.place(x=280, y=360, width=150)

    Email_line =Canvas(ajou_repr_frame, width=150, height=2.0,bg='white',highlightthickness=0)
    Email_line.place(x=280, y=385)


    Entreprise_label = Label(ajou_repr_frame, text="Entreprise*",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Entreprise_label.place(x=80, y=425)

    Entreprise_combobox = ttk.Combobox(ajou_repr_frame, text="Département*",width='15', state='readonly', values=values)
    Entreprise_combobox.place(x=280, y=430, width=150)

    Entreprise_line =Canvas(ajou_repr_frame, width=150, height=2.0,bg='white',highlightthickness=0)
    Entreprise_line.place(x=280, y=450)

    conn.close()

    def validate_email(Email):
        """Valide le format de l'adresse e-mail."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # expression régulière pour valider le format de l'adresse e-mail
        return re.match(pattern, Email) is not None
    
    

    def validate_num_tel(num_tel):
        """
        Vérifie si le numéro de telephone est valide.
        """
        if len(num_tel) != 10:
            return False
        if not num_tel.isdigit():
            return False
        return True

    def save_représantant():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()
        d = conn.cursor()

        Num_représantant = Num_représantant_entry.get()
        Nom = Nom_entry.get()
        Prénom = Prénom_entry.get()
        Num_tel = Num_tel_entry.get()
        Email = Email_entry.get()
        Entreprise = Entreprise_combobox.get()

        # Vérifier si xxxxxx déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM représantant WHERE Num_représantant=?", (Num_représantant,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le numémero de représantant existe déjà dans la base de données", parent=ajou_repr_frame)
            return


        # Vérifier si les champs obligatoires sont remplis
        if not Num_représantant or not Nom or not Prénom or not Num_tel or not Email or not Entreprise:
            messagebox.showerror(title="Erreur", message="Veuillez remplir tous les champs obligatoires (*)", parent=ajou_repr_frame)
            return

        # Vérifier si le numéro de fournisseur est correct
        if not validate_num_tel(Num_tel):
            messagebox.showerror(title="Erreur", message="Le numéro de téléphone est incorrect", parent=ajou_repr_frame)
            return

        

        # Vérifier si l'adresse e-mail est valide
        if not validate_email(Email):
            messagebox.showerror(title="Erreur", message="Adresse e-mail invalide", parent=ajou_repr_frame)
            return


        c.execute("INSERT INTO Personne VALUES (?, ?, ?, ?, ?)",
             (Num_représantant, Nom, Prénom, Num_tel, Email))
        d.execute("INSERT INTO Représantant VALUES (?, ?)",
             (Num_représantant,  Entreprise))      

        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=ajou_repr_frame)       
    

        Num_représantant_entry.delete(0, END)
        Nom_entry.delete(0, END)
        Prénom_entry.delete(0, END)
        Num_tel_entry.delete(0, END)
        Email_entry.delete(0, END)
        Entreprise_combobox.set("")
        
        
        conn.commit()
        conn.close()

    save_button = Button(ajou_repr, text="Ajouter",width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_représantant)
    save_button.place(x=670,y=530)
        

    def annuler():
        Num_représantant_entry.delete(0, END)
        Nom_entry.delete(0, END)
        Prénom_entry.delete(0, END)
        Num_tel_entry.delete(0, END)
        Email_entry.delete(0, END)
        Entreprise_combobox.set("")
    exit_button = Button(ajou_repr, text="Annuler", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=470,y=530)

    def annuler():
        ajou_repr.destroy()

    exit_button = Button(ajou_repr, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)
#===================================Liste représentant====================================================

def Liste_représantant():
    conn = sqlite3.connect('stock1.db')
    cur = conn.cursor()

    repr = Toplevel()
    repr.title("Liste des Représentants ")
    repr.state('zoomed')    
    repr.resizable(0,0) 
    repr.config(background='#ACE5F3')
    repr_frame = Frame(repr,bg='#067790', width='900', height='600')
    repr_frame.place(x=300, y=70)

    article_label = Label(repr, text="Liste des représentant", font=('yu gothic ui', 23,'bold'),fg="white",bg="#ACE5F3")
    article_label.place(x=500, y=20)

    # Créer le tableau
    table = ttk.Treeview(repr_frame, columns=("nom","prenom","num_tel","email","entreprise"))
    # Définir les en-têtes de colonnes
    table.heading("#0", text="Numéro représentant")
    table.heading("nom", text="Nom")
    table.heading("prenom", text="Prénom")
    table.heading("num_tel", text="Numéro de tel")
    table.heading("email", text="Adresse email")
    table.heading("entreprise", text="Entreprise")
    
    table.pack(fill="both", expand=True)

    table.column("#0", width=100, stretch=NO)
    table.column("nom", width=100, stretch=NO)
    table.column("prenom", width=100, stretch=NO)
    table.column("num_tel", width=100, stretch=NO)
    table.column("email", width=150, stretch=NO)
    table.column("entreprise", width=100, stretch=NO)
   
    cur.execute("""SELECT * FROM Personne p
                    JOIN Représantant r ON p.ID = r.Num_représantant""")
    représantants = cur.fetchall()

    for représantant in représantants:
        num_représantant = représantant[0]
        nom = représantant[1]
        prenom = représantant[2]
        num_tel = représantant[3]
        email = représantant[4]
        ID = représantant[5]
        entreprise = représantant[6]

        table.insert("", "end", text=num_représantant , values=(nom, prenom, num_tel, email, entreprise))

    def annuler():
        repr.destroy()

    exit_button = Button(repr, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)



#==================================Ajouter entreprise======================================================

def Ajouter_entreprise():

    ajou_entr = Toplevel()
    ajou_entr.geometry('1000x1000')
    ajou_entr.title("Ajouter Entreprise")
    ajou_entr.state('zoomed')  
    # ajou_entr.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')  
    ajou_entr.resizable(0,0) 
    ajou_entr.config(bg="#ACE5F3")
    ajou_entr_frame = Frame(ajou_entr,bg='#067790', width='500', height='600')
    ajou_entr_frame.place(x=380, y=10)

    label = Label(ajou_entr_frame, text="Ajouter une entreprise ",bg='#067790',font=('yu gothic ui', 25,'bold'),fg='white')
    label.place(x=90, y=30)

    Num_entr_label = Label(ajou_entr_frame, text="Numéro Entreprise* ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Num_entr_label.place(x=90, y=150)

    Num_entr_entry = Entry(ajou_entr_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Num_entr_entry.place(x=260, y=150, width=160)

    Num_entr_line =Canvas(ajou_entr_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Num_entr_line.place(x=260, y=175)

    Nom_label = Label(ajou_entr_frame, text="Nom Entreprise* ",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Nom_label.place(x=90, y=215)

    Nom_entry = Entry(ajou_entr_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Nom_entry.place(x=260, y=215, width=160)

    Nom_line =Canvas(ajou_entr_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Nom_line.place(x=260, y=240)


    Email_label = Label(ajou_entr_frame, text="Adresse e-mail*",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Email_label.place(x=90, y=280)

    Email_entry = Entry(ajou_entr_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Email_entry.place(x=260, y=280, width=160)

    Email_line =Canvas(ajou_entr_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Email_line.place(x=260, y=305)

    
    Adresse_label = Label(ajou_entr_frame, text="Adresse*",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
    Adresse_label.place(x=90, y=345)

    Adresse_entry = Entry(ajou_entr_frame, highlightthickness=0, relief=FLAT, bg='#B0e0e6', fg='black',font=('yu gothic ui',12,'bold'))
    Adresse_entry.place(x=260, y=345, width=160)

    Adresse_line =Canvas(ajou_entr_frame, width=160, height=2.0,bg='white',highlightthickness=0)
    Adresse_line.place(x=260, y=370)

    def validate_email(Email):
        """Valide le format de l'adresse e-mail."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # expression régulière pour valider le format de l'adresse e-mail
        return re.match(pattern, Email) is not None
    

  


    def save_entreprise():
        conn = sqlite3.connect('stock1.db')
        c = conn.cursor()

        Num_entreprise = Num_entr_entry.get()
        Nom = Nom_entry.get()        
        Email = Email_entry.get()
        Adresse = Adresse_entry.get()

        # Vérifier si le code article existe déjà dans la base de données
        c.execute("SELECT COUNT(*) FROM Entreprise WHERE ID_entreprise=?", (Num_entreprise,))
        count = c.fetchone()[0]
        if count > 0:
            messagebox.showerror(title="Erreur", message="Le numémero d'entreprise existe déjà dans la base de données", parent=ajou_entr_frame)
            return

         # Vérifier si les champs obligatoires sont remplis
        if not Num_entreprise or not Nom or not Email or not Adresse:
            messagebox.showerror(title="Erreur", message="Veuillez remplir tous les champs obligatoires (*)", parent=ajou_entr_frame)
            return

        # Vérifier si l'adresse e-mail est valide
        if not validate_email(Email):
            messagebox.showerror(title="Erreur", message="Adresse e-mail invalide", parent=ajou_entr_frame)
            return


        c.execute("INSERT INTO Entreprise VALUES (?, ?, ?, ?)",
             (Num_entreprise, Nom, Email, Adresse))
             

        messagebox.showinfo(title="Succès", message="Les données ont été ajoutées avec succès", parent=ajou_entr_frame)       
    

        Num_entr_entry.delete(0, END)
        Nom_entry.delete(0, END)
        Email_entry.delete(0, END)
        Adresse_entry.delete(0, END)

        
        
        conn.commit()
        conn.close()

    save_button = Button(ajou_entr, text="Ajouter",width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=save_entreprise)
    save_button.place(x=660,y=450)
        
    def annuler():
        Num_entr_entry.delete(0, END)
        Nom_entry.delete(0, END)
        Email_entry.delete(0, END)
        Adresse_entry.delete(0, END)
    
    exit_button = Button(ajou_entr, text="Annuler", width='15',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 11,'bold'),fg='black', command=annuler)
    exit_button.place(x=450,y=450)


    def annuler():
        ajou_entr.destroy()

    exit_button = Button(ajou_entr, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)

#=====================================Liste entreprise==================================================

def Liste_entreprise():
    conn = sqlite3.connect('stock1.db')
    cur = conn.cursor()

    entr = Toplevel()
    entr.title("Liste des Entreprises ")
    entr.state('zoomed') 
    # entr.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    entr.resizable(0,0) 
    entr.config(background='#ACE5F3')
    entr_frame = Frame(entr,bg='#067790', width='900', height='600')
    entr_frame.place(x=380, y=70)

    entreprise_label = Label(entr, text="Liste des entreprises", font=('yu gothic ui', 23,'bold'),fg="white",bg="#ACE5F3")
    entreprise_label.place(x=500, y=20)

    # Créer le tableau
    table = ttk.Treeview(entr_frame, columns=("nom","email","adresse"))
    # Définir les en-têtes de colonnes
    table.heading("#0", text="ID entreprise")
    table.heading("nom", text="Nom")
    table.heading("email", text="Adresse email")
    table.heading("adresse", text="Adresse")
    
    table.pack(fill="both", expand=True)

    table.column("#0", width=100, stretch=NO)
    table.column("nom", width=100, stretch=NO)
    table.column("email", width=150, stretch=NO)
    table.column("adresse", width=100, stretch=NO)
   
    cur.execute("""SELECT * FROM Entreprise""")
    entreprises = cur.fetchall()

    for entreprise in entreprises:
        num_entreprise = entreprise[0]
        nom = entreprise[1]
        email = entreprise[2]
        adresse = entreprise[3]

        table.insert("", "end", text=num_entreprise , values=(nom, email, adresse))

    def annuler():
        entr.destroy()

    exit_button = Button(entr, text="Retour", width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)
#===================================Gestion d'article not admin====================================
def G_article():
    G_art = Toplevel()
    G_art.geometry('500x500')
    G_art.title("Article")
    G_art.state('zoomed')
    # G_art.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
    G_art.resizable(0,0) 
    G_art.config(background='#ACE5F3')
    G_art_frame = Frame(G_art,bg='#067790', width='500', height='600')
    G_art_frame.place(x=380, y=30)


    btn = Button(G_art_frame,text="Liste Article",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=articles_type)
    btn.place(x=120,y=120)
    btn1 = Button(G_art_frame,text="Détails Article",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=article_details)
    btn1.place(x=120,y=220)
    btn2 = Button(G_art_frame,text="Ajouter Article",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=ajouter)
    btn2.place(x=120,y=320)
    btn5 = Button(G_art_frame,text="Supprimer Article",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=supprimer)
    btn5.place(x=120,y=420)

    def annuler():
        G_art.destroy()


    exit_button = Button(G_art, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)



#====================================Gestion d'article======================================================

def G_article_notadmin():
    G_art = Toplevel()
    G_art.geometry('500x500')
    G_art.title("Exercice 2023")
    G_art.state('zoomed')
    # G_art.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
    G_art.resizable(0,0) 
    G_art.config(background='#ACE5F3')
    G_art_frame = Frame(G_art,bg='#067790', width='500', height='600')
    G_art_frame.place(x=380, y=30)


    btn = Button(G_art_frame,text="Liste article",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=articles_type)
    btn.place(x=120,y=200)
    btn1 = Button(G_art_frame,text="Detaile Article",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=article_details)
    btn1.place(x=120,y=380)

    def annuler():
        G_art.destroy()


    exit_button = Button(G_art, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)
#=========================================consulter br pf==========================================
def consulter_ajouter_br_pf():
    
    ajouter_br = Toplevel()
    ajouter_br.geometry('500x500')
    ajouter_br.title("BR PF")
    ajouter_br.state('zoomed')
    # ajouter_br.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
    ajouter_br.resizable(0,0) 
    ajouter_br.config(background='#ACE5F3')
    ajouter_br_frame = Frame(ajouter_br, bg='#067790', width='500', height='600')
    ajouter_br_frame.place(x=380, y=30)
    
    btn1 = Button(ajouter_br_frame,text="Ajouter BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=AjouterBR_PF)
    btn1.place(x=120,y=200)
    btn2 = Button(ajouter_br_frame,text="Liste BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=liste_br)
    btn2.place(x=120,y=330)
 

    def annuler():
        ajouter_br.destroy()


    exit_button = Button(ajouter_br, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)    

#===========================================consulter br fb====================================================
def consulter_ajouter_br_fb():
    
    ajouter_br = Toplevel()
    ajouter_br.geometry('500x500')
    ajouter_br.title("BR FB")
    ajouter_br.state('zoomed') 
    # ajouter_br.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    ajouter_br.resizable(0,0) 
    ajouter_br.config(background='#ACE5F3')
    ajouter_br_frame = Frame(ajouter_br, bg='#067790', width='500', height='600')
    ajouter_br_frame.place(x=380, y=30)
    
    btn1 = Button(ajouter_br_frame,text="Ajouter BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=AjouterBR_FB)
    btn1.place(x=120,y=200)
    btn2 = Button(ajouter_br_frame,text="Liste BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=liste_br)
    btn2.place(x=120,y=330)
 

    def annuler():
        ajouter_br.destroy()


    exit_button = Button(ajouter_br, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)    


#===========================================consulter br bdr======================================================
def consulter_ajouter_br_pdr():
    
    ajouter_br = Toplevel()
    ajouter_br.geometry('500x500')
    ajouter_br.title("BR PDR")
    ajouter_br.state('zoomed')
    # ajouter_br.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
    ajouter_br.resizable(0,0) 
    ajouter_br.config(background='#ACE5F3')
    ajouter_br_frame = Frame(ajouter_br, bg='#067790', width='500', height='600')
    ajouter_br_frame.place(x=380, y=30)
    
    btn1 = Button(ajouter_br_frame,text="Ajouter BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=AjouterBR_PDR)
    btn1.place(x=120,y=200)
    btn2 = Button(ajouter_br_frame,text="Liste BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=liste_br)
    btn2.place(x=120,y=330)
 

    def annuler():
        ajouter_br.destroy()


    exit_button = Button(ajouter_br, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)    

#============================================couslter br mp====================================
def consulter_ajouter_br_mp():
    
    ajouter_br = Toplevel()
    ajouter_br.geometry('500x500')
    ajouter_br.title("BR MP")
    ajouter_br.state('zoomed')
    # ajouter_br.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
    ajouter_br.resizable(0,0) 
    ajouter_br.config(background='#ACE5F3')
    ajouter_br_frame = Frame(ajouter_br, bg='#067790', width='500', height='600')
    ajouter_br_frame.place(x=380, y=30)
    
    btn1 = Button(ajouter_br_frame,text="Ajouter BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=AjouterBR_MP)
    btn1.place(x=120,y=200)
    btn2 = Button(ajouter_br_frame,text="Liste BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=liste_br)
    btn2.place(x=120,y=330)
 

    def annuler():
        ajouter_br.destroy()


    exit_button = Button(ajouter_br, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)
#=============================================ADMINISTRATEUR=====================================================================================
def consulter_ajouter_br():
    
    ajouter_br = Toplevel()
    ajouter_br.geometry('500x500')
    ajouter_br.title("BR")
    ajouter_br.state('zoomed')
    # ajouter_br.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
    ajouter_br.resizable(0,0) 
    ajouter_br.config(background='#ACE5F3')
    ajouter_br_frame = Frame(ajouter_br, bg='#067790', width='500', height='600')
    ajouter_br_frame.place(x=380, y=30)
    
    btn1 = Button(ajouter_br_frame,text="Ajouter BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=AjouterBR)
    btn1.place(x=120,y=100)
    btn2 = Button(ajouter_br_frame,text="Liste BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=liste_br)
    btn2.place(x=120,y=200)
    btn3 = Button(ajouter_br_frame,text="Ajouter fournisseur",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=Ajouter_fournisseur)
    btn3.place(x=120,y=300)
    btn4 = Button(ajouter_br_frame,text="Liste fournisseurs",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=Liste_fournisseur)
    btn4.place(x=120,y=400)

    def annuler():
        ajouter_br.destroy()


    exit_button = Button(ajouter_br, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)
#=================================consulter bsm pf==========================================
def consulter_ajouter_bsm_pf():
    
    ajouter_bsm = Toplevel()
    ajouter_bsm.geometry('500x500')
    ajouter_bsm.title("BSM PF")
    ajouter_bsm.state('zoomed') 
    # ajouter_bsm.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    ajouter_bsm.resizable(0,0) 
    ajouter_bsm.config(background='#ACE5F3')
    ajouter_bsm_frame = Frame(ajouter_bsm, bg='#067790', width='500', height='600')
    ajouter_bsm_frame.place(x=380, y=30)
    

    btn2 = Button(ajouter_bsm_frame,text="Ajouter BSM",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=AjouterBSM_PF)
    btn2.place(x=120,y=150)
    btn3 = Button(ajouter_bsm_frame,text="Liste BSM",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=liste_bsm)
    btn3.place(x=120,y=250)
    btn5 = Button(ajouter_bsm_frame,text="Liste représantants",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=Liste_représantant)
    btn5.place(x=120,y=350)
    btn6 = Button(ajouter_bsm_frame,text="Liste entreprises",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=Liste_entreprise)
    btn6.place(x=120,y=450)


    def annuler():
        ajouter_bsm.destroy()


    exit_button = Button(ajouter_bsm, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)


#=================================consulter bsm fb========================================

def consulter_ajouter_bsm_fb():
    
    ajouter_bsm = Toplevel()
    ajouter_bsm.geometry('500x500')
    ajouter_bsm.title("BSM FB")
    ajouter_bsm.state('zoomed') 
    # ajouter_bsm.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    ajouter_bsm.resizable(0,0) 
    ajouter_bsm.config(background='#ACE5F3')
    ajouter_bsm_frame = Frame(ajouter_bsm, bg='#067790', width='500', height='600')
    ajouter_bsm_frame.place(x=380, y=30)
    
    btn1 = Button(ajouter_bsm_frame,text="Ajouter BSM",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=AjouterBSM_FB)
    btn1.place(x=120,y=150)
    btn3 = Button(ajouter_bsm_frame,text="Liste BSM",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=liste_bsm)
    btn3.place(x=120,y=250)
    btn4 = Button(ajouter_bsm_frame,text="Liste Employé",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=Liste_employé)
    btn4.place(x=120,y=350)
 
  
  
    

    def annuler():
        ajouter_bsm.destroy()


    exit_button = Button(ajouter_bsm, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)





#==================================consulter  bsm pdr================================================
def consulter_ajouter_bsm_pdr():
    
    ajouter_bsm = Toplevel()
    ajouter_bsm.geometry('500x500')
    ajouter_bsm.title("BSM PDR")
    ajouter_bsm.state('zoomed') 
    # ajouter_bsm.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    ajouter_bsm.resizable(0,0) 
    ajouter_bsm.config(background='#ACE5F3')
    ajouter_bsm_frame = Frame(ajouter_bsm, bg='#067790', width='500', height='600')
    ajouter_bsm_frame.place(x=380, y=30)
    
    btn1 = Button(ajouter_bsm_frame,text="Ajouter BSM",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=AjouterBSM_PDR)
    btn1.place(x=120,y=150)
    btn3 = Button(ajouter_bsm_frame,text="Liste BSM",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=liste_bsm)
    btn3.place(x=120,y=250)
    btn4 = Button(ajouter_bsm_frame,text="Liste Employé",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=Liste_employé)
    btn4.place(x=120,y=350)
 
  
  
    

    def annuler():
        ajouter_bsm.destroy()


    exit_button = Button(ajouter_bsm, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)


#================================consulter       bsm mp====================================================
def consulter_ajouter_bsm_mp():
    
    ajouter_bsm = Toplevel()
    ajouter_bsm.geometry('500x500')
    ajouter_bsm.title("BSM MP")
    ajouter_bsm.state('zoomed') 
    # ajouter_bsm.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    ajouter_bsm.resizable(0,0) 
    ajouter_bsm.config(background='#ACE5F3')
    ajouter_bsm_frame = Frame(ajouter_bsm, bg='#067790', width='500', height='600')
    ajouter_bsm_frame.place(x=380, y=30)
    
    btn1 = Button(ajouter_bsm_frame,text="Ajouter BSM",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=AjouterBSM_MP)
    btn1.place(x=120,y=150)
    btn3 = Button(ajouter_bsm_frame,text="Liste BSM",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=liste_bsm)
    btn3.place(x=120,y=250)
    btn4 = Button(ajouter_bsm_frame,text="Liste Employé",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=Liste_employé)
    btn4.place(x=120,y=350)
 
  
  
    

    def annuler():
        ajouter_bsm.destroy()


    exit_button = Button(ajouter_bsm, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)

#=======================================================================================================
def consulter_ajouter_bsm():
    
    ajouter_bsm = Toplevel()
    ajouter_bsm.geometry('500x500')
    ajouter_bsm.title("BSM")
    ajouter_bsm.state('zoomed')
    # ajouter_bsm.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
    ajouter_bsm.resizable(0,0) 
    ajouter_bsm.config(background='#ACE5F3')
    ajouter_bsm_frame = Frame(ajouter_bsm, bg='#067790', width='500', height='600')
    ajouter_bsm_frame.place(x=380, y=30)
    
    def employe():
        Employer = Toplevel()
        Employer.geometry('500x500')
        Employer.title("Employer")
        Employer.state('zoomed')
        # Employer.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
        Employer.resizable(0,0) 
        Employer.config(background='#ACE5F3')
        Employer_frame = Frame(Employer, bg='#067790', width='500', height='600')
        Employer_frame.place(x=380, y=30)

        btn7 = Button(Employer_frame,text="Ajouter Employé",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=Ajouter_empl)
        btn7.place(x=120,y=300)
        btn4 = Button(Employer_frame,text="Liste Employé",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=Liste_employé)
        btn4.place(x=120,y=150)

        def annuler():
            Employer.destroy()


        exit_button = Button(Employer, text="Retour",width='20',cursor='hand2', command=annuler)
        exit_button.place(x=10, y=630)


    def entreprise():
        Entr = Toplevel()
        Entr.geometry('500x500')
        Entr.title("Entreprise")
        Entr.state('zoomed')
        # Entr.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
        Entr.resizable(0,0) 
        Entr.config(background='#ACE5F3')
        Entr_frame = Frame(Entr, bg='#067790', width='500', height='600')
        Entr_frame.place(x=380, y=30)

        btn7 = Button(Entr_frame,text="Ajouter Entreprise",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=Ajouter_entreprise)
        btn7.place(x=120,y=300)
        btn4 = Button(Entr_frame,text="Liste Entreprises",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=Liste_entreprise)
        btn4.place(x=120,y=150)

        def annuler():
            Entr.destroy()


        exit_button = Button(Entr, text="Retour",width='20',cursor='hand2', command=annuler)
        exit_button.place(x=10, y=630)


    def representant():
        Rep = Toplevel()
        Rep.geometry('500x500')
        Rep.title("Representant")
        Rep.state('zoomed')
        # Rep.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
        Rep.resizable(0,0) 
        Rep.config(background='#ACE5F3')
        Rep_frame = Frame(Rep, bg='#067790', width='500', height='600')
        Rep_frame.place(x=380, y=30)

        btn7 = Button(Rep_frame,text="Ajouter Représentant",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=Ajouter_représantant)
        btn7.place(x=120,y=300)
        btn4 = Button(Rep_frame,text="Liste Représentants",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=Liste_représantant)
        btn4.place(x=120,y=150)

        def annuler():
            Rep.destroy()


        exit_button = Button(Rep, text="Retour",width='20',cursor='hand2', command=annuler)
        exit_button.place(x=10, y=630)




    btn1 = Button(ajouter_bsm_frame,text="Ajouter BSM",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=AjouterBSM)
    btn1.place(x=120,y=80)
    btn2 = Button(ajouter_bsm_frame,text="Ajouter BSM PF",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=AjouterBSM_PF)
    btn2.place(x=120,y=160)
    btn3 = Button(ajouter_bsm_frame,text="Liste BSM",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=liste_bsm)
    btn3.place(x=120,y=240)
    btn4 = Button(ajouter_bsm_frame,text="Employé",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=employe)
    btn4.place(x=120,y=320)
    btn5 = Button(ajouter_bsm_frame,text="Représantant",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=representant)
    btn5.place(x=120,y=480)
    btn6 = Button(ajouter_bsm_frame,text="Entreprise",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=entreprise)
    btn6.place(x=120,y=400)
    

    def annuler():
        ajouter_bsm.destroy()


    exit_button = Button(ajouter_bsm, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)

#========================================Exersice PF============================================
def exercice_PF():
    
    Exo = Toplevel()
    Exo.geometry('500x500')
    Exo.title("Exercice 2023")
    Exo.state('zoomed')  
    # Exo.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')   
    Exo.resizable(0,0) 
    Exo.config(background='#ACE5F3')
    Exo_frame = Frame(Exo,bg='#067790', width='500', height='600')
    Exo_frame.place(x=380, y=30)


    btn = Button(Exo_frame,text="Article",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=G_article_notadmin)
    btn.place(x=120,y=160)    
    btn3 = Button(Exo_frame,text="BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=consulter_ajouter_br_pf)
    btn3.place(x=120,y=280)
    btn4 = Button(Exo_frame,text="BSM", width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=consulter_ajouter_bsm_pf)
    btn4.place(x=120,y=400)
    
    def annuler():
        Exo.destroy()


    exit_button = Button(Exo, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)    

#========================================Exersice FB==============================================
def exercice_FB():
    
    Exo = Toplevel()
    Exo.geometry('500x500')
    Exo.title("Exercice 2023")
    Exo.state('zoomed') 
    # Exo.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    Exo.resizable(0,0) 
    Exo.config(background='#ACE5F3')
    Exo_frame = Frame(Exo,bg='#067790', width='500', height='600')
    Exo_frame.place(x=380, y=30)


    btn = Button(Exo_frame,text="Article",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=G_article_notadmin)
    btn.place(x=120,y=160)    
    btn3 = Button(Exo_frame,text="BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=consulter_ajouter_br_fb)
    btn3.place(x=120,y=280)
    btn4 = Button(Exo_frame,text="BSM", width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=consulter_ajouter_bsm_fb)
    btn4.place(x=120,y=400)
    
    def annuler():
        Exo.destroy()


    exit_button = Button(Exo, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)    

#==========================================Exersice PDR==============================================

def exercice_PDR():
    
    Exo = Toplevel()
    Exo.geometry('500x500')
    Exo.title("Exercice 2023")
    Exo.state('zoomed')
    # Exo.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
    Exo.resizable(0,0) 
    Exo.config(background='#ACE5F3')
    Exo_frame = Frame(Exo,bg='#067790', width='500', height='600')
    Exo_frame.place(x=380, y=30)


    btn = Button(Exo_frame,text="Article",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=G_article_notadmin)
    btn.place(x=120,y=160)    
    btn3 = Button(Exo_frame,text="BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=consulter_ajouter_br_pdr)
    btn3.place(x=120,y=280)
    btn4 = Button(Exo_frame,text="BSM", width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=consulter_ajouter_bsm_pdr)
    btn4.place(x=120,y=400)
    
    def annuler():
        Exo.destroy()


    exit_button = Button(Exo, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)

#=======================================Exersise MP========================================
def exercice_MP():
    
    Exo = Toplevel()
    Exo.geometry('500x500')
    Exo.title("Exercice 2023")
    Exo.state('zoomed')
    # Exo.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    Exo.resizable(0,0) 
    Exo.config(background='#ACE5F3')
    Exo_frame = Frame(Exo,bg='#067790', width='500', height='600')
    Exo_frame.place(x=380, y=30)


    btn = Button(Exo_frame,text="Article",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=G_article_notadmin)
    btn.place(x=120,y=160)    
    btn3 = Button(Exo_frame,text="BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=consulter_ajouter_br_mp)
    btn3.place(x=120,y=280)
    btn4 = Button(Exo_frame,text="BSM", width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=consulter_ajouter_bsm_mp)
    btn4.place(x=120,y=400)
    
    def annuler():
        Exo.destroy()


    exit_button = Button(Exo, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)
#==================================================================================================================================
def exercice():
    
    Exo = Toplevel()
    Exo.geometry('500x500')
    Exo.title("Exercice 2023")
    Exo.state('zoomed') 
    # Exo.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    Exo.resizable(0,0) 
    Exo.config(background='#ACE5F3')
    Exo_frame = Frame(Exo,bg='#067790', width='500', height='600')
    Exo_frame.place(x=380, y=30)


    btn = Button(Exo_frame,text="Article",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=G_article)
    btn.place(x=120,y=160)    
    btn3 = Button(Exo_frame,text="BR",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=consulter_ajouter_br)
    btn3.place(x=120,y=280)
    btn4 = Button(Exo_frame,text="BSM", width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=consulter_ajouter_bsm)
    btn4.place(x=120,y=400)
    
    def annuler():
        Exo.destroy()


    exit_button = Button(Exo, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)
#=======================================Fenetre MAGASINER PF==============================================
def ouvrir_fenetre_bienvenue_mag_PF():
    fenetre_bienvenue = Toplevel(lgn_frame)
    fenetre_bienvenue.title("Bienvenue")
    fenetre_bienvenue.config(bg="#D3D3D3")
    fenetre_bienvenue.state('zoomed')
    # fenetre_bienvenue.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
    fenetre_bienvenue.resizable(0,0) 
    fenetre_bienvenue.config(background='#ACE5F3')
    bienvenue_frame = Frame(fenetre_bienvenue,bg='#067790', width='500', height='600')
    bienvenue_frame.place(x=380, y=50)

    message_bienvenue = Label(bienvenue_frame, text="Bienvenue, " + username_entry.get() + " !",font=('yu gothic ui', 26,'bold'),fg="white",bg="#067790")
    message_bienvenue.place(x=50,y=100)
    ex = Button(bienvenue_frame, text="Voir Exercice : 2023", width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=exercice_PF)
    ex.place(x=120, y=300)

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    def deconnecter():
        fenetre_bienvenue.destroy()

    button = Button(fenetre_bienvenue, text="Déconnecter", width='20',bg='red',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=deconnecter)
    button.place(x=1050, y=30)

    def annuler():
        fenetre_bienvenue.destroy()


    exit_button = Button(fenetre_bienvenue, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)
#=======================================Fenètre MAGASINER FB++++++++++++=================================
def ouvrir_fenetre_bienvenue_mag_FB():
    fenetre_bienvenue = Toplevel(lgn_frame)
    fenetre_bienvenue.title("Bienvenue")
    fenetre_bienvenue.config(bg="#D3D3D3")
    fenetre_bienvenue.state('zoomed')     
    fenetre_bienvenue.resizable(0,0) 
    # fenetre_bienvenue.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico') 
    fenetre_bienvenue.config(background='#ACE5F3')
    bienvenue_frame = Frame(fenetre_bienvenue,bg='#067790', width='500', height='600')
    bienvenue_frame.place(x=380, y=50)

    message_bienvenue = Label(bienvenue_frame, text="Bienvenue, " + username_entry.get() + " !",font=('yu gothic ui', 26,'bold'),fg="white",bg="#067790")
    message_bienvenue.place(x=50,y=100)
    ex = Button(bienvenue_frame, text="Voir Exercice : 2023", width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=exercice_FB)
    ex.place(x=120, y=300)

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    def deconnecter():
        fenetre_bienvenue.destroy()

    button = Button(fenetre_bienvenue, text="Déconnecter", width='20',bg='red',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=deconnecter)
    button.place(x=1050, y=30)

    def annuler():
        fenetre_bienvenue.destroy()


    exit_button = Button(fenetre_bienvenue, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)

#=======================================Fenetre MAGASINER PDR===================================
def ouvrir_fenetre_bienvenue_mag_PDR():
    fenetre_bienvenue = Toplevel(lgn_frame)
    fenetre_bienvenue.title("Bienvenue")
    fenetre_bienvenue.config(bg="#D3D3D3")
    fenetre_bienvenue.state('zoomed') 
    # fenetre_bienvenue.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')     
    fenetre_bienvenue.resizable(0,0) 
    fenetre_bienvenue.config(background='#ACE5F3')
    bienvenue_frame = Frame(fenetre_bienvenue,bg='#067790', width='500', height='600')
    bienvenue_frame.place(x=380, y=50)

    message_bienvenue = Label(bienvenue_frame, text="Bienvenue, " + username_entry.get() + " !",font=('yu gothic ui', 26,'bold'),fg="white",bg="#067790")
    message_bienvenue.place(x=50,y=100)
    ex = Button(bienvenue_frame, text="Voir Exercice : 2023", width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=exercice_PDR)
    ex.place(x=120, y=300)

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    def deconnecter():
        fenetre_bienvenue.destroy()

    button = Button(fenetre_bienvenue, text="Déconnecter", width='20',bg='red',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=deconnecter)
    button.place(x=1050, y=30)

    def annuler():
        fenetre_bienvenue.destroy()


    exit_button = Button(fenetre_bienvenue, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)


#=======================================Fenètre MGASINIER MP========================
def ouvrir_fenetre_bienvenue_mag_MP():
    fenetre_bienvenue = Toplevel(lgn_frame)
    fenetre_bienvenue.title("Bienvenue")
    fenetre_bienvenue.config(bg="#D3D3D3")
    fenetre_bienvenue.state('zoomed')  
    # fenetre_bienvenue.iconbitmap('C:\\Users\\hp\\Desktop\\Desktop.2\\star1.ico')    
    fenetre_bienvenue.resizable(0,0) 
    fenetre_bienvenue.config(background='#ACE5F3')
    bienvenue_frame = Frame(fenetre_bienvenue,bg='#067790', width='500', height='600')
    bienvenue_frame.place(x=380, y=50)

    message_bienvenue = Label(bienvenue_frame, text="Bienvenue, " + username_entry.get() + " !",font=('yu gothic ui', 26,'bold'),fg="white",bg="#067790")
    message_bienvenue.place(x=50,y=100)
    ex = Button(bienvenue_frame, text="Voir Exercice : 2023", width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=exercice_MP)
    ex.place(x=120, y=300)

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    def deconnecter():
        fenetre_bienvenue.destroy()

    button = Button(fenetre_bienvenue, text="Déconnecter", width='20',bg='red',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=deconnecter)
    button.place(x=1050, y=30)

    def annuler():
        fenetre_bienvenue.destroy()


    exit_button = Button(fenetre_bienvenue, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)

#============================= Fonction pour ouvrir une nouvelle fenêtre de bienvenue========================================
def ouvrir_fenetre_bienvenue():
    fenetre_bienvenue = Toplevel(lgn_frame)
    fenetre_bienvenue.title("Bienvenue")
    fenetre_bienvenue.config(bg="#D3D3D3")
    fenetre_bienvenue.state('zoomed')
    fenetre_bienvenue.iconbitmap('C:\\Users\\pc\\version1-main\\star.ico')   
    fenetre_bienvenue.resizable(0,0) 
    fenetre_bienvenue.config(background='#ACE5F3')
    bienvenue_frame = Frame(fenetre_bienvenue,bg='#067790', width='500', height='600')
    bienvenue_frame.place(x=380, y=50)

    message_bienvenue = Label(bienvenue_frame, text="Bienvenue, " + username_entry.get() + " !",font=('yu gothic ui', 26,'bold'),fg="white",bg="#067790")
    message_bienvenue.place(x=50,y=100)
    ex = Button(bienvenue_frame, text="Voir Exercice : 2023", width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=exercice)
    ex.place(x=120, y=300)

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    def deconnecter():
        fenetre_bienvenue.destroy()

    button = Button(fenetre_bienvenue, text="Déconnecter", width='20',bg='red',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=deconnecter)
    button.place(x=1050, y=30)

    def annuler():
        fenetre_bienvenue.destroy()


    exit_button = Button(fenetre_bienvenue, text="Retour",width='20',cursor='hand2', command=annuler)
    exit_button.place(x=10, y=630)

    #root.withdraw()           # Pour  Masquer la fenêtre principale


#============================ frame log in=====================================================================================
lgn_frame = Frame(root,bg='#067790', width='500', height='600')
lgn_frame.place(x=380, y=30)

#============================ Fonction afficher/masquer password==============================================================
def toggle_password_visibility():
    if password_entry.cget('show') == '':
        password_entry.configure(show='*')
    else:
        password_entry.configure(show='')

#============================ Créer un bouton de masquage/affichage du mot de passe=============================================
show_password_var = BooleanVar()
show_password_checkbox = Checkbutton(lgn_frame, text='Afficher le mot de passe', variable=show_password_var,bg='#067790',fg='black' ,command=toggle_password_visibility)
show_password_checkbox.place(x=280, y=400)

#============================ Image login ======================================================================================
# user_img = Image.open('C:\\Users\\hp\\Desktop\\Desktop\\logi.png')
# photo = ImageTk.PhotoImage(user_img)
# user_img_panel = Label(root, image=photo, bg='#067790')
# user_img_panel.image = photo
# user_img_panel.place(x=580, y=60) 

#=========================== etiquett Connexion ================================================================================
sign_in_label = Label(lgn_frame, text='Connexion', bg='#067790', fg='white',font=('yu gothic ui', 26,'bold'))
sign_in_label.place(x=165, y=130)

#==========================     Username       ================================================================================
# username_icon = Image.open('C:\\Users\\hp\\Downloads\\user2.png')
# photo = ImageTk.PhotoImage(username_icon)
# username_icon_label = Label(lgn_frame, image=photo, bg='#067790',width='100', height='100')
# username_icon_label.image = photo
# username_icon_label.place(x=40, y=205)

username_label = Label(lgn_frame, text="Nom d'utilisateur",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
username_label.place(x=80, y=210)

username_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg='#067790', fg='black',font=('yu gothic ui',12,'bold'))
username_entry.place(x=120, y=245, width=150)

username_line =Canvas(lgn_frame, width=350, height=2.0,bg='#dbd9b1',highlightthickness=0)
username_line.place(x=80, y=275)

#=========================        Password    ===================================================================================

# password_icon = Image.open('C:\\Users\\hp\\Downloads\\key.png')
# photo = ImageTk.PhotoImage(password_icon)
# password_icon_label = Label(lgn_frame, image=photo, bg='#067790')
# password_icon_label.image = photo
# password_icon_label.place(x=83, y=366)

username_label = Label(lgn_frame, text="Mot de passe",bg='#067790',font=('yu gothic ui', 13,'bold'),fg='white')
username_label.place(x=80, y=330)

password_entry = Entry(lgn_frame, highlightthickness=0,show="*", relief=FLAT, bg='#067790', fg='black',font=('yu gothic ui',12,'bold'))
password_entry.place(x=120, y=365, width=150)

password_line =Canvas(lgn_frame, width=350, height=2.0,bg='#dbd9b1',highlightthickness=0)
password_line.place(x=80, y=395)

#========================= Bouton de connexion =================================================================================
connexion_button = Button(lgn_frame, text="Se connecter",width='25',bg='#ACE5F3',cursor='hand2',font=('yu gothic ui', 13,'bold'),fg='black', command=verifier_identifiants)
message_label = Label(lgn_frame, text="Entrez vos identifiants pour vous connecter.",bg='#067790',font=('yu gothic ui', 10,'bold'),fg='white')
connexion_button.place(x=129,y=440)
message_label.place(x=125,y=500)
   




root.mainloop()
