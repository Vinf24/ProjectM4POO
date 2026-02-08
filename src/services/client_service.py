""" SERVICIOS DE CLIENTE """

from src.model.client import Client
from src.utils.file_manager import load_clients_from_file

PATH = "src/data/clients.txt"

clients:list[Client] = load_clients_from_file(PATH)

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
    return None
