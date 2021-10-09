command = input()

lower_word = ["coding", "dog", "cat", "movie"]
upper_word = ["CODING", "DOG", "CAT", "MOVIE"]
coffees = 0

while not command == "END":
    if command in lower_word:
        coffees += 1
    if command in upper_word:
        coffees += 2
    command = input()
if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)
