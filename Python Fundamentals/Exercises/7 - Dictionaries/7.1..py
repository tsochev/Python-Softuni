courses = {}

data = input()
while not data == "end":
    course, student = data.split(" : ")

    if course not in courses:
        courses[course] = []
    courses[course].append(student)

    data = input()

for k, v in sorted(courses.items(), key=lambda x: -len(x[1])):
    print(f"{k}: {len(v)}")
    for el in sorted(v):
        print(f"-- {el}")