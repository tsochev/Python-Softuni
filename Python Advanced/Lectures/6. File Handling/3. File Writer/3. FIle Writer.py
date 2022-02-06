# file = open("my_first_file.txt", "w")
# file.write("I just created my first file!")


file_path = "my_first_file.txt"
content = "I just created my first file!"
with open(file_path, "W") as file:
    file.write(content)