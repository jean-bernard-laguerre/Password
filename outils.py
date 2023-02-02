import json
from tkinter.messagebox import *

def test_match(mot, test):
    
    for char in mot:
        if char in test:
            return True
    return False

def doublon(hash, liste):

    if hash in liste:
        return True
    return False

def enregistrer(mdp, hash_mdp):

    f = open("mdp.json", "r+")
    liste_mdp = json.load(f)

    if not doublon(hash_mdp, liste_mdp["mdp_hash"]):
        liste_mdp["mdp_hash"].append(hash_mdp)
        liste_mdp["mdp"].append(mdp)
        f.seek(0)
        json.dump(liste_mdp, f, indent=4)
    else:
        showerror("Mot de passe invalide", "Deja present")

    f.close()

def recup_mdp():

    f = open("mdp.json", "r")
    liste = json.load(f)
    f.close()

    return "\n".join(liste["mdp"])
