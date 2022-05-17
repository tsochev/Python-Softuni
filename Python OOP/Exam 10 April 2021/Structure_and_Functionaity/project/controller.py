from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        aquarium = self.__create_aquarium(aquarium_type, aquarium_name)

        if aquarium is None:
            return "Invalid aquarium type."

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        decoration = self.__create_decoration(decoration_type)

        if decoration is None:
            return "Invalid decoration type."

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self._find_aquarium_by_name(aquarium_name)

        if aquarium is not None:
            aquarium.add_decoration(decoration)
            # self.decorations_repository.decorations.remove(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        fish = self.__create_fish(fish_type, fish_name, fish_species, price)

        if fish is None:
            return f"There isn't a fish of type {fish_type}."

        # aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        #
        # if len(aquarium) == 0:
        #     return None
        #
        # return aquarium[0].add_fish(fish)
        aquarium = self._find_aquarium_by_name(aquarium_name)

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name):
        aquarium = self._find_aquarium_by_name(aquarium_name)

        aquarium.feed()
        return f"Fish fed: {aquarium.fish_feed}"

    def calculate_value(self, aquarium_name):
        aquarium = self._find_aquarium_by_name(aquarium_name)

        total_value = sum([f.price for f in aquarium.fish]) + sum([d.price for d in aquarium.decorations])
        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium)

        return result

    @staticmethod
    def __create_aquarium(aquarium_type, aquarium_name):
        if aquarium_type == FreshwaterAquarium.__name__:
            return FreshwaterAquarium(aquarium_name)
        if aquarium_type == SaltwaterAquarium.__name__:
            return SaltwaterAquarium(aquarium_name)
        return None

    @staticmethod
    def __create_decoration(decoration_type):
        if decoration_type == Ornament.__name__:
            return Ornament()
        if decoration_type == Plant.__name__:
            return Plant()
        return None

    @staticmethod
    def __create_fish(fish_type, fish_name, fish_species, price):
        if fish_type == FreshwaterFish.__name__:
            return FreshwaterFish(fish_name, fish_species, price)
        if fish_type == SaltwaterFish.__name__:
            return SaltwaterFish(fish_name, fish_species, price)
        return None

    def _find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
