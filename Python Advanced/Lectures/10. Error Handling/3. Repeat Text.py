try:
    text = input()
    repeated = int(input())
    print(text * repeated)
except ValueError:
    print("Variable times must be an integer")
