jobs = [int(x) for x in input().split(", ")]
job_index = int(input())

cycles = sorted([(jobs[index], index) for index in range(len(jobs))])

total_cycles = 0

for x in cycles:
    total_cycles += x[0]
    if x[1] == job_index:
        break

print(total_cycles)