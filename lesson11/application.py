from authentication import AuthenticationSystem
from registration import RegistrationSystem
from database import Database


class Application:

    @staticmethod
    def run():
        Database.load()
        user_input = input("Are you already registered? Press y/n: ")

        if user_input == "n":
            RegistrationSystem.register()

        AuthenticationSystem.authenticate()
