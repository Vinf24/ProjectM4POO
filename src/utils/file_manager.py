""" GUARDAR CLIENTE EN ARCHIVO file_manager.py """

import json
from src.model.client import Client
from src.utils.client_factory import client_from_dict

def save_client_to_file(clients: list[Client], path: str):
    """ GUARDAR CLIENTE EN ARCHIVO """
    try:
        data = [client.to_dict() for client in clients]

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except OSError as e:
        print(f"Error al guardar el archivo: {e}")

def load_clients_from_file(path: str) -> list[Client]:
    """ CARGAR CLIENTES DEL ARCHIVO """
    clients: list[Client] = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                clients.append(client_from_dict(item))
    except FileNotFoundError:
        print(f"Archivo no encontrado: {path}. Se cargará una lista vacía.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: {path}. Se cargará una lista vacía.")

    return clients
