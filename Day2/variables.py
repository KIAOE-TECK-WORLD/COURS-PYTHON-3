# Variables
#
# A chqque variable créée un espace mémoire qui est occupé
# Quand on affecte une valeur à une variable (AFFECTATION)


lastname = 'KUASSI'
firstname = 'ISRAEL'
profession = 'Software Developer'
experience = 5
school = 'ESMT'
diplome = 'INGENIEUR'
sexType = 'M'
salary = 480000.189
tall = 180  # NULL(UNDEFINED)
weight = None


if __name__ == '__main__':
    # Permet de faire la sortie à la console
    print('Informations Personnelles')
    # {0} => 'KUASSI' OR {} => 'KUASSI'
    print('Lastname: {}'.format(lastname))
    # {0} => 'ISRAEL' OR {} => 'ISRAEL'
    print('Firstname: {0}'.format(firstname))
    print('Tall: {0}'.format(tall))
    # {0} => None AND {1} => 'M'
    print('Weight: {0}, SexType: {1}'.format(weight, sexType))
    print('\n')

    print('Informations Professionnelles')
    # {profession} => 'Software Developer'
    print(f'Profession: {profession}')
    # {experience} => 5
    print(f'Experience: {experience}')
    print(f'School: {school}')
    print(f'Degre: {diplome}')
    print(f'Salary: {salary}')
    print('\n')

    print('Informations')
    print('---------------------------')
    print('Informations Personnelles')
    # {0} => 'KUASSI' OR {} => 'KUASSI'
    print('Lastname: {}'.format(lastname))
    # {0} => 'ISRAEL' OR {} => 'ISRAEL'
    print('Firstname: {0}'.format(firstname))
    print('Tall: {0}'.format(tall))
    # {0} => None AND {1} => 'M'
    print('Weight: {0}, SexType: {1}'.format(weight, sexType))
    
    print('**************************')
    print('Informations Professionnelles')
    # {profession} => 'Software Developer'
    print(f'Profession: {profession}')
    # {experience} => 5
    print(f'Experience: {experience}')
    print(f'School: {school}')
    print(f'Degre: {diplome}')
    print(f'Salary: {salary}')
    print('\n')

    # Correction de l'exercice
    print('Informations Personnelles')
    print('Lastname: {0}, Firstname: {1}, Tall: {2}, Weight: {3}, SexType: {4}'.format(lastname, firstname, tall, weight, sexType))
    print('\n')
    print('Informations Professionnelles')
    print(f'Profession: {profession}, Experience: {experience}, School: {school}, Degre: {diplome}, Salary: {salary}')
    print('\n')
