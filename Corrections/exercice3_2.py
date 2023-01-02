# Proposition de YANON
# Retourne un tuple
def ask_person_infos() -> tuple:
    firstname = input('Entrer votre prénom: ')
    lastname = input('Entrer votre nom: ')
    age = int(input('Entrer votre age: '))
    profession = input('Entrer votre profession: ')
    salary = float(input('quelle est votre salaire: '))

    return firstname, lastname, age, profession, salary


# Ne retourne rien ( None )
def display_person_infos(
    firstname: str,
    lastname: str,
    age: int,
    profession: str,
    salary: float
) -> None:
    print(f'Votre prénom est: {firstname}')
    print(f'Votre nom est: {lastname}')
    print(f'Votre age est: {age}')
    print(f'Votre profession est: {profession}')
    print(f'Votre salaire est: {salary}')


def main():
    firstname, lastname, age, profession, salary = ask_person_infos()
    
    display_person_infos(
        firstname=firstname,
        lastname=lastname,
        age=age,
        profession=profession,
        salary=salary,
    )
