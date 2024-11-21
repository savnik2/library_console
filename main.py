from library import Library
from actions import *


def main():
    library = Library('data.json')

    actions = {
        '1': add_book_action,
        '2': remove_book_action,
        '3': find_books_action,
        '4': display_books_action,
        '5': change_status_action,
    }

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == '6':
            break
        elif choice in actions:
            actions[choice](library)
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 6.")


if __name__ == "__main__":
    main()
