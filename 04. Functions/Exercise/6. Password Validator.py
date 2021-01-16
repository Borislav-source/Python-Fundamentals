def valid_password(password):
    int_count = 0
    valid_int = False
    valid_str = True
    if 5 < len(password) < 11:
        valid = True
    else:
        valid = False
        print('Password must be between 6 and 10 characters')
    for element in range(len(password)):
        if ord('0') <= ord(password[element]) <= ord('9'):
            int_count += 1
            if int_count >= 2:
                valid_int = True
            else:
                valid_int = False
        elif ord("a") <= ord(password[element]) <= ord("z") or ord("A") <= ord(password[element]) <= ord("Z"):
            pass
        else:
            valid_str = False
    if not valid_str:
        print("Password must consist only of letters and digits")
    if not valid_int:
        print("Password must have at least 2 digits")
    if valid == True and valid_int == True and valid_str == True:
        return True


password = input()
if valid_password(password):
    print("Password is valid")