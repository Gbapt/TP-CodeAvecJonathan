def demander_age(nom):
    age_int = 0
    while age_int == 0:
        age_str = input(f"{nom} quel est votre âge ? ")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR: Veuillez entrez un âge valide !")
    return age_int

def afficher_infos_personne(nom, age):
    print(f"Vous vous appelez {nom} et vous avez {age} ans.")
    print(f"L'an prochain vous aurez {age + 1}")

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

NB_PERSONNE = 3

for i in range(0 + NB_PERSONNE):
    nom = "personne" + str(i + 1)
    age = demander_age(nom)
    afficher_infos_personne(nom, age)
