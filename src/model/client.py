""" CLASE CLIENTE client.py """

from src.model.contact_info import ContactInfo
from src.utils.input_helpers import (
    input_int, input_age, input_phone,
    input_non_empty, input_email
)

class Client:
    """ CLASE CLIENTE """
    _next_id = 1

    def __init__(self, name, age, contact: ContactInfo | None = None, client_id: int | None = None):
        if client_id is None:
            self.client_id = self._generate_id()
        else:
            self.client_id = client_id

        self.name: str = name
        self.age: int = age
        self.contact = contact

    @classmethod
    def _generate_id(cls) -> int:
        """ GENERA ID """
        idx = cls._next_id
        Client._next_id += 1
        return idx

    @classmethod
    def sync_next_id(cls, clients: list["Client"]) -> None:
        """ ASEGURA ID UNICO """
        if clients:
            cls._next_id = max(c.client_id for c in clients) + 1

    @classmethod
    def from_dict(cls, data: dict, contact: ContactInfo | None = None) -> "Client":
        """ CREAR CLIENTE DESDE DICT """
        obj = cls(
            data["name"],
            data["age"],
            contact=contact
        )
        obj.client_id = data["client_id"]
        return obj

    def to_dict(self):
        """ IMPRIME DATOS EN DICCIONARIO """
        return {
            "type": self.__class__.__name__,
            "client_id": self.client_id,
            "name": self._name,
            "age": self.age,
        }

    def get_discount(self) -> float:
        """ ENTREGA DESCUENTO """
        return 0.0

    @property
    def name(self) -> str:
        """ NOMBRE DEL CLIENTE """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Name must be a string")

        value = value.strip()

        if not value:
            raise ValueError("Name cannot be empty")

        if value.isdigit():
            raise ValueError("Name cannot be only numbers")

        self._name = value

    @property
    def age(self) -> int:
        """ EDAD DEL CLIENTE """
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")

        if value < 0:
            raise ValueError("Age cannot be negative")

        if value > 122:
            raise ValueError("Age must be realistic, or NEW RECORD")

        self._age = value

    def __str__(self):
        return f"[{self.__class__.__name__}] ID: {self.client_id}. {self._name} ({self.age})"

    def editable_fields(self) -> dict:
        """ DEFINE CAMPOS EDITABLES """
        return {
            "name": ("Name", self._edit_name),
            "age": ("Age", self._edit_age)
        }

    def _edit_name(self):
        new_name = input_non_empty("Enter new name: ")
        self.name = new_name

    def _edit_age(self):
        new_age = input_age("Enter new age: ")
        self.age = new_age

    def _edit_email(self):
        if not self.contact:
            self.contact = ContactInfo()
        self.contact.email = input_email("Enter new email: ")

    def _edit_phone(self):
        if not self.contact:
            self.contact = ContactInfo()
        self.contact.phone = input_phone("Enter new phone: ")

    def show_menu_edit(self) -> None:
        """ MUESTRA MENU DE OPCIONES EDITABLES """
        fields = self.editable_fields()

        while True:
            print("---OPTIONS TO CHANGE---")
            for i, (_, (label, _)) in enumerate(fields.items(), start=1):
                print(f"{i}. {label}")
            print("0. Exit")

            option = input_int("Select an option: ")
            if option == 0:
                break
            try:
                action = list(fields.values())[option - 1][1]
                action()
            except (IndexError, ValueError):
                print("Invalid input. Please enter a valid option.")

class RegularClient(Client):
    """ CLIENTE REGULAR """
    def __init__(self, name, age, email: str | None = None, client_id: int | None = None):
        contact = ContactInfo(email=email) if email else None
        super().__init__(name, age, contact, client_id)

    @classmethod
    def from_dict(cls, data: dict, contact: ContactInfo | None = None) -> "RegularClient":
        email=contact.email if contact else None
        obj = cls(
            data["name"],
            data["age"],
            email=email
        )
        obj.client_id = data["client_id"]
        return obj

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "client_id": self.client_id,
            "name": self._name,
            "age": self.age,
            "contact": self.contact.to_dict() if self.contact else None
        }

    def get_discount(self) -> float:
        return 0.05

    def __str__(self):
        return (
            f"[{self.__class__.__name__}] ID: {self.client_id}. {self._name} ({self.age})\n"
            f"Contact: {self.contact.email}"
    )

    def editable_fields(self) -> dict:
        fields = super().editable_fields()
        fields["email"] = ("Email", self._edit_email)
        return fields

class PremiumClient(Client):
    """ CLIENTE PREMIUM """
    def __init__(self, name, age, email, phone, address, client_id: int | None = None):
        contact = ContactInfo(email=email, phone=phone)
        super().__init__(name, age, contact, client_id)
        self.address = address

    @classmethod
    def from_dict(cls, data: dict, contact: ContactInfo | None = None) -> "PremiumClient":
        obj = cls(
            data["name"],
            data["age"],
            contact.email,
            contact.phone,
            data["address"]
        )
        obj.client_id = data["client_id"]
        return obj

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "client_id": self.client_id,
            "name": self._name,
            "age": self.age,
            "contact": self.contact.to_dict() if self.contact else None,
            "address": self.address
        }

    def get_discount(self) -> float:
        return 0.15

    def __str__(self):
        return (
    f"[{self.__class__.__name__}] ID: {self.client_id}. {self._name} ({self.age})\n"
    f"Contact: {self.contact.email} - {self.contact.phone}\n"
    f"Address: {self.address}"
    )

    def editable_fields(self) -> dict:
        fields = super().editable_fields()
        fields.update({
            "email": ("Email", self._edit_email),
            "phone": ("Phone", self._edit_phone),
            "adress": ("Address", self._edit_address),
        })
        return fields

    def _edit_address(self):
        self.address = input_non_empty("Enter new address: ")

class CorporateClient(Client):
    """ CLIENTE CORPORATIVO """
    def __init__(self, name, age, email, phone, company, client_id: int | None = None):
        contact = ContactInfo(email=email, phone=phone)
        super().__init__(name, age, contact, client_id)
        self.company = company

    @classmethod
    def from_dict(cls, data: dict, contact: ContactInfo | None = None) -> "CorporateClient":
        obj = cls(
            data["name"],
            data["age"],
            contact.email,
            contact.phone,
            data["company"]
        )
        obj.client_id = data["client_id"]
        return obj

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "client_id": self.client_id,
            "name": self._name,
            "age": self.age,
            "contact": self.contact.to_dict() if self.contact else None,
            "company": self.company
        }

    def get_discount(self) -> float:
        return 0.25

    def __str__(self):
        return (
    f"[{self.__class__.__name__}] ID: {self.client_id}. {self._name} ({self.age})\n"
    f"Contact: {self.contact.email} - {self.contact.phone}\n"
    f"Company: {self.company}"
    )

    def editable_fields(self) -> dict:
        fields = super().editable_fields()
        fields.update({
            "email": ("Email", self._edit_email),
            "phone": ("Phone", self._edit_phone),
            "company": ("Company", self._edit_company),
        })
        return fields

    def _edit_company(self):
        self.company = input_non_empty("Enter new company: ")
