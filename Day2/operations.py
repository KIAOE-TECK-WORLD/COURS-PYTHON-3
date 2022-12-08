# Opération
# Opération arithmétiques


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
