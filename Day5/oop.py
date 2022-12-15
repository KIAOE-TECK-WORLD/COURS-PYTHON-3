# OOP

# Class, Function, Heritage
# En python, Class, function, heritage, surcharge


# Déclaration d'un fonction
# Functions Lambda

import math

# Importation spécifique du module dont on a besoin.
from modules import treat_file

if __name__ == '__main__':
    print('Déclaration d\'un fonction lambda')

    # Calcul de la surface d'un carré
    # La formule de la surface: cote x cote
    # area = cote * cote = math.pow(cote, 2)
    area_carre = lambda x: math.pow(x,2)

    # Calcul de la surface d'un rectangle
    # La formule de la surface: Longueur x Largeur
    # area = Longueur * Largeur
    area_rectange = lambda x, y: x * y

    # Calcul du volume d'une sphère
    # La formule est: (4 x PI x rxrxr) / 3
    # volume = (4 * math.pi * math.pow(r, 3)) / 3
    volume = lambda x: (4 * math.pi * math.pow(x, 3)) / 3


    # Appeler la lambda expression
    # Calcul de la surface du carré
    print(area_carre(10))
    print(area_carre(20))
    print("\n")

    # Appeler la lambda expression
    # Calcul de la surface du rectangle
    print(area_rectange(10, 20))
    print(area_rectange(20, 30))
    print("\n")

    # Appeler la lambda expression
    # Calcul de la surface du rectangle
    print(volume(10))
    print(volume(20))

    # la déclaration des fonctions
    # On utilise le mot clé def
    # def <NOM_FUNCTION> ( args ):
    #     instructions 1
    #     instructions 2
    #     ..............
    #     ..............
    #     instructions N

    # Equivalent de: area_carre = lambda x: math.pow(x,2)
    def area_carre(x):
        return math.pow(x,2)

    # Equivalent de: area_carre = lambda x: math.pow(x,2)
    # La signature de la fonction spécifie le type de la valeur
    def area_carre(x: float):
        return math.pow(x,2)

    # Equivalent de: area_carre = lambda x: math.pow(x,2)
    # La signature de la fonction spécifie le type de la valeur
    # La signature de la fonction spécifie le type de de retour
    def area_carre(x: float) -> float:
        return math.pow(x,2)

    # Function ne retournant rien 
    def display_name(name: str) -> None:
        print(f'Le nom passé en parametre est: {name}')
        print(f'Bienvenue {name}')


