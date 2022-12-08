# Types
# La nature de la valeur de la variable


lastname = 'KUASSI'
firstname = 'ISRAEL'
profession = 'Software Developer'
experience = 5 # A afficher
school = 'ESMT'
diplome = 'INGENIEUR'
sexType = 'M'  # A afficher
salary = 480000.189
tall = 180  # NULL(UNDEFINED)
weight = None
# float_special => 18.0
float_special = 18.
string_special = '480000.189' # A afficher


if __name__ == '__main__':
    # Permet de déterminer le type des variables
    # Pour afficher le type: type(<VARIABLE>)
    # Les types sont: STR, INT, FLOAT, NONETYPE
    # Toutes classe est un Type.
    # STR: ''/"" qui le caractérise
    # INT: 5 OR 2000
    # FLOAT: 18.112, 18.
    # NONETYPE: None
    print(type(lastname))
    print(type(salary))
    print(type(tall))
    print(type(weight))
    print(type(float_special))
    print('\n')

    print(type(experience))
    print(type(sexType))
    print(type(string_special))
    print('\n')

    print(f'Le type de la variable salary est {type(salary)}')
    print(f'Le type de la variable lastname est {type(lastname)}')
    print(f'Le type de la variable weight est {type(weight)}')
    print(f'Le type de la variable experience est {type(experience)}')
    print(f'Le type de la variable sexType est {type(sexType)}')
    print(f'Le type de la variable string_special est {type(string_special)}')
    print(f'Le type de la variable float_special est {type(float_special)}')
    print('\n')

    # Déclaration et assignation
    # Déclaration de variables
    # Assignation de valeur
    type_salary = type(salary)
    type_lastname = type(lastname)
    type_weight = type(weight)
    type_experience = type(experience)
    type_sexType = type(sexType)
    type_string_special = type(string_special)
    type_float_special = type(float_special)

    print(f'Le type de la variable salary est {type_salary}')
    print(f'Le type de la variable lastname est {type_lastname}')
    print(f'Le type de la variable weight est {type_weight}')
    print(f'Le type de la variable experience est {type_experience}')
    print(f'Le type de la variable sexType est {type_sexType}')
    print(f'Le type de la variable string_special est {type_string_special}')
    print(f'Le type de la variable float_special est {type_float_special}')

    print(f'je veux afficher le type de salary {type_salary}')
    print(f'Le type de salary etait: {type_salary}')
