from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.value = name

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError("A phone number must be 10 digits long")
        if not value.isdigit():
            raise ValueError("The phone number must contain only digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phones(phone))
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None    
    
    def edit_phone(self, old_phone, new_phone):
        for idx, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[idx] = Phone(new_phone)
                return f"Phone {old_phone} changed to {new_phone}."        
        return f"Phone {old_phone} not found."
         
    def remove_phone(self, phone):
        for idx, p in enumerate(self.phones):
            if p.value == phone:
                del self.phones[idx]
                return f"Phone {phone} removed."
            return f"Phone {phone} not found."    
                         

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def add_records(self, record):
        self.data[record.name.value] = record
        return f"Record for {record.name.value} added."
    
    def find_record(self, name):
        return self.data.get(name, f"No record found for {name}.")
    
    def remove_record(self, name):
        if name in self.data:
            del self.data[name]
            return f"Record for {name} removed."
        return f"Record for {name} not found."
    
    def __str__(self):
        return "\n".join(
            f"Contact name: {record.name.value}, phones: {'; '.join(phone.value for phone in record.phones)}"
            for record in self.data.values()
        )
