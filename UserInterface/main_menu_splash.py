from UserInterface.OpenUser import OpenUser
from UserInterface.OpenWallet import OpenWallet


class MainMenu:
    def __init__(self, user_name, user_account):
        self.user_name = user_name
        self.user_account = user_account

    main_prompt: str = """~~~!!~-- Cool Crypto Application --~!!~~~

    
        Please Choose from the following options:

        1) View Markets
        2) View Wallet
        3) Purchase 
        4) Sell
        5) Access Super Secret Database info (for in depth data tracking/analysis)

        Enter your selection number: """

    def main_splash(self):
        wallet_view = OpenWallet(self.user_name, self.user_account)
        user_view = OpenUser(self.user_name, self.user_account)

        print(f"\n\n Welcome {self.user_name} -- {self.user_account} -- \n\n")

        while (user_input := input(self.main_prompt)) != "5":
            if user_input == '1':
                user_view.open_my_user_info()

            elif user_input == '2':
                wallet_view.open_my_wallet()

            elif user_input == '3':
                pass

            elif user_input == '4':
               print("SELL SELL SELL SELL")

            elif user_input == '5':
                print("you finna access db info!")

            else:
                print("\n !! please enter a proper input value !! : \n")
