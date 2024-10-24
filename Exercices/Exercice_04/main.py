
"""
Titre = 29.Exercice: Forcer à rentrer un nom


Instructions :

Vérifiez si le nom entrez par l'utilisateur est vide,
si c'est le cas boucler avec WHILE pour forcer l'utilsateur à entrer un nom.

"""



nom = ""

while nom == "":
    nom = input("Quel est votre nom ? ")

print(f"Vous vous appeler {nom}")