phone_book = {}
PATH = 'phones_list.txt'


def open_file(book: dict):
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(';')
        book[i] = contact


def save_file(book: dict):
    all_contact = []
    for contact in book.values():
        all_contact.append(';'.join(contact))
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(all_contact))


def show_contacts(book: dict, message: str):
    print('\n' + '=/' * 30)
    if book:
        for i, contact in book.items():
            print(f'{i:>3}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')
    else:
        print(message)
    print('=/' * 30 + '\n')


def add_new_contact(book: dict, new_val: list):
    cur_id = max(book.keys()) + 1
    book[cur_id] = new_val


def find_contact(book: dict, search: str):
    result = {}
    for i, contact in book.items():
        for field in contact:
            if search.lower() in field.lower():
                result[i] = contact
                break
    return result


def func_search(book: dict):
    searсh = input('Введите параметр для поиска: ')
    result = find_contact(book, searсh)
    show_contacts(result, f'Контакт содержащий {searсh} не найден!')


def change_contact(book: dict, cid: int):
    name, phone, comment = book.get(cid)
    changed = []
    for item in ['Введите новое имя: ',
                 'Введите новый телефон: ',
                 'Добавьте новый комментарий: ']:
        changed.append(input(item))
    book[cid] = [changed[0] if changed[0] else name,
                 changed[1] if changed[1] else phone,
                 changed[2] if changed[2] else comment]
    return changed[0] if changed[0] else name


def delete_contact(book: dict, cid: int):
    name = book.pop(cid)
    return name[0]


def menu():
    menu_points = ['Открыть файл',
                   'Сохранить файл',
                   'Посмотреть все контакты',
                   'Добавить контакт',
                   'Найти контакт',
                   'Изменить контакт',
                   'Удалить контакт',
                   'Выход']
    print('Главное меню:')
    [print(f'\t{i}. {item}') for i, item in enumerate(menu_points, 1)]
    choise = int(input('Выберите пункт меню: '))
    return choise


while True:
    choice = menu()
    match choice:
        case 1:
            open_file(phone_book)
            print('\nТелефонная книга успешно открыта!\n')
        case 2:
            save_file(phone_book)
            print('\nТелефонная книга успешно сохранена!\n')
        case 3:
            show_contacts(phone_book, 'Телефонная книга пуста или не открыта!')
        case 4:
            new = []
            for item in ['Введите имя: ', 'Введите телефон: ', 'Добавьте комментарий: ']:
                new.append(input(item))
            add_new_contact(phone_book, new)
            print(f'\nКонтакт {new[0]} успешно добавлен!\n')
        case 5:
            func_search(phone_book)
        case 6:
            func_search(phone_book)
            select = int(input('Какой контакт изменить: '))
            name = change_contact(phone_book, select)
            print(f'\nКонтакт {name} успешно изменён!\n')
        case 7:
            func_search(phone_book)
            select = int(input('Какой контакт удалить: '))
            name = delete_contact(phone_book, select)
            print(f'\nКонтакт {name} успешно удалён!\n')
        case 8:
            print('\nВсего хорошего!')
            break
