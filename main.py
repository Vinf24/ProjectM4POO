""" CONTROL PRINCIPAL main.py """

import sys
from src.repository.client_repository import ClientRepository
from src.services.client_service import (
    create_client, edit_client,
    list_client_purchases, add_purchase_to_client
)
from src.exceptions.client_exceptions import ClientError, DatabaseConnectionError


def main():
    """ PRINCIPAL """
    try:
        repository = ClientRepository()
    except DatabaseConnectionError as e:
        print("Database could not be opened:", e)
        sys.exit()

    while True:
        print("1. Add client")
        print("2. List clients")
        print("3. Find client by ID")
        print("4. Edit client")
        print("5. Delete client")
        print("6. Add purchase to client")
        print("7. List client purchases")
        print("0. Exit")
        option = input("Select an option: ")
        if not option.isdigit():
            print("Invalid option")
            continue

        match option:
            case "1":
                try:
                    client = create_client()
                    if client:
                        repository.save(client)
                        print("client added successfully!")
                    else:
                        print("Client was not created")
                except ClientError as e:
                    print(e)
            case "2":
                clients = repository.find_all()
                if not clients:
                    print("No clients found.")
                else:
                    for client in clients:
                        print(client.to_dict())
            case "3":
                try:
                    client_id = int(input("Enter client ID to find: "))
                except ValueError:
                    print("ID must be a number")
                    continue
                client = repository.find_by_id(client_id)
                if client:
                    print(client.to_dict())
            case "4":
                try:
                    client_id = int(input("Enter client ID to edit: "))
                except ValueError:
                    print("ID must be a number")
                    continue

                client = repository.find_by_id(client_id)

                if not client:
                    print("Client not found.")
                else:
                    changed = edit_client(client)
                    if changed:
                        updated = repository.update(client)
                        if updated:
                            print("Client updated successfully!")
                        else:
                            print("Update failed.")
                    else:
                        print("No changes made. Client was not updated.")
            case "5":
                try:
                    client_id = int(input("Enter client ID to delete: "))
                except ValueError:
                    print("ID must be a number")
                    continue
                deleted = repository.delete(client_id)

                if deleted:
                    print("Client deleted successfully!")
                else:
                    print("Client not found.")
            case "6":
                add_purchase_to_client(repository)
            case "7":
                list_client_purchases(repository)
            case "0":
                print("Exiting program...")
                break
            case _:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
