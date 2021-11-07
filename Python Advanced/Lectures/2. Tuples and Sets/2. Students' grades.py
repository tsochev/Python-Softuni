def avg(values):
    return sum(values) / len(values)


num_students = int(input())

students = {}

for _ in range(num_students):
    name, grade_string = input().split()
    grade = float(grade_string)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    average_grade = avg(grades)
    grades_str = " ".join(str(f"{x:.2f}") for x in grades)
    print(f"{name} -> {grades_str} (avg: {average_grade:.2f})")