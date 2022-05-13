from unittest import TestCase, main

from car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car(fuel_capacity=100, fuel_consumption=5.6, make="Test", model="Opel")

    def test_init_expect_correct_result(self):
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(0, self.car.fuel_amount)
        self.assertEqual("Test", self.car.make)
        self.assertEqual("Opel", self.car.model)

    def test_fuel_capacity__when_is_negative__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_set_fuel_capacity(self):
        res = self.car.fuel_capacity = 100
        self.assertEqual(100, res)

    def test_model__when_name_is_empty__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model__when_expect_correct_result(self):
        self.car.model = "Opel"
        self.assertEqual("Opel", self.car.model)

    def test_make__when_name_is_empty__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make__when_expect_correct_result(self):
        self.car.make = "Test"
        self.assertEqual("Test", self.car.make)

    def test_fuel_consumption__when_is_negative__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_set_fuel_consumption(self):
        self.car.fuel_consumption = 20
        self.assertEqual(20, self.car.fuel_consumption)

    def test_refuel__when_add_fuel__expect_correct_result(self):
        self.car.refuel(20)
        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel__when_add_negative_fuel__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-20)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive__when_drive_without_fuel__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive__when_expect_correct_result(self):
        self.car.refuel(100)
        self.assertEqual(100, self.car.fuel_amount)

        self.car.drive(10)
        self.assertEqual(99.44, self.car.fuel_amount)

    def test_drive__when_not_enough_fuel__expect_exception(self):
        self.car.refuel(5)
        self.assertEqual(5, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()
