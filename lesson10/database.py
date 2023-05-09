from user import User
import json
from datastorage import DataStorage


class Database:
    users = []
    path = DataStorage.path_to_storage

    @staticmethod
    def dump(db_path=path):
        with open(db_path, "w") as write_file:
            json.dump(Database.users, write_file)

    @staticmethod
    def load(db_path=path):
        try:
            with open(db_path, "r") as read_file:
                Database.users = json.load(read_file)
        except FileNotFoundError as error:
            print(error)
            Database.dump()

    @staticmethod
    def generate_default_database():

        Database.users.append(User("Alex", "111111", "26").get_as_dict())
        Database.users.append(User("Max", "222222", "25").get_as_dict())

        Database.dump()

    @staticmethod
    def check_existing_login(login):
        for user in Database.users:
            if user["Login"] == login:
                return True
        return False

    @staticmethod
    def check_login_password_pair(login, password):
        for user in Database.users:
            if user["Login"] == login and user["Password"] == password:
                return True
        return False
