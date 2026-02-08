""" GUARDAR CLIENTE EN ARCHIVO """

from src.model.client import Client

def save_client_to_file(clients: list[Client], path: str):
    """ GUARDAR CLIENTE EN ARCHIVO """
    try:
        with open(path, "w", encoding="utf-8") as file:
            for client in clients:
                file.write(f"{client.client_id},{client.name},{client.age}")
                file.write("\n")
    except OSError as e:
        print(f"Error al guardar el archivo: {e}")

def load_clients_from_file(path: str) -> list[Client]:
    """ CARGAR CLIENTE DEL ARCHIVO """
    clients: list[Client] = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                client_id, name, age = line.strip().split(",")
                client = Client(int(client_id), name, int(age))
                clients.append(client)
    except OSError as e:
        print(f"Error al cargar el archivo: {e}")

    return clients
