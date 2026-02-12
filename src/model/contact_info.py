""" CLASE INFORMACION DE CONTACTO contact_info.py """

from src.exceptions.client_exceptions import (
    InvalidEmailError, InvalidPhoneError
)

class ContactInfo:
    """ INFORMACIÓN DE CONTACTO """
    def __init__(self, email: str | None = None, phone: int | None = None):
        self.email = email
        self.phone = phone

    @property
    def email(self):
        """ EMAIL DEL CLIENTE """
        return self._email

    @email.setter
    def email(self, value: str | None):
        if value is None:
            self._email = None
            return
        if "@" not in value or "." not in value:
            raise InvalidEmailError("Invalid email format")
        self._email = value

    @property
    def phone(self) -> int | None:
        """ TELEFONO DEL CLIENTE """
        return self._phone

    @phone.setter
    def phone(self, value: int | None) -> None:
        if value is None:
            self._phone = None
            return

        if not isinstance(value, int):
            raise InvalidPhoneError("Phone must be numeric")

        if len(str(value)) < 8:
            raise InvalidPhoneError("Phone number too short")

        self._phone = value

    def to_dict(self) -> dict:
        """ IMPRIME DATOS EN DICCIONARIO """
        return {
            "email": self.email,
            "phone": self.phone
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ContactInfo":
        """ CREAR INFORMACION DE CONTACTO DESDE DICT """
        return cls(
            email=data.get("email"),
            phone=data.get("phone")
        )
