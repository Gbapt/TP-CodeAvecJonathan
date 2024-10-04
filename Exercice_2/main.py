
"""
Ligne vide et concaténation


Instructions :

L'administration de notre startup informatique nécessite un programme qui va lister l'identité des employés.

Bonne nouvelle, vous avez été désigné pour réaliser ce programme.

Pour l'instant, votre objectif est de lister l'identité d'un seul employé : Jean Dupont (Développeur)

Point de départ :

Les variables nom et prenom sont déjà définies et possèdent les bonnes valeurs

La sortie du programme affiche déjà le nom et le prénom :

Nom : Dupont
Prénom : Jean


Objectif :

Vous allez rajouter une nouvelle variable profession, qui contiendra la valeur "Développeur"

Vous utiliserez cette nouvelle variable (ainsi que nom et prenom) dans votre code, afin que la sortie du programme soit exactement :

Nom : Dupont
Prénom : Jean
 
Identité : Jean Dupont (Développeur)
"""



nom = "Dupont"
prenom = "Jean"
profession = "Développeur"

print("Nom :")
print(nom)
print("Prénom :")
print(prenom)
print()
print(f"Identité : {prenom} {nom} ({profession})")