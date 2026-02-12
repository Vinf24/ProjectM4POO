""" CREA OBJETO CLIENTE A PARTIR DEL DICCIONARIO client_factory.py """

from src.model.client import Client
from src.model.regular_client import RegularClient
from src.model.premium_client import PremiumClient
from src.model.corporate_client import CorporateClient
from src.exceptions.client_exceptions import ClientTypeError
from src.model.contact_info import ContactInfo

CLIENT_TYPES = {
    "RegularClient": RegularClient,
    "PremiumClient": PremiumClient,
    "CorporateClient": CorporateClient,
}

def client_from_dict(data: dict) -> Client:
    """ CONSTRUYE CLIENTE DESDE LA INFORMACION DEL DICCIONARIO """
    cls = CLIENT_TYPES.get(data.get("type"))
    if not cls:
        raise ClientTypeError(
            f"Invalid client type: {data.get('type')}"
            )
    contact = None
    if data.get("contact"):
        contact = ContactInfo.from_dict(data["contact"])
    return cls.from_dict(data, contact)
