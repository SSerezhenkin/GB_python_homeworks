from contact import Contact


class PhoneBook:
    def __init__(self):
        self.contacts = []

    # Переопределяем метод сравнения
    def __eq__(self, other):
        if isinstance(other, PhoneBook):
            if len(self.contacts) != len(other.contacts):
                return False
            for contact1, contact2 in zip(self.contacts, other.contacts):
                if (contact1.name != contact2.name or
                    contact1.phone != contact2.phone or
                    contact1.comment != contact2.comment):
                    return False
            return True
        return NotImplemented

    # Прочитать из файла
    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                values = line.split(';')
                if len(values) != 3:
                    continue
                name, phone, comment = values
                self.contacts.append(Contact(name, phone, comment))

    # Сохранить в файл
    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for contact in self.contacts:
                f.write(f'{contact.name};{contact.phone};{contact.comment}\n')

    # Посмотреть все контакты
    def show_all_contacts(self):
        print('\nСписок всех контактов:')
        for contact in self.contacts:
            print(contact.name, contact.phone, contact.comment)

    # Добавить контакт
    def add_contact(self, name, phone, comment):
        contact = Contact(name, phone, comment)
        self.contacts.append(contact)
        print("Контакт успешно добавлен")

    # Найти контакт
    def find_contact(self, value, field):
        for contact in self.contacts:
            if field == 'name' and contact.name == value:
                print(contact.name, contact.phone, contact.comment)
                return
            elif field == 'phone' and contact.phone == value:
                print(contact.name, contact.phone, contact.comment)
                return
            elif field == 'comment' and contact.comment == value:
                print(contact.name, contact.phone, contact.comment)
                return
        print("Контакт не найден")

    # Редактировать контакт
    def edit_contact(self, name, new_name=None, new_phone=None, new_comment=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_name is not None:
                    contact.name = new_name
                if new_phone is not None:
                    contact.phone = new_phone
                if new_comment is not None:
                    contact.comment = new_comment
                return
        print("Контакт не найден")

    # Удалить контакт
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Контакт успешно удален")
                return
        print("Контакт не найден")
