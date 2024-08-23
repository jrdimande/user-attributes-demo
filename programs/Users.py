class User:
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def phonenumber(self, phone_number):
        numeber = phone_number
        print(f"{self.first_name} phone number is {numeber}")

    def password(self, password):
        pswd = password
        print(f"{self.first_name} password is  {pswd}")

    def incriment_login_attemps(self, times):
        self.login_attempts += times
        print(f"Login attemps was incrimented to  {self.login_attempts}")

    def reset_login_attemps(self):
        self.login_attempts = 0
        print(f"Login attempts was reseted to {self.login_attempts}")


user1 = User('ian', 'teddy')
user1.incriment_login(1)
user1.incriment_login(2)
user1.reset_login_attemps()

