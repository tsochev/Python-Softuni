class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class UpperCaseFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content.upper()


class Printer:
    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        formatted_book = self.formatter.format(book)
        return formatted_book


uppercase_formatter = UpperCaseFormatter()
regular_formatter = Formatter()


b = Book("Hello world!")
regular_printer = Printer(regular_formatter)
uppercase_printer = Printer(uppercase_formatter)
print(regular_printer.get_book(b))
print(uppercase_printer.get_book(b))
