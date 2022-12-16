# Manipulation des fonctions


def display_name(name: str) -> None:
    print(f'Votre Nom est: {name}')


def display_infos(
        name: str,
        age: int,
        sex_type: str,
        nationality: str,
        tall: float
) -> None:
    print(f'Votre Nom est: {name}')
    print(f'Votre Age est: {age}')
    print(f'Votre Designation est: {sex_type}')
    print(f'Votre Nationalité est: {nationality}')
    print(f'Votre Taille est de: {tall}m')


def display_fullname(firstname: str, lastname: str) -> str:
    return f'{lastname.upper()} {firstname.capitalize()}'


def main():
    firstname = input('Entrez votre prénom / vos prénoms: ')
    lastname = input('Entrez votre nom de famille: ')
    age = int(input('Entrer votre age: '))
    sex_type = input('Entrez votre désignation: ')
    nationality = input('Entrez votre nationalité: ')
    tall = float(input('Entrez votre taille: '))

    name = display_fullname(firstname=firstname, lastname=lastname)

    display_infos(
        name=name,
        age=age,
        sex_type=sex_type,
        nationality=nationality,
        tall=tall
    )


def area_or_volume(cote: float, choix: int = 1) -> float:
    if choix == 1:
        return math.pow(cote, 2)
    else:
        return math.pow(cote, 3)


def controller(cote: float) -> float:
    while (cote not in [1, 2]):
        cote = float(input('Re entrer un bon chiffre entre 1 ou 2: '))
    else:
        return cote

def main():
    cote = float(input('Entrer le cote: '))
    cote = controller(cote)
    return area_or_volume(cote)


if __name__ == '__main__':
    name = input('Entrer votre Nom: ')
    age = int(input('Entrer votre age: '))
    sex_type = input('Entrer votre sexe: ')
    nationality = input('Entrer votre nationalité: ')
    tall = float(input('Entrer votre taille: '))

    display_infos(
        name=name,
        age=age,
        sex_type=sex_type,
        nationality=nationality,
        tall=tall
    )

    display_infos(
        name,
        age,
        sex_type,
        nationality,
        tall
    )
