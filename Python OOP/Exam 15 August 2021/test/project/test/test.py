from unittest import TestCase, main

from project.pet_shop import PetShop


class PetShopTests(TestCase):
    def setUp(self):
        self.pet = PetShop("Shop")

    def test_init(self):
        self.assertEqual("Shop", self.pet.name)
        self.assertEqual({}, self.pet.food)
        self.assertEqual([], self.pet.pets)

    def test_add_food__when_quantity_is_0__expect_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.pet.add_food("Food", 0)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food__when_quantity_is_below_0__expect_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.pet.add_food("Food", -2)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food__when_increase_quantity_of_food(self):
        quantity = 20
        food = "Food"
        self.pet.add_food(food, quantity)

        self.assertEqual({food: quantity}, self.pet.food)
        self.assertEqual(f"Successfully added {quantity:.2f} grams of {food}.", self.pet.add_food(food, quantity))

    def test_add_pet__when_pet_exist__expect_raise(self):
        self.pet.add_pet("pet")
        with self.assertRaises(Exception) as ex:
            self.pet.add_pet("pet")

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet__when_pet_is_added(self):
        name = "dog"

        self.assertEqual(f"Successfully added {name}.", self.pet.add_pet(name))
        self.assertEqual(1, len(self.pet.pets))

    def test_feed_pet__when_name_is_invalid__expect_raise(self):
        name = "pet"
        self.pet.add_pet(name)
        self.pet.add_food("Food", 100)

        with self.assertRaises(Exception) as ex:
            self.pet.feed_pet("Food", "Doggy")

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet__when_food_name_is_invalid__expect_raise(self):
        name = "pet"
        invalid_food = "Dogfood"

        self.pet.add_pet(name)
        self.pet.add_food("Food", 100)

        self.assertEqual(f'You do not have {invalid_food}', self.pet.feed_pet(invalid_food, name))

    def test_feed_pet__when_food_quantity_is_below_100(self):
        name = "pet"
        food_name = "Food"
        self.pet.add_pet(name)
        self.pet.add_food(food_name, 20)

        self.assertEqual({food_name: 20}, self.pet.food)
        self.assertEqual("Adding food...", self.pet.feed_pet(food_name, name))
        self.assertEqual({food_name: 1020}, self.pet.food)

    def test_feed_pet__when_feed_pet(self):
        quantity = 1000
        name = "pet"
        food_name = "Food"
        self.pet.add_pet(name)
        self.pet.add_food(food_name, quantity)

        self.assertEqual({food_name: quantity}, self.pet.food)
        self.assertEqual(f"{name} was successfully fed", self.pet.feed_pet(food_name, name))
        self.assertEqual(900, self.pet.food[food_name])

    def test_repr(self):
        self.assertEqual(f"""Shop {self.pet.name}:
Pets: {", ".join(self.pet.pets)}""", self.pet.__repr__())


if __name__ == "__main__":
    main()