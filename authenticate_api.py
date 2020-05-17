

def pass_auth(passw_hash: str) -> bool:

    def compare_user_input(hash) -> bool:
        unlock_pass = str(input(": "))
        master_pass = hash

        if unlock_pass == master_pass:
            return True
        else:
            return False

    unlocked = False
    print("To unlock Password Manager app please enter master password: ")
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
