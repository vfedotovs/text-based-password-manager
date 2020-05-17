from file_helper_api import find_master_pass_file
from file_helper_api import load_master_pass_file
from file_helper_api import create_master_pass_file
from authenticate_api import pass_auth
from menu_helper_api import *
from start_api import start_app


# Main code driver #
print("*********************************")
print("Text based Password Manager v1.0 ")
print("*********************************\n")

while True:
    start_choice = start_app()
    if find_master_pass_file():
        db_file_unlock_hash = load_master_pass_file()
        auth_reponse = pass_auth(db_file_unlock_hash)
        if auth_reponse:
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
