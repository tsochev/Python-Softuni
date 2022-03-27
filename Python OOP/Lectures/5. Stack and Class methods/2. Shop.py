class Shop:
    _small_shop_capacity = 10

    def __init__(self, name, shop_type, capacity):
        self.name = name
        self.type = shop_type
        self.capacity = capacity
        self.items_count = 0
        self.items = {}

    @classmethod
    def small_shop(cls, name, shop_type):
        return cls(name, shop_type, cls._small_shop_capacity)

    def _can_add_items(self):
        return self.items_count < self.capacity - 1

    def _can_remove_amount_of_item(self, item, amount):
        if item not in self.items:
            return False

        return amount <= self.items[item]

    def add_item(self, item_name):
        if not self._can_add_items():
            return "Not enough capacity in the shop"

        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        self.items_count += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
        if not self._can_remove_amount_of_item(item_name, amount):
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        self.items_count -= amount
        return f"{amount} {item_name} removed from the shop"

    def __str__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
