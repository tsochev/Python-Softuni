import os


" ------> Version1: Recursion - when we check folders too <------"
def traverse_directories(dir_path, result):
    for x in os.listdir(dir_path):
        file_with_path = os.path.join(dir_path, x)
        if os.path.isfile(file_with_path):
            ext = x.split('.')[-1]
            if ext not in result:
                result[ext] = []
            result[ext].append(x)
        elif os.path.isdir(file_with_path):
            traverse_directories(file_with_path, result)


result = {}
traverse_directories(os.getcwd(), result)

with open("output.txt", "w") as result_file:
    for ext, files in sorted(result.items()):
        result_file.write(f".{ext}")
        result_file.write("\n")
        for file in sorted(files):
            result_file.write(f"--- {file}")
            result_file.write("\n")


"------> Version2: built-in - Fast way <------"
# result = {}
# for root, direction, files in os.walk(os.getcwd()):
#     for file in files:
#         ext = file.split(".")[-1]
#         if ext not in result:
#             result[ext] = []
#         result[ext].append(file)
#
# with open("output.txt", "w") as result_file:
#     for ext, files in sorted(result.items()):
#         result_file.write(f".{ext}")
#         result_file.write("\n")
#         for file in sorted(files):
#             result_file.write(f"--- {file}")
#             result_file.write("\n")

"-------> Version3: Current exercise - get files only from current directory <------"
# def traverse_directories(dir_path, result):
#     for x in os.listdir(dir_path):
#         #file_with_path = os.path.join(dir_path, x)
#         if os.path.isfile(x):
#             ext = x.split('.')[-1]
#             if ext not in result:
#                 result[ext] = []
#             result[ext].append(x)
#
#
# result = {}
# traverse_directories(os.getcwd(), result)
#
# with open("output.txt", "w") as result_file:
#     for ext, files in sorted(result.items()):
#         result_file.write(f".{ext}")
#         result_file.write("\n")
#         for file in sorted(files):
#             result_file.write(f"--- {file}")
#             result_file.write("\n")
