from helpers import *
from func_command import *
from contacts_class import *


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) >= 2:
                print(add_contact(args, book))
            else:
                print("Usage: add <name> <phone>")    
        elif command == "change":
            if len(args) >= 3:
                print(change_contact(args, book))
            else:
                print("Usage: change <name> <old_phone> <new_phone>")
        elif command == "phone":
            if len(args) >= 1:
                print(show_contact(args, book))
            else:
                print("Usage: phone <name>")
        elif command == "all":
            print(show_all_contact(book))   
        elif command == "delete":
            if len(args) >= 1:
                print(delete_contact(args, book))
            else:
                print("Usage: delete <name>") 
        elif command == "add-birthday":
            if len(args) >= 2:
                print(add_birthday(args, book))
            else:
                print("Usage: add-birthday <name> <birthday (DD.MM.YYYY)>")
        elif command == "show-birthday":
            if len(args) >= 1:
                print(show_birthday(args, book))
            else:
                print("Usage: show-birthday <name>")
        elif command == "birthdays":
            print(birthdays(args, book))        
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()