from unittest import TestCase, main

from project.library import Library


class LibraryTests(TestCase):
    def setUp(self):
        self.library = Library("Test")

    def test_init__expect_result(self):
        self.library = Library("Test")

        self.assertEqual("Test", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_init__when_name_is_empty_string__expect_raise(self):
        with self.assertRaises(ValueError) as ct:
            self.library = Library("")

        self.assertEqual("Name cannot be empty string!", str(ct.exception))

    def test_add_book__when_author_and_title(self):
        self.library.add_book("Test", "Bigtest")
        self.assertEqual({'Test': ['Bigtest']}, self.library.books_by_authors)

    def test_add_reader__expect_result(self):
        reader = "reader"
        self.library.add_reader(reader)
        self.assertEqual({reader: []}, self.library.readers)

    def test_add_reader__when_name_exist__expect_raise(self):
        reader = "reader"
        self.library.add_reader(reader)
        self.assertEqual(f"{reader} is already registered in the {self.library.name} library.",
                         self.library.add_reader(reader))

    def test_rent_book__when_reader_name_is_not_registered__expect_raise(self):
        reader = "reader"
        result = self.library.rent_book("reader", "Author", "Title")
        self.assertEqual(f"{reader} is not registered in the {self.library.name} Library.", result)

    def test_rent_book__when_book_author_is_not_registered__expect_raise(self):
        reader = "Reader"
        author_name = "author"
        self.library.add_reader(reader)

        result = self.library.rent_book(reader, author_name, "bigtest")
        self.assertEqual(f"{self.library.name} Library does not have any {author_name}'s books.", result)

    def test_rent_book__when_book_title_is_not_registered__expect_raise(self):
        reader = "reader"
        author = "author"
        invalid_title = "title"
        self.library.add_reader(reader)
        self.library.add_book(author, "random title")

        result = self.library.rent_book(reader, author, invalid_title)
        self.assertEqual(f"""{self.library.name} Library does not have {author}'s "{invalid_title}".""", result)

    def test_rent_book__expect_result(self):
        reader = "reader"
        author = "author"
        first_title = "title1"
        second_title = "title2"
        self.library.add_reader(reader)
        self.library.add_book(author, first_title)
        self.library.add_book(author, second_title)

        self.library.rent_book(reader, author, first_title)

        self.assertEqual([{author: first_title}], self.library.readers[reader])
        self.assertEqual(1, len(self.library.books_by_authors[author]))
        self.assertTrue(first_title not in self.library.books_by_authors[author])
        self.assertTrue(second_title in self.library.books_by_authors[author])


if __name__ == "__main__":
    main()
