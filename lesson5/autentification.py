alex1, alex2, alex3, alex4, alex5 = "Alex", "Bob", "Bil", "Ben", "Bro"
names = (alex1, alex2, alex3, alex4, alex5)
passwords = ("11111", "22222", "33333", "44444", "55555")

def get_name():
    name = input("Enter your name:")
    if name == "exit":
        exit()
    if check_name(name) and name in names:
        return name

def check_name(name):
    if len(name) < 2:
        print("Error. The name is too short. The name must contain more than 1 character.")
        return False
    if len(name) > 10:
        print("Error. The name is too long. The name must contain less than 11 characters.")
        return False
    return True

def get_password():
    password = input("Enter your password:")
    if check_password(password) and password in passwords:
        return password


def check_password(password):
    if len(password) < 5:
        print("Error. The password is too short. The password must contain more than 4 character.")
        return False
    return True


while True:
    name = get_name()
    password = get_password()
    if name != None and password !=None:
        print(f"Hey, {name}!")
        break
    print('Authentication Error. Check name or password!')






