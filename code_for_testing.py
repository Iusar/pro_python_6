# Каталог документов:
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
# Перечень полок:
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

commands_catalogue = [
    {"command_key": "p", "func_name": "find_client_name", "title": "Поиск имени человека по номеру документа"},
    {"command_key": "s", "func_name": "find_shelf_no", "title": "Поиск номера полки по номеру документа"},
    {"command_key": "l", "func_name": "print_all_docs", "title": "Вывести список всех документов"},
    {"command_key": "a", "func_name": "add_new_doc", "title": "Добавить новый документ в каталог"},
    {"command_key": "d", "func_name": "delete_doc", "title": "Удалить документ"},
    {"command_key": "m", "func_name": "move_doc_to_shelf", "title": "Переместить документ с текущей полки на целевую"},
    {"command_key": "as", "func_name": "add_new_shelf", "title": "Добавить новую полку"},
]


# Вводим функции программы. Старт программы после функций
# Поиск имени человека по номеру документа
def find_client_name(documents, document_no):
    # document_no = input("Введите номер документа: ")
    for document in documents:
        if document_no in document.values():
            print(f'Имя владельца документа {document.get("name")}')
            return (document.get("name"))


# Поиск номера полки по номеру документа (туповато но работает)
def find_shelf_no(directories, document_no):
    # document_no = input("Введите номер документа: ")
    document_check = False
    for shelf_no, doc_on_shelf in directories.items():
        if document_no in doc_on_shelf:
            document_check = True
            print(shelf_no)
            return shelf_no
    if document_check == False:
        print('Документа с таким номером не существует')


# Вывести список всех документов
def print_all_docs(documents):
    for document in documents:
        # print(document.get("type"), end=' ')
        # print('"', document.get("number"), '"', end=' ')
        # print('"', document.get("name"), '"')
        return documents


# Добавить новый документ в каталог
def add_new_doc(documents, directories, type, number, name, shelf_no):
    # type = input("Введите тип документа: ")
    # number = input("Введите номер документа: ")
    # name = input("Введите имя: ")
    # shelf_no = input("Введите номер полки: ")
    if shelf_no in directories:

        directories[shelf_no].append(number)
        documents.append({"type": type, "number": number, "name": name})

    else:
        print('Хм... похоже такой полки не существует')
    return documents, directories


def delete_doc(documents, directories, document_no):
    # document_no = input("Введите номер документа: ")
    for record in documents:
        if document_no in record.values():
            record.clear()
    for place in directories.values():
        if document_no in place:
            place.remove(document_no)
    return documents, directories


# def move_doc_to_shelf():
#     new_shelf = input("Введите номер документа")
#     directories[max(int(directories.keys())) + 1] = new_shelf


def add_new_shelf(directories):
    shelf_no = input("Введите номер полки: ")
    if shelf_no in directories:
        print('Хм... похоже такая полка существует')
    else:
        directories[shelf_no] = []


# Старт программы
if __name__ == '__main__':
    # Выводим список доступных комманд
    print('Выберите команду:')
    for every_type in commands_catalogue:
        print(f'Введите "{every_type.get("command_key")}" для выбора команды "{every_type.get("title")}" ')
    # print('Введите "q" для выхода')
    # Запрашиваем и фиксируем выбранную команду
    chosen_command = input('Выберите команду: ')

    # Информируем пользователя о выбранной команде, фиксируем назмание функции
    for every_command in commands_catalogue:
        if chosen_command in every_command.values():
            print(f'Выбрана команда "{every_command.get("title")}" ')

    if chosen_command == "p":
        find_client_name()
    elif chosen_command == "s":
        find_shelf_no(directories)
    elif chosen_command == "l":
        print_all_docs(documents)
    elif chosen_command == "a":
        add_new_doc(documents, directories)
        # Проверка что получилось
        print(documents)
        print(directories)
    elif chosen_command == "d":
        delete_doc(documents, directories)
        # Проверка что получилось
        print(documents)
        print(directories)
    elif chosen_command == "as":
        add_new_shelf(directories)
        # Проверка что получилось
        print(documents)
        print(directories)
