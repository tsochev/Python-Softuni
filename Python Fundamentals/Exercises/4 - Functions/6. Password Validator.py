def pass_in_range(new_pass):
    if 6 <= len(new_pass) <= 10:
        return True
    return False


def letters_and_digits_alphanumeric(new_pass):
    return new_pass.isalnum()
    # is_alphanum = True
    # for el in new_pass:
    #     if not el.isalpha() or el.isdigit():
    #         is_alphanum = False
    #         break
    # return is_alphanum


def at_least_two_digit(new_pass):
    count = 0
    for el in new_pass:
        if el.isdigit():
            count += 1
    if count >= 2:
        return True
    else:
        return False


def wrote_pass(new_pass):
    is_valid = True
    if not pass_in_range(new_pass):
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not letters_and_digits_alphanumeric(new_pass):
        print("Password must consist only of letters and digits")
        is_valid = False
    if not at_least_two_digit(new_pass):
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


enter_pass = input()
wrote_pass(enter_pass)