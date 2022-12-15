# Les Structures de données
# Une structure de données peut contenir n'importe quel type de données
# Parmis ces types de données on a: STR / INT / FLOAT / BOOL / LIST / DICT / TUPLE
# Déclaration de chacun de ces types:
# - STR: NOM_VARIABLE = "" / ''
# - INT: NOM_VARIABLE = ENTIER ( 1 / 2 / 3 )
# - FLOAT: NOM_VARIABLE = REEL ( 13.99 / 991.081 )
# - BOOL: NOM_VARIABLE = BOOLEAN ( True / False )
# - LIST: NOM_VARIABLE = [] / list()
# - DICT: NOM_VARIABLE = {} / dict()
# - TUPLE: NOM_VARIABLE = () / tuple()


if __name__ == '__main__':
    print('Les structure de données')
    print('Structure de données => STR/INT/FLOAT/LIST/DICT/TUPLE')
    
    List = [
        1, 
        "AISSATA", 
        [1, 2], 
        {'a': 1},
        (1, 2, 3)
    ]

    print(type(List[0])) # INT
    print(type(List[1])) # STR
    print(type(List[2])) # list
    print(type(List[3])) # dict

    print('Pour accéder aux éléments d\'une liste on peut y accéder via les indexes')

    print('\n')
    print('Les listes sont MUTABLES')
    print('Les dictionnaires sont MUTABLES')
    print('Les tuples ne sont pas MUTABLES')

    List = [1, 2, 3]
    Tuple = (1, 2, 3)
    Dict = {'a': 1, 'b': 2}
    
    # Caractère de MUTABILITE des STRUCTURES DE DONNEES
    # 
    # 
    # Les Listes sont MUTABLES
    # Une liste peut supporter l'assignement de valeurs
    List[0] = 100
    print(List[0])

    # Les Tuples ne sont pas MUTABLES
    # TypeError: 'tuple' object does not support item assignment
    # Tuple[0] = 100

    # Le Dictionnaire est MUTABLE
    Dict['a'] = 100
    print(Dict.get('a'))

    print('\n')

    # La fonction du nom de append()
    # Qui permet d'ajouter un élément de tout type à la liste
    List.append(29900) # 29900 (INT)
    List.append(["DIT", "est", "la", "meilleure", "ecole", "de DATASCIENCE à Dakar"])
    List.append((200, 300, 400)) # (200, 300, 400) (TUPLE)
    print(List)

    # Le contenu actul de List + 29900
    List.extend([29900]) # [29900] (List)
    # Le contenu actul de List + 29900, 200, 40200
    List.extend([29900, 200, 40200]) # [29900] (List)
    print(List)

    # Utilisation de la boucle for
    # Par la syntaxe de Python
    # L'iterateur qui prend les valeurs successives de List
    for i in List:
        print(f"L'élément est: {i}")

    print("\n")

    # Utilisation de la boucle for
    # Par l'approche traditionnelle
    # Utiliser l'indexe pour afficher la valeur
    for i in range(0, len(List)):
        print(f"L'élément est: {List[i]}")

    # Une liste a une ligne est un VECTEUR
    # Une liste a une colonne est un VECTEUR
    # Dès que l'ordre de la dimension > 1 ( MATRICE )
    # Une liste
    List = [
        [1, 2], # Une liste ( len() => 2)
        [3, 4], # Une liste ( len() => 2)
        [5, 6], # Une liste ( len() => 2)
    ]

    print("\n")
    for i in List:
        print(f'Level 1 element: {i}')
        for j in i:
            print(f"\t Level 2 element: {j}")

    print("\n")
    for i in List:
        print(f'Element1 est: {i[0]}, element2: {i[1]}')

    List = [
        [
            [1, 2], # Une liste ( len() => 2)
            [1, 2]  # Une liste ( len() => 2)
        ], # Une liste ( len() => 2)
        [
            [3, 4], # Une liste ( len() => 2)
            [3, 4]  # Une liste ( len() => 2)
        ], # Une liste ( len() => 2)
        [
            [4, 5], # Une liste ( len() => 2)
            [4, 5]  # Une liste ( len() => 2)
        ], # Une liste ( len() => 2)
    ]

    print("\n")
    for i in List:
        print(f'Level 1 element: {i}')
        for j in i:
            print(f"\t Level 2 element: {j}")

    print("\n")
    for i in List:
        print(f'Level 1 element: {i}')
        for j in i:
            print(f"\t Level 2 element: {j}")
            for z in j:
                print(f"\t\t Level 3 element: {z}")


    print("\n")
    # Flatter une liste ayant plusieurs niveau
    # De déterminer les niveaux
    # Et FLATTER: ( Flat list )
    for i in List:
        print(f'Element1 est: {i[0][0]}, element2: {i[0][1]}, element3: {i[1][0]}, element4: {i[1][1]}')

    # Un string étant une chaine de caractère
    # Chaine de caractères => Tableau de caractères
    # En python => Liste de caractères
    # Donc on peut utilser l'approche des indexes
    name = "AISSATA"

    print("\n")
    print(name[0])
    print(name[1])
    print(name[2])
    print(name[-1])

    # Passer d'un string à une liste
    print("\n")
    name = "La meillere école de MANAGEMENT DES DONNEES est DIT. Le lien de son site est le https://dit.sn. La rtesponsable de filière est MARIE PIERRE."
    print(name.split())
    print("\n")
    print(name.split(" "))

    datas = name.split(" ")

    school = dict()

    school['name'] = datas[8]
    school['site_url'] = datas[-8]
    school['subject'] = f'{datas[4]} {datas[5]} {datas[6]}'
    school['master'] = '{0} {1}'.format(datas[-2], datas[-1])
    school['city'] = "Dakar"

    print("\n")
    print(school)

    # Corriger site_url
    print("\n")
    school['site_url'] = school.get('site_url').replace('sn.', 'sn')
    print(school.get('site_url'))
    print(school)

    print("\n")
    school['master'] = school.get('master').replace('.', '')
    print(school.get('master'))
    print(school)

    print("\n")
    school['name'] = school.get('name').replace('.', '')
    print(school.get('name'))
    print(school)

    # D'utiliser la fonction update des dictionnaires
    print("\n")

    # Cette fonction return None
    # La fonction update ajoute une key:value si elle n'existait pas ou met à jour la valeur de cette clé si elle existatit déjà
    school.update({"students": 10})
    print(school)

    print('\n')
    school.update({"students": 1000})
    print(school)

    print('\n')
    school.update({"name": 'Dakar Institute of Technology'})
    print(school)

    print('\n')
    # La fonction items() retourne une liste de tuple
    # C'est à dire => [(key1, value1), ..., (keyN, valueN)]
    # (key, value) => Pack variables
    for key, value in school.items():
        print(f'La clé est: {key} et la valeur: {value}')

    
    # Quelques fontions usuelles des strings
    name = "YANON"

    print("\n")
    # Afficher en minuscule un string
    print("Mettre en minuscule un string")
    print(name.lower())

    print("\n")
    # Afficher en majuscule un string
    print("Mettre en majuscule un string")
    print(name.upper())

    print("\n")
    # Afficher la première d'un string en majuscule
    print("Mettre la première lettre du premier mot d'un string en majuscule")
    print(name.capitalize())

    print("\n")

    sentence = "YANON a eu 8.5 hier en code Live"
    # Afficher la première d'un string en majuscule
    print("Mettre les premières lettres de chaque mot d'un string en majuscule")
    print(sentence.title())

    print("\n")

    sentence = "  YANON a eu 8.5 hier en code Live  "
    # Suppression des espaces de début et de fin d'un string
    print("Suppression des espaces de début et de fin d'un string")
    print(sentence.strip())

    print("\n")

    sentence = "  YANON a eu 8.5 hier en code Live  "
    # Suppression des espaces de début et de fin d'un string
    print("Suppression des espaces de début et de fin d'un string")
    print(sentence.replace("  ", ""))

    print("\n")
    sentence = "  YANON a eu 8.5 hier en code Live  "
    
    # sentence.replace(" ", '') -> str
    # sentence.replace(" ", '').title() -> str
    # sentence.replace(" ", '').title().upper() -> str
    # sentence.replace(" ", '').title().upper().lower() -> str
    sentence = sentence \
        .replace("  ", "") \
        .title() \
        .upper() 
    
    print(sentence)




