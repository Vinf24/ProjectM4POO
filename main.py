""" COONTROL PRINCIPAL """

from src.model.client import Client
from src.services.client_service import add_client, list_clients, find_client_by_id
from src.utils.file_manager import save_client_to_file

def main():
    """ PRINCIPAL """
    while True:
        print("1. Add client")
        print("2. List clients")
        print("3. Find client by ID")
        print("4. Save clients to File")
        print("5. Exit")
        option = input("Select an option: ")

        try:
            match option:
                case "1":
                    client_id = int(input("Enter client ID: "))
                    name = input("Enter name: ")
                    age = int(input("Enter age: "))
                    client = Client(client_id, name, age)
                    add_client(client)
                    print("client added successfully!")
                case "2":
                    clients = list_clients()
                    if not clients:
                        print("No clients found.")
                    else:
                        for client in clients:
                            print(client.to_dict())
                case "3":
                    client_id = int(input("Enter client ID to find: "))
                    client = find_client_by_id(client_id)
                    if client:
                        print(client.to_dict())
                case "4":
                    clients = list_clients()
                    if not clients:
                        print("No clients to save.")
                    else:
                        path = "src/data/clients.txt"
                        save_client_to_file(clients, path)
                        print(f"clients saved to {path}")
                case "5":
                    print("Exiting program...")
                    break
                case _:
                    print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
