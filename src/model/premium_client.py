""" CLASE CLIENTE PREMIUM premium_client.py """

from src.model.contact_info import ContactInfo
from src.model.client import Client
from src.exceptions.client_exceptions import ClientError, InvalidAddressError

class PremiumClient(Client):
    """ CLIENTE PREMIUM """
    def __init__(self, name, age, email, phone, address, client_id: int | None = None):
        contact = ContactInfo(email=email, phone=phone)
        super().__init__(name, age, contact, client_id)
        self.address = address

    @property
    def address(self) -> str:
        """ DIRECCION DEL CLIENTE """
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        if not isinstance(value, str):
            raise InvalidAddressError("Address must be a string")

        value = value.strip()

        if not value:
            raise InvalidAddressError("Address cannot be empty")

        self._address = value

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
            "address": ("Address", self._edit_address),
        })
        return fields

    def _edit_address(self):
        new_address = input("Enter new address: ")
        try:
            self.address = new_address
        except ClientError as e:
            print(e)
