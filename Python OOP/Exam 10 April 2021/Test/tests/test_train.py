from unittest import TestCase, main

from project.train.train import Train


class TrainTest(TestCase):
    def setUp(self):
        self.t = Train("Test", 3)

    def test_init__when_is_correct(self):
        self.assertEqual("Test", self.t.name)
        self.assertEqual(3, self.t.capacity)
        self.assertEqual([], self.t.passengers)

    def test_class_attributes__expect_result(self):
        self.assertEqual("Train is full", self.t.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.t.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.t.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.t.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.t.PASSENGER_REMOVED)
        self.assertEqual(0, self.t.ZERO_CAPACITY)

    def test_add__when_train_is_full__expect_raise(self):
        self.t.add("Gosho")
        self.t.add("Ivan")
        self.t.add("Elena")

        with self.assertRaises(ValueError) as ct:
            self.t.add("Pesho")

        self.assertEqual("Train is full", str(ct.exception))

    def test_add__when_name_exist_in_the_train__expect_raise(self):
        self.t.add("Gosho")
        self.t.add("Annie")
        self.assertEqual(["Gosho", "Annie"], self.t.passengers)

        with self.assertRaises(ValueError) as ct:
            self.t.add("Annie")

        self.assertEqual("Passenger Annie Exists", str(ct.exception))

    # def test_add__when_return_the_name(self):
    #     self.t.add("Annie")
    #     self.assertEqual("Added passenger Annie", self.t.)
    #     self.assertTrue(["Annie"])

    def test_remove__when_name_is_not_in_train__expect_raise(self):
        with self.assertRaises(ValueError) as ct:
            self.t.remove("Test2")

        self.assertEqual("Passenger Not Found", str(ct.exception))

    def test_remove__when_name_is_in_train__expect_result(self):
        self.t.add("Annie")
        # self.t.remove("Annie")
        self.assertEqual("Removed Annie", self.t.remove("Annie"))




if __name__ == "__main__":
    main()
