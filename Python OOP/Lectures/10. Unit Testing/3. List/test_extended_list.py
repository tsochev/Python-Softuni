from unittest import TestCase, main

from extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.list_integers = IntegerList(5, 6, 7)

    def test_init__when_expect_correct_result(self):
        self.assertEqual([5, 6, 7], self.list_integers._IntegerList__data)

    def test_init__when_takes_non_integer(self):
        list_integers = IntegerList(5.6, "6", 7.2)
        self.assertEqual([], list_integers._IntegerList__data)

    def test_add__when_integer_is_added__expect_to_return_list(self):
        result = self.list_integers.add(100)
        self.assertEqual([5, 6, 7, 100], result)

    def test_add__when__takes_non_integer_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.list_integers.add(6.3)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_index_when_remove_element_on_that_index__expect_to_return_it(self):
        el = self.list_integers.remove_index(0)
        self.assertEqual(5, el)
        self.assertEqual([6, 7], self.list_integers._IntegerList__data)

    def test_remove_index_when_index_is_out_of_range_expect_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.remove_index(5)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get__when_valid_index__expect_return_specific_element(self):
        el = self.list_integers.get(0)
        self.assertEqual(5, el)
        self.assertEqual([5, 6, 7], self.list_integers._IntegerList__data)

    def test_get__when_invalid_index__expect_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.get(5)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert__when_expect_correct_result(self):
        self.list_integers.insert(0, 4)

        self.assertEqual([4, 5, 6, 7], self.list_integers._IntegerList__data)

    def test_insert__when_invalid_index__expect_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.insert(3, 8)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert__when__element_is_not_integer__expect_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integers.insert(0, 4.4)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest__when_expect_correct_result(self):
        result = self.list_integers.get_biggest()
        self.assertEqual(7, result)

    def test_get_index__when_expect_correct_result(self):
        result = self.list_integers.get_index(5)
        self.assertEqual(0, result)


if __name__ == '__main__':
    main()
