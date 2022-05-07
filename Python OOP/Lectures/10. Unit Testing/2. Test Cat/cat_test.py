from unittest import TestCase, main

from cat import Cat


class CatTests(TestCase):
    name = "Kitty"

    def setUp(self):
        self.cat = Cat(self.name)

    def test_eat__expect_size_to_be_increased_by_1(self):
        self.cat.eat()

        self.assertEqual(1, self.cat.size)

    def test_eat__expect_fed_to_be_true(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test_eat__when_cannot_eat_if_is_fed__expect_raise_exception(self):
        self.cat.eat()

        with self.assertRaises(Exception) as context:
            self.cat.eat()

        self.assertEqual("Already fed.", str(context.exception))

    def test_sleep__when_cannot_sleep_if_is_not_fed__expect_raise(self):
        self.assertFalse(self.cat.fed)

        with self.assertRaises(Exception) as context:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(context.exception))

    def test_sleep__when_cannot_sleep_after_sleeping__expect_to_be_false(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
