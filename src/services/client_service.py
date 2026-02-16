""" SERVICIOS DE CLIENTE client_service.py """

from src.model.client import Client
from src.model.regular_client import RegularClient
from src.model.premium_client import PremiumClient
from src.model.corporate_client import CorporateClient
from src.model.purchase import Purchase
from src.exceptions.client_exceptions import ClientTypeError, InvalidAgeError, InvalidPhoneError

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
    try:
        age = int(input("Enter age: "))
    except ValueError as e:
        raise InvalidAgeError("Age must be a valid number") from e

    match tipo:
        case 1:
            email = input("Enter email: ")
            client = RegularClient(name, age, email)
            return client
        case 2:
            email = input("Enter email: ")
            try:
                phone = int(input("Enter number phone: "))
            except ValueError as e:
                raise InvalidPhoneError("Phone must be only numbers") from e
            address = input("Enter address: ")
            client = PremiumClient(name, age, email, phone, address)
            return client
        case 3:
            email = input("Enter email: ")
            try:
                phone = int(input("Enter phone: "))
            except ValueError as e:
                raise InvalidPhoneError("Phone must be only numbers") from e
            company = input("Enter company: ")
            client = CorporateClient(name, age, email, phone, company)
            return client
        case _:
            print("Invalid option")

    return None

def edit_client(client: Client):
    """ EDITA UN CLIENTE RECIBIDO """
    if not client:
        return
    original_data = client.to_dict()
    client.show_menu_edit()
    updated_data = client.to_dict()
    return original_data != updated_data

def add_purchase_to_client(repository):
    """ AÑADE COMPRA """
    try:
        client_id = int(input("Enter client ID: "))
        client = repository.find_by_id(client_id)

        if not client:
            print("Client not found.")
            return

        amount = float(input("Enter purchase amount: "))
        description = input("Enter description (optional): ")

        purchase = Purchase(amount, description)
        client.add_purchase(purchase)
        repository.add_purchase(client_id, purchase)

        print("Purchase added successfully.")

    except ValueError:
        print("Invalid numeric input.")

def list_client_purchases(repository):
    """ ENTREGA LISTA DE COMPRAS """
    client_id_input = input("Enter client ID: ")

    if not client_id_input.isdigit():
        print("Invalid ID.")
        return

    client_id = int(client_id_input)

    client = repository.find_by_id(client_id)

    if not client:
        print("Client not found.")
        return

    purchases_data = repository.get_purchases_by_id(client_id)

    if not purchases_data:
        print("This client has no purchases.")
        return

    print(f"\nPurchases for {client.name}:")

    total_spent = 0

    for amount, description, date in purchases_data:
        purchase = Purchase(amount, description)
        purchase.date = date

        total = purchase.calculate_total_with_discount(client)
        total_spent += total

        print(purchase)

    print(f"\nTotal spent (with discounts): {total_spent:.2f}")
