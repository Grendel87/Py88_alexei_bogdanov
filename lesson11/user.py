class User:

    def __init__(self, login="", password="", age=""):
        self.login = login
        self.password = password
        self.age = age

    def update_login(self, login):
        if len(login) < 5 or len(login) > 20:
            print("Login must consists of less than 20 chars and more than 1.")
            return False
        else:
            self.login = login
            return True

    def update_password(self, password):
        if len(password) < 6 or len(password) > 10:
            print("Password must consists of less than 10 chars and more than 5.")
            return False
        else:
            self.password = password
            return True

    def update_age(self, age):
        if not age.isdigit() or int(age) < 18:
            print("You must be over 18 years old!")
            return False
        else:
            self.age = age
            return True

    def get_as_dict(self):
        return {"Login": self.login, "Password": self.password, "Age": self.age}
