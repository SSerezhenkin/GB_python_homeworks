from phoneBook import PhoneBook

commands = {'1': 'Открыть книгу',
            '2': 'Сохранить книгу',
            '3': 'Посмотреть все контакты',
            '4': 'Создать контакт',
            '5': 'Найти контакт',
            '6': 'Изменить контакт',
            '7': 'Удалить контакт',
            '8': 'Выход'}


def print_commands():
    print('Введите команду для работы с телефонной книгой:')
    for i in commands:
        print(i + '. ' + commands[i])


main_flag = True
book_temp = None
book_final = None

while main_flag:
    print('\n')
    print_commands()
    command = input('Команда: ')
    if command == '8':  # Выход
        if book_final != book_temp:
            while True:
                ans = input('Сохранить изменения (да/нет): ')
                if ans == 'да':
                    book_final.save_to_file('book.txt')
                    break
                elif ans == 'нет':
                    break
                else:
                    print('Не понял ответ, повторите.')
        print('Выключаюсь...')
        main_flag = False
    elif command == '1':  # Открытие
        book_temp = PhoneBook()
        try:
            book_temp.load_from_file('book.txt')
            print('Начинаем работу с файлом')
            book_final = PhoneBook()
            book_final.contacts = book_temp.contacts.copy()
        except Exception as e:
            print(e)
            print('Файл не найден')
            main_flag = False
    elif command == '2':  # Сохранение
        if book_final == book_temp:
            print('Не было никаких изменений')
            main_flag = False
        else:
            book_temp.contacts = book_final.contacts.copy()
            book_final.save_to_file('book.txt')
            print('Файл сохранён')
    elif command == '3':  # Просмотр всех
        try:
            book_final.show_all_contacts()
        except Exception:
            print('Сначала откройте книгу')
    elif command == '4':  # Создание
        name = input('Введите имя контакта: ')
        phone = input('Введите телефон контакта: ')
        comment = input('Введите комментарий: ')
        try:
            book_final.add_contact(name, phone, comment)
        except Exception:
            print('Сначала откройте книгу')
    elif command == '5':  # Найти контакт
        try:
            print('Поиск по:\n1. Имя\n2. Телефон\n3. Комментарий')
            ans = input('Как ищем (цифру): ')
            if ans == '1':
                value = input('Поиск по имени: ')
                book_final.find_contact(value, 'name')
            elif ans == '2':
                value = input('Поиск по телефону: ')
            elif ans == '3':
                value = input('Поиск по комментарию: ')
            else:
                print('Ошибка поиска')
        except Exception:
            print('Сначала откройте книгу')
    elif command == '6':  # Изменить контакт
        name = input('Введите имя изменяемого контакта: ')
        print('Под замену:\n1. Имя\n2. Телефон\n3. Комментарий')
        ans = input('Что меняем (можно несколько через запятую): ')
        new_name = None
        new_phone = None
        new_comment = None
        try:
            if '1' in ans:
                new_name = input('Введите новое имя: ')
            if '2' in ans:
                new_phone = input('Введите новый телефон: ')
            if '3' in ans:
                new_comment = input('Введите новый комментарий: ')
            book_final.edit_contact(name, new_name, new_phone, new_comment)
        except Exception:
            print('Сначала откройте книгу')
    elif command == '7': # Удалить контакт
        name = input('Введите имя контакта: ')
        try:
            book_final.delete_contact(name)
        except Exception: 
            print('Сначала откройте книгу')