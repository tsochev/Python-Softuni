key = int(input())
lines = int(input())

for _ in range(1, lines + 1):
    letter = input()
    final_letter = ord(letter) + key
    print(f"{chr(final_letter)}", end="")
