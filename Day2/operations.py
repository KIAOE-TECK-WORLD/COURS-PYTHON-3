# Opération
# Opération arithmétiques

# importer le module
import math


lastname = 'KUASSI'
firstname = 'ISRAEL'
profession = 'Software Developer'
experience = 5
school = 'ESMT'
diplome = 'INGENIEUR'
sexType = 'M'
salary = 480000.189
tall = 180
weight = None
float_special = 18.
string_special = '480000.189'


if __name__ == '__main__':
    # Addition
    addition = salary + tall
    print('Addition de deux nombres:')
    print(f'Le résultat est: {addition}')
    print('\n')

    # Soustraction
    soustraction = salary - tall
    inv_soustraction = tall - salary
    print('Soustraction de deux nombres:')
    print(f'Le résultat est: {soustraction}')
    print(f'Le résultat négatif est: {inv_soustraction}')
    print('\n')

    # Multiplication
    multiply = tall * experience * float_special
    print('Multiplication de deux nombres:')
    print(f'Le résultat est: {multiply}')
    print('\n')

    # Division
    division = tall / experience
    print('Division de deux nombres:')
    print(f'Le résultat est: {division}')
    print('\n')

    # Division entière
    # Affiche la partie entire du résultant
    # int // int => ( float ) // => (int)
    #  1 / 4 => 0.25
    ent_division = 1 // 4
    print('Division entiere de deux nombres:')
    print(f'Le résultat est: {ent_division}')
    print('\n')

    # Exposant
    exposant_carre = experience ** 2
    exposant_cube = experience ** 3
    exposant_dix = experience ** 10
    print('Exposant des nombres:')
    print(f'Le résultat au carré est: {exposant_carre}')
    print(f'Le résultat au cube est: {exposant_cube}')
    print(f'Le résultat a exposant 10 est: {exposant_dix}')
    print('\n')

    # Opération avec les strings
    # L'ancienne son contenu sera écrasé
    # Le résultat: INGENIEUR Software Developer
    # On peut faire de l'addition entre les chaines de caractères
    addition = diplome + ' ' + profession
    print("L'addition de deux strings")
    print(f'Le résultat est: {addition}')
    print('\n')

    multiply = diplome * 3
    print("La multiplication de deux strings")
    print(f'Le résultat est: {multiply}')
    print('\n')

    multiply = '*' * 20
    print("La multiplication de deux strings")
    print(f'Le résultat est: {multiply}')
    print('\n')

    # Exposant
    # https://docs.python.org/3/library/math.html
    # https://requests.readthedocs.io/en/latest/
    exposant_carre = math.pow(experience, 2)
    racine_carre = math.sqrt(9)
    print('Exposant des nombres:')
    print(f'Le résultat au carré est: {exposant_carre}')
    print(f'Le résultat de la racine carré est: {racine_carre}')
