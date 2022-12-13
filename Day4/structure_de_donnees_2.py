# Les dictionnaires
# Sont des structures de données comme les listes
# Syntaxen des dictionnaires

# new_dict = dict()
# new_dict = {}
#   key: value
#   Pour ajouter un élément dans un dictionnaire:
#   new_dict[key] = value


if __name__ == '__main__':
    # Instanciation
    new_dict = dict()
    new_dict_2 = {}

    new_dict, new_dict_2 = dict(), {}

    # print({
    #     'a': 1,
    #     'b': 2,
    #     'c': 3,
    #     'd': 4,
    # })

    # a, b, c, d sont des cles du dictionnaire
    # 1, 2, 3, 4 sont des valeurs du dictionnaire
    # Les valeurs peuvent être de tous les types
    new_dict['a'] = 1
    new_dict['b'] = 2
    new_dict['c'] = 3
    new_dict['d'] = 4

    new_dict['name'] = "DOSSO"  # str
    new_dict['age'] = 28
    new_dict['salary'] = 300000.0919
    new_dict['sex_type'] = "M"
    new_dict['favories'] = [1, 2, 3, 4, 5, 6, 7, 8]

    new_dict['films'] = [{
        'africains': {
            'film_size': 'long',
            'film_type': 'metrage',
            'film_height': 'medium',
            'film_color': 'black',
        },
        'white': {
            'film_size': 'large',
            'film_type': 'short',
            'film_height': 'medium',
            'film_color': 'white',
        },
        'duration': [120, 130, 200]
    }]

    # Les variables c'est en minuscule et c'est du CAMEL_CASE
    # Le nom des constantes qui sont en majuscule
    # Le nom des classe Person
    Person = {}
    Person['tall'] = 160.44
    Person['weight'] = 82
    Person['teint'] = 'black'
    Person['name'] = 'AISSATA'
    Person['location'] = {
        'address': 'RUE 10x22',
        'city': 'DAKAR',
        'state': 'Sénégal',
        'zip': '10000'
    }
    Person['sex'] = 'female'

    # print(Person)
    # Afficher la valeur a partir d'une clé
    # Evite la levée d'exception
    print(Person.get('surname'))

    # Afficher la valeur a partir d'une clé
    # Lève une exception en cas de non existence de la clé
    # print(Person['surname'])
    print('\n')

    print(Person.get('location'))  # fonction get()

    print(type(Person.get('location')))  # type dict

    state = Person \
        .get('location') \
        .get('state')

    city = Person \
        .get('location') \
        .get('city')

    zip = Person \
        .get('location') \
        .get('zip')

    print(state)
    print(city)
    print(zip)

    print('\n')
    print(f'Le state est: {state}, la cité est: {city}, le zip code est: {zip}')

    print('\n')

    # Afficher la liste des clées du dictionnaire person
    print(Person.keys())
    print(list(Person.keys()))
    print('\n')

    # Afficher la liste des valeurs du dictionnaire person
    print(Person.values())
    print(list(Person.values()))
    print('\n')

    # Afficher la liste des (keys, valeurs) du dictionnaire person
    print(list(Person.items()))
