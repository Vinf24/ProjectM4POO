""" BASE DEL REPOSITORIO client_repository.py """

import sqlite3
from src.utils.client_factory import client_from_dict
from src.model.purchase import Purchase
from src.exceptions.client_exceptions import (
    DatabaseConnectionError, DatabaseSchemaError,
    DatabaseWriteError, DatabaseReadError, DatabaseDeleteError
)

class ClientRepository:
    """ PERSISTENCIA SQLITE """

    def __init__(self, db_path: str = "src/data/clients.db"):
        self.db_path = db_path
        self._create_tables()

    def _create_tables(self):
        """ CREA LAS TABLAS """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                # Tabla Clientes
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS clients (
                        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        email TEXT NOT NULL,
                        phone TEXT,
                        type TEXT NOT NULL,
                        address TEXT,
                        company TEXT
                    )
                """)

                # Tabla Compras
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS purchases (
                        purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        client_id INTEGER NOT NULL,
                        amount REAL NOT NULL,
                        description TEXT,
                        date TEXT NOT NULL,
                        FOREIGN KEY (client_id) REFERENCES clients(client_id)
                    )
                """)

                conn.commit()
        except sqlite3.OperationalError as e:
            raise DatabaseConnectionError("Cannot open or access database file") from e
        except sqlite3.Error as e:
            raise DatabaseSchemaError("Failed creating database schema") from e

    def save(self, client):
        """ GUARDA CLIENTE EN LA BASE DE DATOS """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                cursor.execute("""
                    INSERT INTO clients (
                        name,
                        age,
                        email,
                        phone,
                        type,
                        address,
                        company
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    client.name,
                    client.age,
                    client.contact.email,
                    client.contact.phone,
                    client.__class__.__name__,
                    getattr(client, "address", None),
                    getattr(client, "company", None)
                ))

                client.client_id = cursor.lastrowid
                conn.commit()
        except sqlite3.IntegrityError as e:
            raise DatabaseWriteError("Client violates database constraints") from e
        except sqlite3.Error as e:
            raise DatabaseWriteError("Failed saving client") from e

    def find_all(self):
        """ RETORNA CLIENTES DESDE DB """
        clients = []
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM clients")
                rows = cursor.fetchall()

                for row in rows:
                    (
                        client_id,
                        name,
                        age,
                        email,
                        phone,
                        client_type,
                        address,
                        company
                    ) = row

                    client_data = {
                        "client_id": client_id,
                        "name": name,
                        "age": age,
                        "type": client_type,
                        "contact": {
                            "email": email,
                            "phone": phone
                        }
                    }

                    if address:
                        client_data["address"] = address

                    if company:
                        client_data["company"] = company

                    client = client_from_dict(client_data)
                    clients.append(client)

            return clients
        except sqlite3.Error as e:
            raise DatabaseReadError("Failed retrieving clients") from e

    def find_by_id(self, client_id: int):
        """ BUSCA CLIENTE POR ID """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                cursor.execute(
                    "SELECT * FROM clients WHERE client_id = ?",
                    (client_id,)
                )

                row = cursor.fetchone()

                if not row:
                    return None

                (
                    client_id,
                    name,
                    age,
                    email,
                    phone,
                    client_type,
                    address,
                    company
                ) = row

                client_data = {
                    "client_id": client_id,
                    "name": name,
                    "age": age,
                    "type": client_type,
                    "contact": {
                        "email": email,
                        "phone": phone
                    }
                }

                if address:
                    client_data["address"] = address

                if company:
                    client_data["company"] = company

                return client_from_dict(client_data)
        except sqlite3.Error as e:
            raise DatabaseReadError(f"Failed retrieving client id={client_id}") from e

    def get_purchases_by_id(self, client_id: int):
        """ ENTREGA COMPRAS DEL CLIENTE SELECCIONADO """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT amount, description, date
                    FROM purchases
                    WHERE client_id = ?
                """, (client_id,))
                return cursor.fetchall()
        except sqlite3.Error as e:
            raise DatabaseReadError(f"Failed retrieving purchases for client {client_id}") from e

    def delete(self, client_id: int) -> bool:
        """ ELIMINA UN CLIENTE """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                cursor.execute(
                    "DELETE FROM clients WHERE client_id = ?",
                    (client_id,)
                )

                conn.commit()

                return cursor.rowcount > 0
        except sqlite3.Error as e:
            raise DatabaseDeleteError(f"Failed deleting client {client_id}") from e

    def update(self, client) -> bool:
        """ ACTUALIZA UN CLIENTE EXISTENTE """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                cursor.execute("""
                    UPDATE clients
                    SET
                        name = ?,
                        age = ?,
                        email = ?,
                        phone = ?,
                        type = ?,
                        address = ?,
                        company = ?
                    WHERE client_id = ?
                """, (
                    client.name,
                    client.age,
                    client.contact.email if client.contact else None,
                    client.contact.phone if client.contact else None,
                    client.__class__.__name__,
                    getattr(client, "address", None),
                    getattr(client, "company", None),
                    client.client_id
                ))

                conn.commit()

                return cursor.rowcount > 0
        except sqlite3.Error as e:
            raise DatabaseWriteError(f"Failed updating client {client.client_id}") from e

    def add_purchase(self, client_id: int, purchase: Purchase):
        """ AÑADE COMPRA A LA DB """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO purchases (client_id, amount, description, date)
                    VALUES (?, ?, ?, ?)
                """, (
                    client_id,
                    purchase.amount,
                    purchase.description,
                    purchase.date
                ))
                conn.commit()
        except sqlite3.Error as e:
            raise DatabaseWriteError(f"Failed saving purchase for client {client_id}") from e
