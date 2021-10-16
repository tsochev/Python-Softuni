class Party:
    def __init__(self):
        self.people = []


names_count = 0
party = Party()
name = input()
while not name == "End":
    party.people.append(name)
    names_count += 1
    name = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {names_count}")
# print(f"Total: {len(party.people)}")
