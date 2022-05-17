from abc import ABC, abstractmethod


from project.fish.base_fish import BaseFish


class WaterSuitable:
    @staticmethod
    def check_if_fish_is_suitable(fish_type, aquarium_type):
        if fish_type == "FreshwaterFish":
            return aquarium_type == "FreshwaterAquarium"
        if fish_type == "SaltwaterFish":
            return aquarium_type == "SaltwaterAquarium"
        return None


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []
        self.fish_feed = 0


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([c.comfort for c in self.decorations])

    def add_fish(self, fish: BaseFish):
        if self.capacity == 0:
            return "Not enough capacity."

        water_suitable = WaterSuitable.check_if_fish_is_suitable(fish.__class__.__name__, self.__class__.__name__)

        if water_suitable:
            self.capacity -= 1
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."
        return "Water not suitable."

    def remove_fish(self, fish: BaseFish):
        self.capacity += 1
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            self.fish_feed += 1
            fish.eat()

    def __str__(self):
        result = ""
        result += f"{self.name}:\n"
        result += f"Fish: {' '.join([f.name for f in self.fish]) if self.fish else 'none'}\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}\n"
        return result.strip()


