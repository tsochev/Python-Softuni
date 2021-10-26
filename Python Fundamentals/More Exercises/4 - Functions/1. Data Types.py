def int_double_string(text: str, num: str):
    if text == "int":
        num = int(num) *2
        return num
    elif text == "real":
        num = float(num) * 1.5
        return f"{num:.2f}"
    elif text == "string":
        return f"${num}$"


data_type = input()
number = input()
print(int_double_string(data_type, number))