from decorators import input_error


@input_error
def add_contact(args, book):
    if len(args) < 2:
        raise ValueError("Expected at least 2 arguments: name and phone.")
    name, phone, *_ = args
    record = book.find_record(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    if len(args) != 3:
        raise ValueError("Expected 3 arguments: name, old phone and new phone.")
    name, old_phone, new_phone = args
    record = book.find_record(name)
    if record is None: 
        return f"No contact found with name {name}."
    return record.edit_phone(old_phone, new_phone)
    
    
@input_error
def show_contact(args, book):
    if len(args) != 1:
        raise ValueError("Expected 1 argument: name.")
    name = args[0]
    record = book.find_record(name)
    if isinstance(record, str):
        return record
    return str(record)
 

@input_error
def show_all_contact(book):
    if not book:  
        return "No contacts saved." 
      
    result = "\n".join(
        f"{name}: {', '.join(phone.value for phone in record.phones)}"
        for name, record in book.items()
    )
    
    return result


@input_error
def delete_contact(args, book):
    if len(args) != 2:
        raise ValueError("Expected 2 arguments: name and phone.")
    name, phone = args
    record = book.find_record(name)
    if isinstance(record, str):
        return record
    return record.remove_phone(phone)
    
    
@input_error
def add_birthday(args, book):
    if len(args) != 2:
        raise ValueError("Usage: add-birthday <name> <birthday (DD.MM.YYYY)>")
    name, birthday = args
    record = book.find_record(name)
    if isinstance(record, str):  
        return record
    return record.add_birthday(birthday)


@input_error
def show_birthday(args, book):
    if len(args) != 1:
        raise ValueError("Usage: show-birthday <name>")
    name = args[0]
    record = book.find_record(name)
    if isinstance(record, str):  
        return record
    if record.birthday:
        return f"Birthday of {name}: {record.birthday.value.strftime('%d.%m.%Y')}"
    else:
        return f"{name} does not have a birthday set."


@input_error
def birthdays(args, book):
    if len(args) > 1:
        raise ValueError("Usage: birthdays [<days>]")
    days = int(args[0]) if args else 7  
    upcoming = book.get_upcoming_birthdays(days)
    if not upcoming:
        return "No upcoming birthdays."
    result = "\n".join(
        f"{record.name.value}: {record.birthday.value.strftime('%d.%m.%Y')} ({record.days_to_birthday()} days left)"
        for record in upcoming
    )
    return f"Upcoming birthdays:\n{result}"
    
    
