""" VALIDACIONES EN LOS INPUTS input_helpers.py """

from src.exceptions.client_exceptions import (
    ClientTypeError, InvalidAgeError, InvalidEmailError
)

def input_int(msg: str) -> int:
    """ SOLICITA UN VALOR NUMERICO """
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Please enter a valid number")

def input_age(msg="Enter age: ") -> int:
    """ SOLICITA EDAD """
    while True:
        try:
            age = input_int(msg)
            if age <= 0:
                raise InvalidAgeError("Age must be positive")
            return age
        except InvalidAgeError as e:
            print(e)

def input_phone(msg="Enter phone: ") -> int:
    """ SOLICITA TELEFONO """
    while True:
        phone = input_int(msg)
        if len(str(phone)) < 8:
            print("Invalid number, too short")
        else:
            return phone

def input_email(msg="Enter email: ") -> str:
    """ SOLICITA EMAIL """
    while True:
        try:
            email = input(msg).strip()
            if "@" not in email or "." not in email:
                raise InvalidEmailError("Invalid email format")
            return email
        except InvalidEmailError as e:
            print(e)

def input_non_empty(msg: str) -> str:
    """ SOLICITA UN VALOR NO VACIO """
    while True:
        value = input(msg).strip()
        if value:
            return value
        print("Value cannot be empty")

def input_tipo(msg="Enter client type: ") -> int:
    """ SOLICITA TIPO CLIENTE """
    while True:
        tipo = input_int(msg)
        if tipo not in [1, 2, 3]:
            raise ClientTypeError("Invalid client type")
        return tipo
