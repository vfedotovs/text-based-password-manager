import pickle


def start_app() -> str:
    """
    Takes user stdin
    Returns: string create or load
    """
    print("**********************")
    print("Password Manager v1.0 ")
    print("**********************\n")
    print("Please enter 'create' for new database file or 'load' to load exiting database file:")
    start_answer = input()
    possible_choices = ['create', 'load']

    while True:
        if start_answer in possible_choices:
            return start_answer

        else:
            print("Please enter valid choise ...")


def load_file() -> str:
    load_file_name = input(
        "Please enter database file to load:")
    try:
        with open(load_file_name, 'r') as f:
            # This will read only first line with pass hash
            first_line = (f.readline())
            pass_hash_str = first_line[11:]
            return pass_hash_str

    except IOError:
        print("Password manager database file not found, do you want to create new file?")


def create_file():
    new_file_name = input(
        "Please enter data base file name example (my_db.txt)")
    first_pass = input("Enter master password for file: ")
    # conf_pass = input("Confirm master password: ") # will be needed for hidden passwords

    with open(new_file_name, 'w') as f:
        code = 'masterpass:'
        hash = code + first_pass    # masterpass:1234
        print(hash)
        f.write(hash)


def pass_auth(passw_hash: str) -> bool:

    def compare_user_input(hash) -> bool:
        unlock_pass = str(input(": "))
        master_pass = hash

        if unlock_pass == master_pass:
            return True
        else:
            return False

    unlocked = False
    print("To unlock database file please enter master password: ")
    unlock_attempt_count = 3
    while unlock_attempt_count > 0:
        # print(unlock_attempt_count)  # only for debug
        if compare_user_input(passw_hash):
            unlocked = True
            break
        else:
            if unlock_attempt_count > 1:
                print(
                    "Entered password was incorrect please try again ... ")

        unlock_attempt_count -= 1
    return unlocked


def get_menu_choice() -> str:
    """
    TODO write proper  decription
    """
    chices_list = ['1', '2', '4', '5', '6']
    print("\nPlease choose option :")
    print("1. List all entries")
    print("2. Crete new entry")
    print("3. Find entry - not implemented")
    print("4. Read file to memory - totest")
    print("5. Save entries to file - ok")
    print("6. Exit application")

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

start_choice = start_app()
if start_choice == 'create':
    create_file()
if start_choice == 'load':
    db_file_unlock_hash = load_file()
    # Try to pass file authentication
    auth_reponse = pass_auth(db_file_unlock_hash)
    if auth_reponse:
        print("Database file was loaded with sucess")
        while True:
            menu_choice = get_menu_choice()
            if menu_choice == '6':
                print("You have choosen exit application ...")
                break
            else:
                process_menu_choice(menu_choice)

    if auth_reponse is False:
        print("Failed to load Database file due to incorrect master password ")
