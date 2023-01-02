# Les normes SOLID
# S => Single Responsability
# O => Open/Close

# Arguments de Positions
# Les arguments de Positions sont: name, age
# Définir une valeur par défaut
# display_infos(name ="AISSATA")
# display_infos(name = "AISSATA", age = 18)

# Le fait de passerr une autre class en parametre d'une autre
# On fait un héritage
# Python supporte l'héritage Multiple
# Majority(Enum, Math, Object)

import json
from enumerations import Majority


class Utility:
    @classmethod
    def jump_line(cls, character: str = "\n"):
        print(character)


class Displayer:
    def __init__(self, **options):
        self.options = options

    def to_text(self) -> None:
        for key, value in self.options.items():
            print(f'Votre {key} est: {value}')

    def to_json(self) -> None:
        print(json.dumps(self.options))


class Information:
    LIMIT_AGE = 18

    def __init__(
        self,
        firstname: str,
        lastname: str,
        age: int,
        profession: str,
        salary: float
    ) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.profession = profession
        self.salary = salary

    def _majority(self) -> bool:
        return self.age >= self.LIMIT_AGE

    def full_name(self) -> str:
        return f'{self.firstname} {self.lastname}'

    def update_salary(self, new_salary) -> None:
        self.salary += new_salary

    def is_major(self) -> str:
        if self._majority():
            return Majority.MAJOR
        return Majority.MINOR


def ask_infos() -> tuple:
    firstname = input('Entrer votre prénom: ')
    lastname = input('Entrer votre nom: ')
    age = int(input('Entrer votre age: '))
    profession = input('Entrer votre profession: ')
    salary = float(input('quelle est votre salaire: '))

    return firstname, lastname, age, profession, salary


def main():
    firstname, lastname, age, profession, salary = ask_infos()

    Utility.jump_line()

    displayer = Displayer(
        firstname=firstname,
        lastname=lastname,
        age=age,
        profession=profession,
        salary=salary
    )

    displayer.to_text()

    Utility.jump_line()

    displayer.to_json()

    informations = Information(
        firstname=firstname,
        lastname=lastname,
        age=age,
        profession=profession,
        salary=salary
    )

    Utility.jump_line()

    print(informations.full_name())


if __name__ == '__main__':
    main()
