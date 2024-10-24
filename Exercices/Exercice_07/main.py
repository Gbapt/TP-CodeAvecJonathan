"""

Titre = 49.Exercice: Faire un escalier

Instruction:

- Créer un escalier avec un boucle 'for' qui fera 5 marches 30 pixels avec un départ d'une ligne horizontal de 30pixel également.
- Créer une fonction qui prendra en paramètre 'taille' pour le nombre de pixel et 'nb' pour le nombre de marche à créer. 



import turtle

t = turtle.Turtle()  # Crée une instance de la classe Turtle

t.forward(100)  # Déplace la tortue vers l'avant de 100 unités
t.right(90)
t.forward(45)
t.left(50)

turtle.done()  # Garde la fenêtre ouverte après l'exécution

"""

import turtle

t = turtle.Turtle()

def stair_creation(taille, nb):
    t.forward(taille)
    for i in range(nb):
        t.left(90)
        t.forward(taille)
        t.right(90)
        t.forward(taille)

stair = stair_creation(30, 5)

turtle.done()
