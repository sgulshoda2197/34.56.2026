# 6-m
class User:
    def __init__(self, username, _email, __password):
        self.username = username
        self._email = _email
        self.__password = __password

    def login(self, pw):
        if pw == self.__password:
            print("Login successful")
        else:
            print("Wrong password")

    def change_password(self, old, new):
        if old == self.__password:
            self.__password = new
            print("Password changed successfully")
        else:
            print("Old password is incorrect")

    def info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self._email}")


user1 = User("john_doe", "john@gmail.com", "12345")

user1.info()

user1.login("12345")
user1.change_password("12345", "67890")

user1.login("67890")

7-m
class Brand:
    def __init__(self, ram=16, storage=512, serial="0000"):
        self._ram = ram
        self._storage = storage
        self.__serial = serial

    def upgrade_ram(self, x):
        self._ram += x

    def upgrade_storage(self, x):
        self._storage += x

    def info(self):
        print(f"RAM:{self._ram} Storage:{self._storage}")

b = Brand()
b.info()
