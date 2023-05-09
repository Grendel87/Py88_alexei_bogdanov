from database import Database


class AuthenticationSystem:

    @staticmethod
    def authenticate():
        print("Please, enter your login and password.")
        while True:
            login = input("Login: ")
            if Database.check_existing_login(login):
                break
            else:
                print("Wrong login. Try again!")
        while True:
            password = input("Password: ")
            if Database.check_login_password_pair(login, password):
                print(f"Hello, {login}.")
                break
            else:
                print("Wrong password. Try again!")
