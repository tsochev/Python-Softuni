def age_assignment(*args, **kwargs):
    result = {}
    for arg in args:
        first_letter = arg[0]
        result[arg] = kwargs[first_letter]
    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))