# This file needs to be rewritten


def start_app() -> str:
    """Function will check if master password bin file exists will return 'load' str
    In case if master password bin file not found  requests user enter stdin and returns 'create'

    Returns:
        'create' or 'load' : str
    """
    print("Searching for master_pass.bin file ...")
    if find_master_pass_file():
        return 'load'
    else:
        print("Password manager master_pass.bin file was not found.")

    usr_stdin_str = input(
        "Type 'create' to create new MASTER PASSOWORD and save it to new master_pass.bin file")
    possible_choices = ['create', 'load']

    while True:
        if usr_stdin_str in possible_choices:
            return usr_stdin_str
        else:
            print("Please enter valid choise 'create' or 'load'...")
