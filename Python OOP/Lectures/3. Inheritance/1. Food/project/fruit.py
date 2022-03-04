from project.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name

    def __str__(self):
        return f"{self.name} with expiration date to {self.expiration_date}"
