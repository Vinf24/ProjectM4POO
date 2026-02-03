""" COONTROL PRINCIPAL """

from src.model.user import User
from src.services.user_service import add_user, list_users, find_user_by_id
from src.utils.file_manager import save_user_to_file

def main():
    """ PRINCIPAL """
    while True:
        print("1. Add User")
        print("2. List Users")
        print("3. Find User by ID")
        print("4. Save Users to File")
        print("5. Exit")
        option = input("Select an option: ")

        try:
            match option:
                case "1":
                    user_id = int(input("Enter user ID: "))
                    name = input("Enter name: ")
                    age = int(input("Enter age: "))
                    user = User(user_id, name, age)
                    add_user(user)
                    print("User added successfully!")
                case "2":
                    users = list_users()
                    if not users:
                        print("No users found.")
                    else:
                        for user in users:
                            print(user.to_dict())
                case "3":
                    user_id = int(input("Enter user ID to find: "))
                    user = find_user_by_id(user_id)
                    if user:
                        print(user.to_dict())
                case "4":
                    users = list_users()
                    if not users:
                        print("No users to save.")
                    else:
                        path = "src/data/users.txt"
                        save_user_to_file(users, path)
                        print(f"Users saved to {path}")
                case "5":
                    print("Exiting program...")
                    break
                case _:
                    print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
