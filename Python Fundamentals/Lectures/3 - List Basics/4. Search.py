num = int(input())
searched_word = input()

main_list = []
special_list = []

for _ in range(num):
    current_sting = input()
    main_list.append(current_sting)
    if searched_word in current_sting:
        special_list.append(current_sting)
print(main_list)
print(special_list)
