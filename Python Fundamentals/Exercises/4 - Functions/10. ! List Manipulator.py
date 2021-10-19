def is_valid_index(collection: list, index: int):
    if 0 <= index < len(collection):
        return True
    return False


def exchange_list(collection: list, index: int):
    exchanged_list = []

    if not is_valid_index(collection, index):
        print("Invalid index")
        exchanged_list = collection
    else:
        left_side_list = collection[:index + 1]
        right_side_list = collection[index + 1:]
        exchanged_list = right_side_list + left_side_list
    return exchanged_list


f_list = input().split()
