""" CLASE CLIENTE """

from dataclasses import dataclass

@dataclass
class Client:
    """ CLASE CLIENTE """
    client_id: int
    name: str
    age: int

    def to_dict(self):
        """ IMPRIME DATOS EN DICCIONARIO """
        return {
            "client_id": self.client_id,
            "name": self.name,
            "age": self.age
        }
