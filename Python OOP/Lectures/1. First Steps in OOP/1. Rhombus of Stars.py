def print_line(space_count, star_count):
    line_spaces = "".join([" "] * space_count)
    line_stars = " ".join(["*"] * star_count)
    print(line_spaces + line_stars)


def print_rhombus(n):
    for i in range(n):
        spaces = n - i - 1
        stars = i + 1
        print_line(spaces, stars)

    for i in range(n - 2, -1, -1):
        spaces = n - i - 1
        stars = i + 1
        print_line(spaces, stars)


print_rhombus(int(input()))
