import json
from typing import List
from book import Book


class Library:
    """
        Класс, представляющий библиотеку книг.

        Атрибуты:
            filename (str): Имя файла, в котором хранятся данные о книгах.
            books (List[Book]): Список объектов Book, представляющих книги в библиотеке.
    """
    def __init__(self, filename: str):
        """
            Инициализация объекта Library.

            :param filename: Имя файла, в котором хранятся данные о книгах.
        """
        self.filename = filename
        self.books: List[Book] = self.load_books()

    def load_books(self) -> List[Book]:
        """
            Загрузка книг из JSON-файла.

            :return: Список объектов Book, представляющих книги в библиотеке.
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Book.from_dict(book_data) for book_data in data]
        except FileNotFoundError:
            return []

    def save_books(self):
        """
            Сохранение книг в JSON-файл
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """
            Добавление новой книги в библиотеку.

            :param title: Название книги.
            :param author: Автор книги.
            :param year: Год выпуска книги.
            :return: Строка с информацией о добавленной книге.
        """
        new_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(title=title, author=author, year=year, id=new_id)
        self.books.append(new_book)
        self.save_books()
        return f"Книга добавлена: {new_book}"

    def remove_book(self, book_id: int):
        """
            Удаление книги из библиотеки по её ID.

            :param book_id: ID книги, которую нужно удалить.
            :return: Строка с информацией об удалении книги.
        """
        try:
            deleted_book = self.books.pop(next(i for i, book in enumerate(self.books) if book.id == book_id))
            self.save_books()
            return f"Книга {deleted_book.title} удалена"
        except (StopIteration, ValueError):
            return f"Книга с ID {book_id} не найдена."

    def find_books(self, query: str) -> List[Book]:
        """
            Поиск книги в файле
            :param query: Название, автор или год выпуска
        """
        query = query.lower()
        return [book for book in self.books if book.search_query(query)]

    def display_books(self):
        """
            Вывод всех книг в консоль
        """
        return self.books

    def change_status(self, book_id: int, new_status: str):
        """

            :param book_id: ID книги для обновления
            :param new_status: новый статус (в наличии\ выдана)
            :return: Строка с информацией об обновлении книги.
        """
        access_status = [
            "в наличии",
            "выдана",
        ]
        if new_status not in access_status:
            return "Недопустимый статус"
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books()
                return f"Статус книги с ID {book_id} изменен на '{new_status}'."

        return f"Книга с ID {book_id} не найдена."


