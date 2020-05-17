import pickle


class Entry:
    def __init__(self, title, username, passw):
        self.title = title  # rename to title
        self.username = username
        self.passw = passw
        # Add URL
        # Add Notes

    def __str__(self):
        return 'Entry (title=' + self.title + ', UN=' + self.username + ', PWD=' + self.passw + ' )'


all_entry_list = []  # Password entry database as list


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

    # option with dumping whole list
    pickle.dump(all_entry_list, filehandler)
    filehandler.close()


def read_objects_to_memory():
    """Function reads binary file and returns pickle object dump as list

    """
    file_name = input("Enter file to open:")
    with open(file_name, 'rb') as f:
        obj_dump_as_list = pickle.load(f)
    return obj_dump_as_list
