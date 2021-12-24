jobs = [int(x) for x in input().split(", ")]
job_index = int(input())

total_cycles = 0

for x in jobs:
    if x <= jobs[job_index]:
        result = jobs[job_index]
        total_cycles += x

print(total_cycles)