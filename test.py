from contacts_class import AddressBook, Record
from func_command import *

book = AddressBook()


user1 = Record("John Doe")
user1.add_phone("4878808379")
user1.add_birthday("15.12.1990")
book.add_record(user1)


user2 = Record("Jane Smith")
user2.add_phone("0987654321")
user2.add_birthday("20.12.1985")
book.add_record(user2)


user3 = Record("Alice Brown")
user3.add_phone("1122334455")
book.add_record(user3)


print("All contacts:")
print(book)


print("\nUpcoming birthdays in the next 7 days:")
for contact in book.get_upcoming_birthdays():
    print(contact)



