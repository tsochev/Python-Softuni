country_names = input().split(", ")
capitals = input().split(", ")

dict_zipped = zip(country_names, capitals)

for k, v in dict_zipped:
    print(f"{k} -> {v}")