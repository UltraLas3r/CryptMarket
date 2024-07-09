class OpenUser:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def open_my_user_info(self):
        print("This is your user account info")
        print(self.name)
        print(self.account)
