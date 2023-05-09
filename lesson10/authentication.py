from database import Database
from exception import MyError


class AuthenticationSystem:

    @staticmethod
    def authenticate():
        print("Please, enter your login and password.")
        login = input("Login: ")
        try:
            if not Database.check_existing_login(login):
                raise MyError("Wrong login. Application will terminate.")
        except MyError as error:
            print(error)
            exit()

        while True:
            password = input("Password: ")
            if Database.check_login_password_pair(login, password):
                print(f"Hello, {login}.")
                break
            else:
                print("Wrong password. Try again!")
