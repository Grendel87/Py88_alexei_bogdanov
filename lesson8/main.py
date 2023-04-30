import json
from user import User


def add_user(db, us):
    db[us.name] = us.password


def check_name(db):
    while True:
        username = input("Enter your username for a registration.\n")
        if username in db.keys():
            print("This username is already taken.")
        elif 10 < len(username) or 2 > len(username):
            print("The name must consists of less than 10 chars and more than 1.")
        else:
            return username


def get_password():
    password = input("Create your password:\n")
    while input("Repeat your password:\n") != password:
        pass
    print("The registration is over. Now you can log-in.\n")
    return password


def login():
    while True:
        username = input("Please, enter your username:\n")
        if username in data.keys():
            print("Correct.")
            break
        else:
            print("Authentication error. Try again.\n")
    while True:
        password = input("Please, enter your password:\n")
        if (username, password) in data.items():
            print(f"Hello, {username}!")
            break
        else:
            print("Authentication error. Try again.\n")


user1 = User("Alex", "11111")
user2 = User("Bob", "22222")
user3 = User("Bil", "33333")
user4 = User("Ben", "44444")
user5 = User("Bro", "55555")

database = {}
add_user(database, user1)
add_user(database, user2)
add_user(database, user3)
add_user(database, user4)
add_user(database, user5)

with open("database.json", "w") as write_file:
    json.dump(database, write_file)

with open("database.json", "r") as f_json:
    data = json.load(f_json)

answer = input("Are you already registered? Press y/n:\n")
if answer == "n":
    user_name = check_name(data)
    user_password = get_password()
    new_user = User(user_name, user_password)
    add_user(data, new_user)
    with open("database.json", "w", encoding="utf8") as file:
        file.write(json.dumps(data, indent=2, ensure_ascii=False))

login()
