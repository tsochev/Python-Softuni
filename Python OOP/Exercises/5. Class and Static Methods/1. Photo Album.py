from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__build_photos()

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for row_index, row in enumerate(self.photos):
            if len(row) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[row_index].append(label)
                return f"{label} photo added successfully on page {row_index + 1} slot {len(self.photos[row_index])}"
        return "No more free slots"

    def display(self):
        separation = "-" * 11
        result = separation + "\n"
        for row in self.photos:
            result += ' '.join(["[]" for _ in row]) + "\n"
            result += separation + "\n"

        return result.strip()

    def __build_photos(self):
        result = []
        for x in range(self.pages):
            result.append([])

        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())

