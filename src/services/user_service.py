""" SERVICIOS DE USUARIO """

from src.model.user import User
from src.utils.file_manager import load_users_from_file

PATH = "src/data/users.txt"

users:list[User] = load_users_from_file(PATH)

def add_user(user: User):
    """ AÑADE USUARIO"""
    users.append(user)

def list_users() -> list[User]:
    """ LISTA USUARIOS"""
    if not users:
        return []
    return users

def find_user_by_id(user_id: int) -> User | None:
    """ BUSCA USUARIO POR ID"""
    for user in users:
        if user.user_id == user_id:
            return user
    return None
