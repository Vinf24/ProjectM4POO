""" CONTROL PRINCIPAL main.py """

from src.services.client_service import (
    add_client, list_clients, find_client_by_id, create_client,
    edit_client, delete_client
    )
from src.utils.file_manager import save_client_to_file

def main():
    """ PRINCIPAL """
    while True:
        print("1. Add client")
        print("2. List clients")
        print("3. Find client by ID")
        print("4. Save clients to File")
        print("5. Edit client")
        print("6. Delete client")
        print("0. Exit")
        option = input("Select an option: ")

        try:
            match option:
                case "1":
                    client = create_client()
                    if client:
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
                        path = "src/data/clients.json"
                        save_client_to_file(clients, path)
                        print(f"clients saved to {path}")
                case "5":
                    edit_client()
                case "6":
                    delete_client()
                case "0":
                    confirm = input("Save before exit? (y/n): ").strip().lower()

                    if confirm == "y":
                        path = "src/data/clients.json"
                        save_client_to_file(list_clients(), path)
                        print("Clients saved successfully.")

                    print("Exiting program...")
                    break
                case _:
                    print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
