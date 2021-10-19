def loading_bar(num: int):
    loading_points = num // 10
    percent_points = loading_points * "%"
    dot_points = (10 - loading_points) * "."

    if num == 100:
        print(f"100% Complete!\n[%%%%%%%%%%]")
    else:
        print(f"{num}% [{percent_points}{dot_points}]\nStill loading...")


number = int(input())
loading_bar(number)