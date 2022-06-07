from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    def __init__(self, name: str, budget: float, members_count:int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    def calculate_expenses(self, *args):
        total_expenses = 0
        for el_list in args:
            for el in el_list:
                if isinstance(el, Appliance):
                    total_expenses += el.get_monthly_expense()
                elif isinstance(el, Child):
                    total_expenses += el.cost * 30
        self.expenses = total_expenses

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

