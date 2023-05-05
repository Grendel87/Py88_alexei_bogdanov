from database import Database
from registration import RegistrationSystem
from authentication import AuthenticationSystem

# Default database -----------------------------------------------------------------------------------------------------

# from user import User
#
# user1 = User("Alex", "111111", "26")
# user2 = User("Max", "222222", "25")
#
# Database.users.append(user1.get_as_dict())
# Database.users.append(user2.get_as_dict())
#
# Database.dump()

# ---------------------------------------------------------------------------------------------------------------------

Database.load()

user_input = input("Are you already registered? Press y/n: ")

if user_input == "n":
    RegistrationSystem.register()

AuthenticationSystem.authenticate()
