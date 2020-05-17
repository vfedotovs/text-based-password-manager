from file_helper_api import find_master_pass_file
from file_helper_api import load_master_pass_file
from file_helper_api import create_master_pass_file
from authenticate_api import pass_auth
from menu_helper_api import *


def start_app() -> str:
    """
    Takes user stdin
    Returns: string create or load
    """
    print("*********************************")
    print("Text based Password Manager v1.0 ")
    print("*********************************\n")

    print("Searching for master_pass.bin file ...")
    if find_master_pass_file():
        return 'load'

    else:
        print(
            "Password manager master_pass.bin file was not found.")

        print("Type 'create' to create new MASTER PASSOWORD and save it to new master_pass.bin file")

    # test
    # print(" database file or 'load' to load exiting database file:")
    start_answer = input()
    possible_choices = ['create', 'load']

    while True:
        if start_answer in possible_choices:
            return start_answer

        else:
            print("Please enter valid choise 'create' or 'load'...")


class Entry:
    def __init__(self, title, username, passw):
        self.title = title  # rename to title
        self.username = username
        self.passw = passw
        # Add URL
        # Add Notes

    def __str__(self):
        return 'Entry (title=' + self.title + ', UN=' + self.username + ', PWD=' + self.passw + ' )'



# Main code driver
all_entry_list = []

# load master_pass.bin return  pass string used for auth

while True:
    start_choice = start_app()
    if find_master_pass_file():
        db_file_unlock_hash = load_master_pass_file()
        # Try to pass file authentication
        auth_reponse = pass_auth(db_file_unlock_hash)
        if auth_reponse:
            # print("Database file was loaded with sucess")
            while True:
                menu_choice = get_menu_choice()
                if menu_choice == '6':
                    print("You have choosen exit application ...")
                    break
                else:
                    process_menu_choice(menu_choice)

        if auth_reponse is False:
            print("Failed to unlock app due to incorrect master password ")

    if start_choice == 'create':
        create_master_pass_file()

    if start_choice == 'load':
        pass
