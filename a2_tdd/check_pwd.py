def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    else:
        lowercase_found = False
        uppercase_found = False
        digit_found = False
        symbol_found = False
        for character in pwd:
            if character.islower():
                lowercase_found = True
            elif character.isupper():
                uppercase_found = True
            elif character.isdigit():
                digit_found = True
            elif character in "~`!@#$%^&*()_+-=":
                symbol_found = True
            else:
                return False
        return lowercase_found and uppercase_found and digit_found and symbol_found
