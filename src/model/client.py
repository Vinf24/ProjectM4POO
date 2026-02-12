""" CLASE CLIENTE client.py """

from src.model.contact_info import ContactInfo
from src.exceptions.client_exceptions import (
    InvalidEmailError, InvalidNameError,
    InvalidPhoneError, InvalidAgeError, ClientError
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
            raise InvalidNameError("Name must be a string")

        value = value.strip()

        if not value:
            raise InvalidNameError("Name cannot be empty")

        if any(char.isdigit() for char in value):
            raise InvalidNameError("Name can't have numbers")

        self._name = value

    @property
    def age(self) -> int:
        """ EDAD DEL CLIENTE """
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise InvalidAgeError("Age must be an integer")

        if value < 0:
            raise InvalidAgeError("Age cannot be negative")

        if value > 122:
            raise InvalidAgeError("Age must be realistic, or NEW RECORD")

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
        new_name = input("Enter new name: ")
        self.name = new_name

    def _edit_age(self):
        new_age = input("Enter new age: ")
        self.age = new_age

    def _edit_email(self):
        value = input("Enter new email: ").strip()
        if not value:
            return
        if not self.contact:
            self.contact = ContactInfo()
        try:
            self.contact.email = value
        except InvalidEmailError as e:
            print(e)

    def _edit_phone(self):
        value = input("Enter new phone: ").strip()
        if not value:
            return
        if not value.isdigit():
            print("Phone must contain only numbers")
            return
        if not self.contact:
            self.contact = ContactInfo()
        try:
            self.contact.phone = int(value)
            print("Phone updated successfully")
        except InvalidPhoneError as e:
            print(e)

    def show_menu_edit(self) -> None:
        """ MUESTRA MENU DE OPCIONES EDITABLES """
        fields = self.editable_fields()

        while True:
            print("---OPTIONS TO CHANGE---")
            for i, (_, (label, _)) in enumerate(fields.items(), start=1):
                print(f"{i}. {label}")
            print("0. Exit")

            try:
                option = int(input("Select an option: "))
                if option == 0:
                    break
                try:
                    action = list(fields.values())[option - 1][1]
                    action()
                except ClientError as e:
                    print(e)
            except (IndexError, ValueError):
                print("Invalid input. Please enter a valid option.")
