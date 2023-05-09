import os
import json
from datastorage import DataStorage


class Database:
    users = []
    path = DataStorage.path_to_storage

    @staticmethod
    def dump(db_path=path):
        with open(db_path, "w") as write_file:
            json.dump(list(Database.users), write_file)

    @staticmethod
    def load(db_path=path):
        if os.path.exists(db_path):
            with open(db_path, "r") as read_file:
                Database.users = json.load(read_file)
        else:
            print(f"{db_path} was not found!")

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
