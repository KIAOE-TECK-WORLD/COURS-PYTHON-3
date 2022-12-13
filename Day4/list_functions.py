# Les fonctions de base d'une liste
# https://docs.python.org/3/tutorial/datastructures.html


if __name__ == '__main__':
    new_list = [] # type list

    # La fonction append() permet d'ajouter un nouvel élément à une liste
    for i in range(1, 10):
        new_list.append(i)
        
        
    # append permet d'ajouter
    # new_list.append('AISSATA')
    new_list.append(1000)
    new_list.append(2000)
    new_list.append(66.88)
    # new_list.append([1, 2, 2])

    print("Première liste new list")
    print(new_list)
    
    print("Liste après renversement")
    new_list = new_list[::-1]
    
    print(new_list)

    # La fonction sort(): les fonction qui nont pas de retour (processus)
    # Cette fonction est de type ( VOID ) ( RIEN )
    # permet d'arranger par ordre croissant
    new_list.sort()
    
    print("Liste après arrangement")
    print(new_list)
    
    
    # La fonction extend()
    new_list.extend([8818.991, 24001.99])
    
    print(new_list)
    
    # La fonction pop()
    # Suppression d'un élément à partir de la fin de la list
    new_list.pop()
    print(new_list)
    
    new_list.pop(1)
    print(new_list)
    
    # La fonction insert()
    # Insert le nouvel élément à l'index fourni et déplace l'ancien élément d'un pas vers la droite
    new_list.insert(0, "AISSATA")
    new_list.insert(0, "YANON")
    new_list.insert(0, "OUMY")
    new_list.insert(0, "MARIE PIERRE")
    print(new_list)
    
    # faire la concatenation de deux listes
    new_list_2 = ["ORANGE", "BANANE"]
    new_list_3 = new_list + new_list_2
    
    print(new_list_3)
    
    new_list_4 = list(range(1, 10))
    
    # Arrangement en ordre décroissant
    # Contrairement à la fonction sort() de la liste sorted return une nouvelle liste
    # La fonction srt() => None
    print(sorted(new_list_4, reverse=True))
    # Par ordre croissnat
    print(sorted(new_list_4, reverse=False))
    
    
    new_list_5 = []
    
    
    
    new_list_4.append(2.06)
    
    new_list_4.append("DOSSO")
    new_list_4.append([166, 9919, 83.0000])
    
    new_list_5.append(1)
    new_list_5.append(2.06)
    new_list_5.append("DOSSO")
    new_list_5.append([166, 9919, 83.0000])

    
    new_list_4.extend(11111)
    new_list_4.extend(new_list_5)
    # new_list_4.extend(new_list_5) => new_list_4.extend([1, 2.06, "DOSSO", [166, 9919, 83.0000]])
