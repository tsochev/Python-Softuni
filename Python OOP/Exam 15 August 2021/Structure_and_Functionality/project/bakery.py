from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.food_names = set()
        self.drinks_menu = []
        self.drink_names = set()
        self.tables_repository = []
        self.table_numbers = set()
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        food = self.__create_food(food_type, name, price)

        if food.name in self.food_names:
            raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(food)
        self.food_names.add(food.name)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if name in self.drink_names:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = self.__create_drink(drink_type, name, portion, brand)

        self.drinks_menu.append(drink)
        self.drink_names.add(drink.name)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if table_number in self.table_numbers:
            raise Exception(f"Table {table_number} is already in the bakery!")

        table = self.__create_table(table_type, table_number, capacity)

        self.tables_repository.append(table)
        self.table_numbers.add(table.table_number)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        def is_table_free(table):
            return not table.is_reserved and number_of_people <= table.capacity

        free_tables = [t for t in self.tables_repository if is_table_free(t)]

        if len(free_tables) == 0:
            return f"No available table for {number_of_people} people"

        table_to_be_reserved = free_tables[0]
        table_to_be_reserved.reserve(number_of_people)
        return f"Table {table_to_be_reserved.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number, *args):
        # if table_number not in self.table_numbers:
        #     return f"Could not find table {table_number}"
        table = [t for t in self.tables_repository if t.table_number == table_number]

        if len(table) == 0:
            return f"Could not find table {table_number}"

        valid_orders = [self.__get_food_by_name(f) for f in args if f in self.food_names]
        invalid_orders = [f for f in args if f not in self.food_names]

        for order in valid_orders:
            table[0].food_orders.append(order)

        ordered_foods_str = "\n".join(repr(f) for f in valid_orders)
        missing_foods_str = "\n".join(invalid_orders)

        return f"""Table {table_number} ordered:
{ordered_foods_str}
{self.name} does not have in the menu:
{missing_foods_str}"""

    def order_drink(self, table_number, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]

        if len(table) == 0:
            return f"Could not find table {table_number}"

        valid_orders = [self.__get_drink_by_name(d) for d in args if d in self.drink_names]
        invalid_orders = [d for d in args if d not in self.drink_names]

        for order in valid_orders:
            table[0].drink_orders.append(order)

        ordered_drinks_str = "\n".join(repr(d) for d in valid_orders)
        missing_drinks_str = "\n".join(invalid_orders)

        return f"""Table {table_number} ordered:
{ordered_drinks_str}
{self.name} does not have in the menu:
{missing_drinks_str}"""

    def leave_table(self, table_number):
        table = [t for t in self.tables_repository if t.table_number == table_number]

        total_bill = table[0].get_bill()
        table[0].clear()
        self.total_income += total_bill

        return f"""Table: {table_number}
Bill: {total_bill:.2f}"""

    def get_free_tables_info(self):
        table_info = [t.free_table_info() for t in self.tables_repository if not t.is_reserved]
        return "\n".join(table_info)

    def get_total_income(self):
        # total_income = sum([t.get_bill() for t in self.tables_repository])
        return f"Total income: {self.total_income:.2f}lv"

    def __get_food_by_name(self, name):
        foods = [f for f in self.food_menu if f.name == name]
        return foods[0] if foods else None

    def __get_drink_by_name(self, name):
        drinks = [d for d in self.drinks_menu if d.name == name]
        return drinks[0] if drinks else None

    @staticmethod
    def __create_food(food_type, name, price):
        if food_type == Bread.__name__:
            return Bread(name, price)
        if food_type == Cake.__name__:
            return Cake(name, price)
        return None

    @staticmethod
    def __create_drink(drink_type, name, portion, brand):
        if drink_type == Tea.__name__:
            return Tea(name, portion, brand)
        if drink_type == Water.__name__:
            return Water(name, portion, brand)
        return None

    @staticmethod
    def __create_table(table_type, table_number, capacity):
        if table_type == InsideTable.__name__:
            return InsideTable(table_number, capacity)
        if table_type == OutsideTable.__name__:
            return OutsideTable(table_number, capacity)
        return None
