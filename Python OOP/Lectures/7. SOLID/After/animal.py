class Animal:
    _sound = None
    _species = None

    def get_species(self):
        return self._species

    def get_sound(self):
        return self._sound


class Cat(Animal):
    _sound = "meow"
    _species = "cat"


class Dog(Animal):
    _sound = "woof-woof"
    _species = "dog"


class Chicken(Animal):
    _sound = "chick-chirick"
    _species = "chiken"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_sound())


animals = [Dog(), Cat(), Chicken()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
