from decorators import input_error

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Expected 2 arguments: name and phone.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Expected 2 arguments: name and new phone.")
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated."
    else:
        raise KeyError(f"{name} not found.")

@input_error
def show_contact(args, contacts):
    if len(args) != 1:
        raise ValueError("Expected 1 argument: name.")
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        raise KeyError(f"{name} not found.")

@input_error
def show_all_contact(contacts):
    if not contacts:
        return "No contacts saved."
    else:
        result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
        return result

@input_error
def delete_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Expected 2 arguments: name and phone.")
    name, phone = args
    if name in contacts and contacts[name] == phone:
        del contacts[name]
        return "Contact deleted."
    else:
        raise KeyError(f"{name} not found.")
    
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
    
    
