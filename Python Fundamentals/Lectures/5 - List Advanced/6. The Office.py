employees = [int(el) for el in input().split()]
factor = int(input())

happiness = [el * factor for el in employees]
average_happy = sum(happiness) / len(happiness)

happy_employee = [el for el in happiness if el >= average_happy]
sad_employee = [el for el in happiness if el < average_happy]

if len(sad_employee) > len(happiness) / 2:
    print(f"Score: {len(happy_employee)}/{len(happiness)}. Employees are not happy!")
else:
    print(f"Score: {len(sad_employee)}/{len(happiness)}. Employees are happy!")


