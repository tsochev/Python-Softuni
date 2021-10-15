def calculation(oper, num_1, num_2):
    if oper == "multiply":
        return num_1 * num_2
    elif oper == "divide":
        return num_1 // num_2
    elif oper == "add":
        return num_1 + num_2
    elif oper == "subtract":
        return num_1 - num_2


operation = input()
number_1 = int(input())
number_2 = int(input())

print(calculation(operation, number_1, number_2))
