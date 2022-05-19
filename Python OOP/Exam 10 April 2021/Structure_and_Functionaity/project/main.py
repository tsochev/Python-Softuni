from project.controller import Controller

c = Controller()

# print(c.add_aquarium("FreshwaterAquarium", "Fresh"))
print(c.add_aquarium("SaltwaterAquarium", "Salty"))

print(c.add_decoration("Plant"))
print(c.add_decoration("Ornament"))


print(c.insert_decoration("Salty", "Plant"))

print(c.add_fish("Salty", "SaltwaterFish", "Dojo", "gold", 5))
# print(c.add_fish("Salty", "SaltwaterFish", "Dary", "white", 4))

# print(c.feed_fish("Salty"))
#
# print(c.calculate_value("Salty"))

