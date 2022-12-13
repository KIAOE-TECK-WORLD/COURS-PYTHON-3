# Structures de données
# Les listes
#
# Les listes ( Tableau )
# Tableaux:
#   - type est figé pour certains languages
#   - Définir une taille pour certains languages
#   - En python:
#       - La taille est dynamique
#       - Le contenu de la liste est variables
#       - Les listes peuvent contenir des éléments de types différents
#           - Dans une liste on peut avoir:
#               - un STR
#               - un INT
#               - un FLOAT
#               - un BOOL
#               - une LIST ( Une liste dans une liste )
# Syntaxe des listes:
# - Pour déclarer une liste:
#   - list() => instanciaion ( c'est un type )
#   - [] => instanciation
#   - NB: programmation (OOP) toute classe est un type


if __name__ == "__main__":
    # Instanciation d'une liste
    new_list = list() # première methode
    new_list_2 = []   # deuxième méthode
    print('\n')

    # Instanciation d'une liste
    # Pack ( Mis en box deux variable )
    # new_list => list()
    # new_list_2 => []
    new_list, new_list_2 = list(), []

    print('\n')

    # Afficher le type
    print(f'Type de new list est: {type(new_list)}')
    print(f'Type de new list2 est: {type(new_list_2)}')

    print('\n')

    # Taille dynamique
    # Index 0 => "YANON"
    # Index 1 => "DIT"
    # Index 2 => 1000
    new_list = ["YANON", "DIT", 1000, 66.88, [1,2,3]]

    # Accéder aux élément d'une liste
    # On peut utiliser les indexes
    # Le premier d'une liste commence par 0
    print(f'Premier élément est de type: {type(new_list[0])}')
    print(f'Troisième élément est de type: {type(new_list[2])}')
    print(f'Dernier élément est de type: {type(new_list[4])}')
    
    print('\n')
    
    # Avec les listes
    # Accéder au premier élements
    print(f'Premier élément est: {new_list[0]}')
    
    print('\n')
    
    # Accéder au dernier élément
    # Si vous aviez une liste de n éléments
    print(f'Dernier élément est: {new_list[-1]}')
    
    print('\n')
    
    # Les éléments du dernier éléments de la list
    print(f'Dernier élément est: {new_list[4][0]}')
    print(new_list[4][0])
    print(new_list[4][1])
    print(new_list[4][2])
    print(new_list[4][-1])
    
    print('\n')
    
    # Afficher l'ensemble des éléments d'une list
    print('Afficher le contenu de la list')
    print(new_list[:])
    
    print('\n')
    
    # Afficher la liste en sens inverse
    # Prendre la liste en sens inverse par pas de 1
    print('Afficher la liste en sens inverse')
    print(new_list[::-1])
    
    print('\n')
    
    # Afficher la liste en sens inverse
    # Prendre la liste en sens inverse par pas de 2
    print('Afficher la liste en sens inverse par pas de 2')
    print(new_list[::-2])
    
    print('\n')
    
    # Afficher un intervalle de la liste ( SLICE )
    print('Afficher un intervalle de la liste ( SLICE )')
    # [0:3] => Index 0, Index 1, Index 2
    # [1:3] => Index 1, Index 2
    print(new_list[0:3]) # print(new_list[0]) , print(new_list[1]), print(new_list[2])
    print(new_list[1:3])


