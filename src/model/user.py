""" CLASE USUARIO """

from dataclasses import dataclass

@dataclass
class User:
    """ CLASE USUARIO """
    user_id: int
    name: str
    age: int

    def to_dict(self):
        """ IMPRIME DATOS EN DICCIONARIO """
        return {
            "user_id": self.user_id,
            "name": self.name,
            "age": self.age
        }
