import re

from user import User
from database import Database


class RegistrationSystem:

    @staticmethod
    def register():
        new_user = User()
        while True:
            login = input("Enter your email for registration: ")
            if not re.match(
                    "^[a-zA-Z0-9_+!#%&'*/=?^{|}-]+((.[a-zA-Z0-9_+!#%&'*/=?^{|}-])*)?([a-zA-Z0-9_+!#%&'*/=?^{|}-])?@[a-zA-Z0-9]([a-zA-Z0-9-]{0,29})?[a-zA-Z0-9]?\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,29})?[a-zA-Z0-9]?$",
                    login):
                print("Error. Please enter your email.")
            else:
                if new_user.update_login(login):
                    if not Database.check_existing_login(new_user.login):
                        break
                    else:
                        print(f"Login '{new_user.login}' is already taken!")
        while True:
            password = input("Enter your password for registration: ")
            if new_user.update_password(password):
                break
        while True:
            repeated_password = input("Repeat your password: ")
            if repeated_password == password:
                break
            else:
                print("Entered passwords do not match.")
        while True:
            age = input("Enter your age for registration: ")
            if new_user.update_age(age):
                break
        Database.users.append(new_user.get_as_dict())
        Database.dump()
        print(f"{new_user.login}, your registration is over.")
