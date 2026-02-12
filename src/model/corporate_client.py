""" CLASE CLIENTE CORPORATIVO corporate_client.py """

from src.model.contact_info import ContactInfo
from src.model.client import Client
from src.exceptions.client_exceptions import ClientError, InvalidCompanyError

class CorporateClient(Client):
    """ CLIENTE CORPORATIVO """
    def __init__(self, name, age, email, phone, company, client_id: int | None = None):
        contact = ContactInfo(email=email, phone=phone)
        super().__init__(name, age, contact, client_id)
        self.company = company

    @property
    def company(self) -> str:
        """ EMPRESA QUE REPRESENTA EL CLIENTE """
        return self._company

    @company.setter
    def company(self, value: str) -> None:
        if not isinstance(value, str):
            raise InvalidCompanyError("Company must be a string")

        value = value.strip()

        if not value:
            raise InvalidCompanyError("company cannot be empty")

        self._company = value

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
        new_company = input("Enter new company: ")
        try:
            self.company = new_company
        except ClientError as e:
            print(e)
