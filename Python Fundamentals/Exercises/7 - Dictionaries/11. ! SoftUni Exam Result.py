total_points = {}
submissions = {}

data = input()
while not data == "exam finished":
    cmd = data.split("-")

    if "banned" not in data:
        name = cmd[0]
        language = cmd[1]
        points = int(cmd[2])
        if name not in total_points:
            total_points[name] = points
        else:
            if total_points[name] < points:
                total_points[name] = points
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
    else:
        name = cmd[0]
        total_points.pop(name)
    data = input()

print("Result:")
[print(f"{k} | {v}") for k, v in sorted(total_points.items(), key=lambda x: (-x[1], x[0]))]
print("Submissions:")
[print(f"{k} - {v}") for k, v in sorted(submissions.items(), key=lambda x: -x[1],)]
