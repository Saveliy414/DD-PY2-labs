class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целочисленного типа")
        if pages <= 0:
            raise ValueError("Количество страниц не может быть меньше или равна нулю")
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{super().__repr__()}. Количество страниц {self.pages!r}"

    def get_pages(self):
        return self.pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность не может быть меньше или равна нулю")
        self.duration = duration

    def __str__(self):
        return f"{super().__str__()}. Продолжительность {self.duration} часов"

    def __repr__(self):
        return f"{super().__repr__()}. Продолжительность {self.duration!r} часов"

    def get_duration(self):
        return self.duration