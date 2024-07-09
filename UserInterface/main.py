#!/usr/bin/env python
from UserInterface.main_menu_splash import MainMenu


def main(name: str, account: str):
    main_menu = MainMenu(name, account)
    main_menu.main_splash()


if __name__ == '__main__':
    # get user information method

    #inject user information into the following variablesVVVV

    user_name: str = "TEMP NAME"
    user_account: str = "199TEMPACCT"

    main(user_name, user_account)
