
"""
Titre = 36.Exercice: Fonction afficher


Instructions :

Créer et incrémenter au code exsitant une fonction nommer afficher_information qui permet d'afficher les information d'une personne (le nom et l'âge).

"""



#CODE EXISTANT ci-dessous:
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom

def demander_age(nom):
    age_int = 0
    while age_int == 0:
        age_str = input(f"{nom} quel est votre âge ? ")
        try:
            age_int = int(age_str)
        except:
            print("Veuillez entrer un nombre valide !")
    return age_int


nom = demander_nom()
age = demander_age(nom)
#CODE EXISTANT ci-dessus:


def afficher_information(nom, age):
    print(f"Vous vous appeler {nom}, et vous avez {age} ans.")

infos_personne = afficher_information(nom, age)