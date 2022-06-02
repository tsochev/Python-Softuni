from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.pf = PaintFactory("Test", 100)

    def test_initialization(self):

        self.assertEqual("Test", self.pf.name)
        self.assertEqual(100, self.pf.capacity)
        self.assertEqual({}, self.pf.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.pf.valid_ingredients)

    def test_add_ingredient_invalid_product_type_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.pf.add_ingredient("purple", 5)

        self.assertEqual(f"Ingredient of type purple not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient_invalid_quantity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pf.add_ingredient("white", 110)

        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_when_add_ingredient(self):
        self.assertEqual({}, self.pf.ingredients)
        self.pf.add_ingredient("white", 10)
        self.assertEqual({"white": 10}, self.pf.ingredients)

    def test_add_ingredient_when_increase_quantity(self):
        self.assertEqual({}, self.pf.ingredients)
        self.pf.add_ingredient("white", 10)
        self.assertEqual({"white": 10}, self.pf.ingredients)
        self.pf.add_ingredient("white", 20)
        # self.assertEqual(30, self.pf.ingredients["white"])
        self.assertEqual({"white": 30}, self.pf.ingredients)

    def test_remove_ingredient_when_invalid_product_type_raise(self):
        with self.assertRaises(KeyError) as ex:
            self.pf.remove_ingredient("purple", 10)

        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_ingredient_when_quantity_is_below_zero_raise(self):
        self.pf.add_ingredient("white", 20)
        with self.assertRaises(ValueError) as ex:
            self.pf.remove_ingredient("white", 30)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_when_quantity_can_be_decreased(self):
        self.pf.add_ingredient("white", 50)
        self.pf.remove_ingredient("white", 20)

        self.assertEqual({"white": 30}, self.pf.ingredients)

    def test_products_property(self):
        self.pf.add_ingredient("white", 50)
        self.assertEqual({"white": 50}, self.pf.products)


if __name__ == "__main__":
    main()
