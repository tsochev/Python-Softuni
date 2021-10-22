country_name = input().split(", ")
capitals = input().split(", ")

country_info = zip(country_name, capitals)

for k, v in country_info:
    print(f"{k} -> {v}")