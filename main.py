import pickle
from file_helper_api import find_master_pass_file
from file_helper_api import load_master_pass_file
from file_helper_api import create_master_pass_file
from authenticate_api import pass_auth


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


def get_menu_choice() -> str:
    """
    TODO write proper  decription
    """
    chices_list = ['1', '2', '4', '5', '6']
    print("\nPlease choose option :")
    print("If you have saved your passwords before, use option 4 to load it in memory")
    print(" ")
    print("1. List all password entries - ok")
    print("2. Crete new password entry - ok")
    print("3. Find entry - not implemented")
    print("4. Read file to memory - ok")
    print("5. Save entries to file - ok")
    print("6. Exit application - ok ")

    while True:
        choice = str(input(":"))
        if choice in chices_list:
            return choice
        else:
            print("Please enter valid choice")


class Entry:
    def __init__(self, title, username, passw):
        self.title = title  # rename to title
        self.username = username
        self.passw = passw
        # Add URL
        # Add Notes

    def __str__(self):
        return 'Entry (title=' + self.title + ', UN=' + self.username + ', PWD=' + self.passw + ' )'


def manualy_create_entry():
    print("Creting new entry ... ")
    title = input("Enter entry description: ")
    uname = input("Enter username: ")
    pwd = input("Enter password: ")
    return Entry(title, uname, pwd)


def action_list_entries():
    print("Listing all entries in password manager ... ")
    n = len(all_entry_list)
    if n > 0:
        for e in all_entry_list:
            print(e.__str__())
    else:
        print("Entry list is empty ... please create new entry")


def process_menu_choice(some_choice: str):
    if some_choice == '2':
        entry_obj = manualy_create_entry()
        all_entry_list.append(entry_obj)
        print("Appended new entry to list with success...")
    if some_choice == '1':
        action_list_entries()
    if some_choice == '5':
        save_objects_to_file(all_entry_list)
    if some_choice == '4':
        temp_list = read_objects_to_memory()
        for obj in temp_list:
            all_entry_list.append(obj)


def save_objects_to_file(my_list):
    file_to_save = input("Enter file to save:")
    filehandler = open(file_to_save, 'wb+')
    # for e in all_entry_list:
    #    pickle.dump(e, filehandler)

    # option with dumping whole list
    pickle.dump(all_entry_list, filehandler)
    filehandler.close()


def read_objects_to_memory():

    fn = input("Enter file to open:")

    # read multi items
    with open(fn, 'rb') as f:
        w_list = pickle.load(f)

    return w_list


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
