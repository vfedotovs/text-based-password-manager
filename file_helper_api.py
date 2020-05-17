from os import path


def find_master_pass_file() -> bool:
    """Function check if master_pass.bin is found in current directry

    Returns:
        True if file exist or false if file was not found

    """
    master_pass_file = 'master_pass.bin'
    if path.exists(master_pass_file):
        return True
    else:
        return False


def load_master_pass_file() -> str:
    """Fnction reads  master_pass.bin

    Returns:
        pass_hash_str str: saved master password  in plain text for now       
    """
    print("Loading master_pass.bin file ...")
    file_name = "master_pass.bin"
    try:
        with open(file_name, 'r') as f:
            # This will read only first line with pass hash
            first_line = (f.readline())
            pass_hash_str = first_line[11:]
            return pass_hash_str

    except IOError:
        print("Error opening  master_pass.bin file ... ")


# def load_file() -> str:
#    load_file_name = input(
#        "Please enter database file to load:")
#    try:
#        with open(load_file_name, 'r') as f:
#            # This will read only first line with pass hash
#            first_line = (f.readline())
#            pass_hash_str = first_line[11:]
#            return pass_hash_str
#
#    except IOError:
#        print("Password manager database file not found, do you want to create new file?")


def create_master_pass_file():
    new_file_name = "master_pass.bin"
    first_pass = input("Enter master password for file: ")
    # conf_pass = input("Confirm master password: ") # will be needed for hidden passwords

    with open(new_file_name, 'w') as f:
        code = 'masterpass:'
        hash = code + first_pass    # masterpass:1234 current nonencripted hash algo
        print(hash)
        f.write(hash)
