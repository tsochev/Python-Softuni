rows = int(input())
student_grades = {}
while rows > 0:
    name = input()
    grade = float(input())

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

    rows -= 1

filtered_grades = {}
for student, grades in student_grades.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.5:
        filtered_grades[student] = avg_grade

for k, v in sorted(filtered_grades.items(), key=lambda x: -x[1]):
    print(f"{k} -> {v:.2f}")
