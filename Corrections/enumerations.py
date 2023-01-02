from enum import Enum

class Majority(Enum):
    MINOR = "MINOR", "MINOR"
    MAJOR = "MAJOR", "MAJOR"
    ADULT = "ADULT", "ADULT"


class Sex(Enum):
    MALE = "MALE", "MALE"
    FEMALE = "FEMALE", "FEMALE"


class Currency(Enum):
    XOF = "XOF", "XOF"
    USD = "USD", "USD"
    EUR = "EUR", "EUR"
