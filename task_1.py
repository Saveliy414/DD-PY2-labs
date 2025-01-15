BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id: int, name: str, pages: int) -> None:
        if not isinstance(id, int):
            raise TypeError("Идентификатор книги должен иметь тип int")

        if not isinstance(name, str):
            raise TypeError("Название книги должно иметь тип string")
        if name == "":
            raise ValueError("Название книги не может быть пустым")

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно иметь тип int")
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)
    print(list_books)
