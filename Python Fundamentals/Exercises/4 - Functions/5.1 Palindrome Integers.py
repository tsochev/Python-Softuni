def palindrome_int(my_list):
    for n in my_list:
        for el in n:
            for el_2 in n[::-1]:
                if el == el_2:
                    print("True")
                    break
                else:
                    print("False")
                    break
            break


list_int = list(input().split(", "))
palindrome_int(list_int)