# Controle de Flux
#
# Syntaxe:
# if ( condition )
# les operateurs de conditions (==, <, >, >=, <=, !=)

# Déclaration de constante
LIMITE_AGE = 18
MINEUR = 'MINEUR'
MAJEUR = 'MAJEUR'

# Types booléens
# False === 0 ( 0 controle de flux => bool(0))
# True === 1 ( 1 controle de flux => bool(1))
# False est le contraire de True
# Si ce n'est False => True <=>
#
# La negation: != / not


if __name__ == '__main__':
    age = int(input('Entrez votre age svp: '))

    if age < LIMITE_AGE:
        print(f'Tu es {MINEUR}')
        print('Tu peux partir')
    else:
        # age >= LIMITE_AGE
        print(f'Tu es {MAJEUR}')
        firstname = input('Entrez votre firstname: ')
        lastname = input('Entrez votre lastname: ')
        sex_type = input('Entrez votre designation: ')
        print(f'Monsieur/Madame {firstname} {lastname} de sexe: {sex_type} peut rentrer')


    print('\n')
    condition = age < LIMITE_AGE

    # condition === False
    if condition:
        print(f'Tu es {MINEUR}')
        print('Tu peux partir')
    else:
        # age >= LIMITE_AGE
        print(f'Tu es {MAJEUR}')
        firstname = input('Entrez votre firstname: ')
        lastname = input('Entrez votre lastname: ')
        sex_type = input('Entrez votre designation: ')
        print(f'Monsieur/Madame {firstname} {lastname} de sexe: {sex_type} peut rentrer')

    # condition === True ( True === not False )
    if not condition:
        print(f'Tu es {MINEUR}')
        print('Tu peux partir')
    else:
        # age >= LIMITE_AGE
        print(f'Tu es {MAJEUR}')
        firstname = input('Entrez votre firstname: ')
        lastname = input('Entrez votre lastname: ')
        sex_type = input('Entrez votre designation: ')
        print(f'Monsieur/Madame {firstname} {lastname} de sexe: {sex_type} peut rentrer')
