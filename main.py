class Book:
    def __init__(self, id_, name, pages):
        """
               Создание и подготовка к работе объекта "Книга"
               Аргументы:
               :param id_:  идентификатор книги
               :param name: название книги
               :param pages: количество страниц в книге
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
               Метод возвращает название книги
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
                Метод возвращает  валидную python строку,
                по которой можно инициализировать точно такой же экземпляр
        """
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books=None):
        """
                Создание и подготовка к работе объекта "Библиотека"
                Аргументы:
                :param books: книги
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
               Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
               Если книг в библиотеке нет, то вернет 1.
               Если книги есть, то вернет идентификатор последней книги увеличенный на 1.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        """
                Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
                Если книга существует, то вернет индекс из списка.
                Если книги нет, то вызвет ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует"
        """
        for i, book in enumerate(self.books):
            if book.id == book_id:
                return i
        raise ValueError(f"Книга с запрашиваемым id {book_id} не существует")
