""" SERVICIOS DE CLIENTE client_service.py """

from src.model.client import Client, RegularClient, PremiumClient, CorporateClient
from src.utils.file_manager import load_clients_from_file
from src.utils.input_helpers import (
    input_int, input_age, input_phone,
    input_non_empty, input_email, input_tipo
)

PATH = "src/data/clients.json"

clients: list[Client] = load_clients_from_file(PATH)
Client.sync_next_id(clients)

def add_client(client: Client):
    """ AÑADE CLIENTE"""
    clients.append(client)

def list_clients() -> list[Client]:
    """ LISTA CLIENTES"""
    if not clients:
        return []
    return clients

def find_client_by_id(client_id: int) -> Client | None:
    """ BUSCA CLIENTE POR ID"""
    for client in clients:
        if client.client_id == client_id:
            return client
    print("Client doesn't exist")
    return None
def create_client():
    """ NEW CLIENT """
    print("Client types: 1. Regular - 2. Premium - 3. Corporate")
    tipo = input_tipo()
    name = input_non_empty("Enter name: ")
    age = input_age()
    email = input_email()
    match tipo:
        case 1:
            return RegularClient(name, age, email)
        case 2:
            phone = input_phone()
            address = input_non_empty("Enter address: ")
            return PremiumClient(name, age, email, phone, address)
        case 3:
            phone = input_phone()
            company = input_non_empty("Enter company: ")
            return CorporateClient(name, age, email, phone, company)
        case _:
            print("Invalid client type selected")

def edit_client():
    """ EDITA ALGUN ATRIBUTO DEL CLIENTE """
    client_id = input_int(msg="Enter an existing ID: ")
    client = find_client_by_id(client_id)

    if not client:
        return
    client.show_menu_edit()
    print("Client updated correctly")

def delete_client():
    """ ELIMINA CLIENTE POR ID """
    client_id = input_int("Enter client ID to delete: ")
    client = find_client_by_id(client_id)

    if not client:
        return

    confirm = input("Are you sure? (y/n): ").strip().lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return

    clients.remove(client)
    print(f"Client ID {client_id} deleted successfully.")
