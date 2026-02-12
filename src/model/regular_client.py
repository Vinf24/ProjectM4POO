""" CLASE CLIENTE REGULAR regular_client.py """

from src.model.contact_info import ContactInfo
from src.model.client import Client

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
