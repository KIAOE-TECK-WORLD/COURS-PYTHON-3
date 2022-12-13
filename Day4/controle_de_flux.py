# Controle de flux (Part 2)
# Les conditions


# Suppose qu'on a Mentions
# Moy >= 9 & < 11 => Passable
# Moy >= 11 & < 14 => Assez Bien
# Moy >= 14 & < 17 => Bien
# Moy >= 17 => Très bien
#
# Matiere Mathématiques ( 1 )
# 	- Note / 20: A demander en console
# 	- Coeff des maths: 6
# 	- Moy / 20 = Note demander
# 	- Moy coefficié = (Moy / 20) * 6
#
# Matiere français ( 2 )
# 	- Note / 20: A demander en console
# 	- Coeff des maths: 6
# 	- Moy / 20 = Note demander
# 	- Moy coefficié = (Moy / 20) * 6
#
#
# Font a ligature: operator mon lig, fira code

FAIBLE = "FAIBLE"
PASSABLE = "PASSABLE"
ASSEZ_BIEN = "ASSEZ_BIEN"
BIEN = "BIEN"
TRES_BIEN = "TRES_BIEN"

if __name__ == "__main__":
    note_math = input('Entrez note maths: ')
    note_french = input('Entrez note français: ')

    moy = (float(note_math) + float(note_french)) / 2

    if moy >= 17:
        print(f'Votre mention est: {TRES_BIEN}')
    elif (moy < 17) and (moy >= 14):
        print(f'Votre mention est: {BIEN}')
    elif (moy < 14) and (moy >= 11):
        print(f'Votre mention est: {ASSEZ_BIEN}')
    elif (moy < 11) and (moy >= 9):
        print(f'Votre mention est: {PASSABLE}')
    else:
        print(f'Votre mention est: {FAIBLE}')
