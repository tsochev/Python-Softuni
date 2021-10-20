rooms = int(input())
free_chairs = 0
need_chair = True
for el in range(1, rooms + 1):
    chairs, visitors = input().split()
    if len(chairs) < int(visitors):
        needed_chairs = int(visitors) - len(chairs)
        print(f"{needed_chairs} more chairs needed in room {el}")
        need_chair = False
    else:
        free_chairs += len(chairs) - int(visitors)
    rooms -= 1

if need_chair:
    print(f"Game On, {free_chairs} free chairs left")
