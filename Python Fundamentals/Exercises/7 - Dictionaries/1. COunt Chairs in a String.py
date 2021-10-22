text = input().split()
dict_count = {}

for word in text:
    for i in word:
        # if i == " ":
        #     continue
        if i not in dict_count:
            dict_count[i] = 1
        else:
            dict_count[i] += 1

for k, v in dict_count.items():
    print(f"{k} -> {v}")