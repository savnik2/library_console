import json
from typing import List, Optional


class Book:
    """
        Класс, представляющий книгу в библиотеке.

        Атрибуты:
            id (Optional[int]): Уникальный идентификатор книги (опциональный).
            title (str): Название книги.
            author (str): Автор книги.
            year (str): Год выпуска книги.
            status (str): Статус книги (по умолчанию "в наличии").
            _search_data (str): Строка для поиска, содержащая название, автора и год в нижнем регистре.
        """

    def __init__(
            self,
            title: str,
            author: str,
            year: str,
            id: Optional[int] = None,
            status: str = "в наличии"
    ):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self._search_data = f"{title.lower()} {author.lower()} {year}"

    def search_query(self, query: str) -> bool:
        """
            Поиск книги по названию, автору или году выпуска
        """
        return query in self._search_data

    def to_dict(self) -> dict:
        """
            Преобразование объекта Book в словарь.

            :return: Словарь, представляющий объект Book.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        """
            Преобразование словаря в объект Book.

            :param data: Словарь, содержащий данные о книге.
            :return: Объект Book, созданный из словаря.
        """
        return cls(
            id=data.get("id"),
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"]
        )

    def __str__(self) -> str:
        """
            Возвращает строковое представление объекта Book.

            :return: Строка, содержащая информацию о книге.
        """
        return f"ID: {self.id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}"
