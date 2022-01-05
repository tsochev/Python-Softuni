file_name = "text.txt"

try:
    file = open(file_name, "r")
    print("File found")
except:
    print("File not found")
