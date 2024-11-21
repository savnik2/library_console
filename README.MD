# Система управления библиотекой

## Описание

Это консольное приложение для управления библиотекой книг. Приложение позволяет добавлять, удалять, искать и отображать книги. Каждая книга содержит следующие поля:

- id (уникальный идентификатор, генерируется автоматически)
- title (название книги)
- author (автор книги)
- year (год издания)
- status (статус книги: “в наличии”, “выдана”)

## Функционал

1. **Добавление книги:** Введите название, автора и год выпуска книги, после чего она добавится в библиотеку.
2. **Удаление книги:** Введите ID, которую нужно удалить.
3. **Поиск книги:** Введите название, автора или год выпуска книги
4. **Отображение всех книг:** Приложение выводит список всех книг с их ID, названием, автором, годом выпуска и статусом.
5. **Изменение статуса книги:** Введите ID книги и новый статус (“в наличии” или “выдана”).

## Запуск приложения

1. Убедитесь, что у вас установлен Python3.
2. Запустите приложение с помощью команды:

```bash
python main.py