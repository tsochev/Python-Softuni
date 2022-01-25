def fill_the_box(height, length, width, *args):
    cube_size = height * length * width
    failed = False
    left_cubes = 0

    for el in args:
        if el == "Finish":
            break

        if el > cube_size and not failed:
            failed = True
            left_cubes += el - cube_size
            continue

        if failed:
            left_cubes += el
        else:
            cube_size -= el

    if failed:
        return f"No more free space! You have {left_cubes} more cubes."
    else:
        return f"There is free space in the box. You could put {cube_size} more cubes."


#print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
