word_to_remove = input()
sub_sting = input()

while word_to_remove in sub_sting:
    sub_sting = sub_sting.replace(word_to_remove, "")

print(sub_sting)