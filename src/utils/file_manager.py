""" GUARDAR USUARIO EN ARCHIVO """

from src.model.user import User

def save_user_to_file(users: list[User], path: str):
    """ GUARDAR USUARIO EN ARCHIVO """
    try:
        with open(path, "w", encoding="utf-8") as file:
            for user in users:
                file.write(f"{user.user_id},{user.name},{user.age}")
                file.write("\n")
    except OSError as e:
        print(f"Error al guardar el archivo: {e}")

def load_users_from_file(path: str) -> list[User]:
    """ CARGAR USUARIO DEL ARCHIVO """
    users: list[User] = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                user_id, name, age = line.strip().split(",")
                user = User(int(user_id), name, int(age))
                users.append(user)
    except OSError as e:
        print(f"Error al cargar el archivo: {e}")

    return users
