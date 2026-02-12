""" SERVICIOS DE CLIENTE client_service.py """

from src.model.client import Client
from src.model.regular_client import RegularClient
from src.model.premium_client import PremiumClient
from src.model.corporate_client import CorporateClient
from src.utils.file_manager import load_clients_from_file
from src.exceptions.client_exceptions import ClientTypeError

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
def create_client() -> Client | None:
    """ CREA UN NUEVO CLIENTE """
    print("Client types: 1. Regular - 2. Premium - 3. Corporate")

    while True:
        tipo = input("Enter client type: ")
        try:
            tipo = int(tipo)
            if tipo not in (1, 2, 3):
                raise ClientTypeError("Invalid client type")
            break
        except ValueError:
            print("Must be a number")
        except ClientTypeError as e:
            print(str(e))

    name = input("Enter name: ")
    age = int(input("Enter age: "))

    match tipo:
        case 1:
            email = input("Enter email: ")
            client = RegularClient(name, age, email)
            return client
        case 2:
            email = input("Enter email: ")
            phone = int(input("Enter number phone: "))
            address = input("Enter address: ")
            client = PremiumClient(name, age, email, phone, address)
            return client
        case 3:
            email = input("Enter email: ")
            phone = int(input("Enter phone: "))
            company = input("Enter company: ")
            client = CorporateClient(name, age, email, phone, company)
            return client
        case _:
            print("Invalid option")

    return None

def edit_client():
    """ EDITA ALGUN ATRIBUTO DEL CLIENTE """
    client_id = int(input("Enter an existing ID: "))
    client = find_client_by_id(client_id)

    if not client:
        return
    client.show_menu_edit()
    print("Client updated correctly")

def delete_client():
    """ ELIMINA CLIENTE POR ID """
    client_id = int(input("Enter client ID to delete: "))
    client = find_client_by_id(client_id)

    if not client:
        return

    confirm = input("Are you sure? (y/n): ").strip().lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return

    clients.remove(client)
    print(f"Client ID {client_id} deleted successfully.")
