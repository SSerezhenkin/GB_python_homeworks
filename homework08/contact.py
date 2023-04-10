class Contact:
    def __init__(self, name, phone, comment):
        self.name = name
        self.phone = phone
        self.comment = comment

    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False
        return self.name == other.name and self.phone == other.phone and self.comment == other.comment