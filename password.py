from tkinter import *
from tkinter.messagebox import *
from outils import *
import hashlib
import random
import string


charactere = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

conditions = [  ("Doit contenir au moins une lettre majuscule.", string.ascii_uppercase),
                ("Doit contenir au moins une lettre minuscule.", string.ascii_lowercase), 
                ("Doit contenir au moins un chiffre.", string.digits),
                ("Doit contenir au moins un caractère spécial.", string.punctuation)]


fenetre = Tk()
fenetre.title("Mot de Passe")

liste_hash = StringVar()
liste_hash.set(recup_mdp())



def generateur():
    entr_mdp.delete(0, END)
    mdp = "".join(random.choice(charactere) for x in range(16))
    entr_mdp.insert(0, mdp)

def validation():

    mdp = entr_mdp.get()
    echec = []

    if len(mdp) < 8:
        echec += ["Doit contenir au moins 8 caractères."]

    for condition in conditions:
        if not test_match(mdp, condition[1]):
            echec += [condition[0]]
    
    if len(echec) > 0:
        showerror("Mot de passe invalide", "\n".join(echec))
        return False

    showinfo("Mot de passe", "Valide")
    enregistrer(mdp, hashlib.sha256(mdp.encode()).hexdigest())
    fenetre.quit()
    


#Interface
frame_mdp = Frame(fenetre)
frame_liste = LabelFrame(fenetre, text="Mots de passe precedent")

lbl_mdp = Label(frame_mdp, text="Mot de passe :")
entr_mdp = Entry(frame_mdp)

btn_valider = Button(frame_mdp, text="Valider", command= validation, width=15)
btn_gen = Button(frame_mdp, text="Generer", command= generateur, width=15)

lbl_liste = Label(frame_liste, textvariable=liste_hash)


frame_mdp.pack(anchor='center', pady=10, padx=10)
frame_liste.pack(anchor='center', pady=10, padx=10, fill=X, expand=YES)
lbl_mdp.grid(row=0, column=0)
entr_mdp.grid(row=0, column=1)
btn_valider.grid(row=1, column=1)
btn_gen.grid(row=1, column=0)
lbl_liste.pack()


fenetre.mainloop()