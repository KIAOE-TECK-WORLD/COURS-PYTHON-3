# Entré/Sortie (I/O)


lastname = 'KUASSI'
firstname = 'ISRAEL'
profession = 'Software Developer'
diplome = 'INGENIEUR'


if __name__ == '__main__':
    # Afficher
    # La sortie de données en console
    print(f'Lastname: {lastname}')
    print(f'Firstname: {firstname}')
    print(f'Profession: {profession}')
    print(f'Diplôme: {diplome}')
    print('\n')

    # Entrer de données
    # On utilise la fonction input()
    sex_type = input('Entrez votre sex: ')
    experience = input('Entrez vos experiences: ')
    school = input('Entrez le nom de votre école: ')
    salary = input('Entrez vôtre salaire: ')
    print('\n')

    print('Informations: ')
    print(f'Votre sexe est: {sex_type}')
    print(f'Vos experiences sont de: {experience}')
    print(f'Votre école est: {school}')
    print(f'Votre salaire est: {salary}')
    print('\n')

    # type STR ( sex_type )
    # type INT ( experience )
    # type STR ( school )
    # type FLOAT ( salary )

    type_sex = type(sex_type)
    type_experience = type(experience)
    type_school = type(school)
    type_salary = type(salary)
    print('Types des variables:')
    print(f'Le type de sexe est: {type_sex}')
    print(f'Le type des experiences est: {type_experience}')
    print(f"Le type de l'ecole est: {type_school}")
    print(f'Le type du salaire est: {type_salary}')
    print('\n')

    # Casting des types
    # type STR ( sex_type )
    # type INT ( experience )
    # type STR ( school )
    # type FLOAT ( salary )
    #
    # INT => int(<NOM_VARIABLE> (type(NOM_VARIABLE) === STR))
    # FLOAT => float(<NOM_VARIABLE>) (type(NOM_VARIABLE) === STR)
    # STR => str(<NOM_VARIABLE>) (type(NOM_VARIABLE) === INT/FLOAT )
    cast_experience = int(experience)
    cast_salary = float(salary)
    type_cast_experience = type(cast_experience)
    type_cast_salary = type(cast_salary)
    print('Types des variables:')
    print(f'Le type de sexe est: {type_sex}')
    print(f'Le type des experiences est: {type_cast_experience}')
    print(f"Le type de l'ecole est: {type_school}")
    print(f'Le type du salaire est: {type_cast_salary}')
    print('\n')

    cast_experience = str(cast_experience)
    type_cast_experience = type(cast_experience)
    print(f'Le type des experiences est: {type_cast_experience}')
