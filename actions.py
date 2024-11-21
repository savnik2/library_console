def safe_int_input(prompt: str) -> int:
    """
        Безопасный ввод целого числа с проверкой.
        :param prompt: Строка с приглашением для ввода.
        :return: Введенное целое число.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: введено некорректное значение. Пожалуйста, введите целое число.")


def add_book_action(library):
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год издания: ")
    result = library.add_book(title, author, year)
    print(result)


def remove_book_action(library):
    book_id = safe_int_input("Введите ID книги для удаления: ")
    result = library.remove_book(book_id)
    print(result)


def find_books_action(library):
    query = input("Введите запрос для поиска: ")
    found_books = library.find_books(query)
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("Книги не найдены.")


def display_books_action(library):
    for book in library.display_books():
        print(book)


def change_status_action(library):
    book_id = safe_int_input("Введите ID книги для изменения статуса: ")
    new_status = input("Введите новый статус (в наличии/выдана): ")
    result = library.change_status(book_id, new_status)
    print(result)
