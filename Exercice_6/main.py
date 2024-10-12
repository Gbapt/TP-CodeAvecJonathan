"""
Titre = 39.Exercice: Conditions


Instructions :

Ajouter les conditions suivantes pour l'age dans le code existant.
- age supérieur à soixante, affichez vous êtes senior.
- age inferieur à dix, affichez vous êtes enfant.

"""


#CODE existant ci dessous:
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
            print("ERREUR: Veuillez entrez un âge valide !")
    return age_int

def afficher_informations(nom, age):
    print(f"Vous vous appelez {nom} et vous avez {age} ans.")

nom = demander_nom()
age = demander_age(nom)
infos_personne = afficher_informations(nom, age)

"""if age == 17:
    print("Vous êtes presque majeur.")
elif age == 18:
    print("Vous êtes majeur, Félicitation!")
elif age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.)"""
#CODE existant ci dessus:

if age == 17:
    print("Vous êtes presque majeur.")
elif age == 18:
    print("Vous êtes majeur, Félicitation!")
elif age > 60:
    print("Vous êtes senior.")
elif age >= 18:
    print("Vous êtes majeur.")
elif age < 10:
    print("Vous êtes enfant.")
else:
    print("Vous êtes mineur.")