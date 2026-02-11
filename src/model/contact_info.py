""" CLASE INFORMACION DE CONTACTO contact_info.py """

from dataclasses import dataclass

@dataclass
class ContactInfo:
    """ INFORMACIÓN DE CONTACTO """
    email: str | None = None
    phone: int | None = None

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
