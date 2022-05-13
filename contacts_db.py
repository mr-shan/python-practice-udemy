import sqlite3
from helpers import get_integer


def initialize_contacts_db():
    db = sqlite3.connect("contacts.sqlite")
    db.execute(
        "CREATE TABLE IF NOT EXISTS contacts (name TEXT NOT NULL, phone INTEGER PRIMARY KEY NOT NULL)"
    )
    return db


def start_program(db: sqlite3.Connection):
    while True:
        print("1. View all contacts")
        print("2. Create a new contact")
        print("3. Search for a contact")
        print("0. Exit the program\n")
        choice = get_integer("Please select an operation: ")
        print()
        if choice == 0:
            return
        elif choice == 1:
            show_all_contacts(db)
        elif choice == 2:
            create_new_contact(db)
        elif choice == 3:
            search_for_contact(db)


def show_all_contacts(db: sqlite3.Connection):
    print("********** SHOW ALL CONTACTS **********")
    cursor = db.execute("SELECT * FROM contacts")
    all_contacts = cursor.fetchall()
    print('Contact Name', 'Contact Number')
    for name, number in all_contacts:
        print(name, '\t', number)
    print()
    cursor.close()


def create_new_contact(db: sqlite3.Connection):
    print("********** CREATE NEW CONTACT **********")
    name = input("Enter contact name: ")
    number = get_integer("Enter the contact number: ")
    try:
        db.execute("INSERT INTO contacts VALUES (?, ?)", (name, number))
    except sqlite3.Error:
        print("Failed to create new contact")
        db.rollback()
    else:
        print("Added new contact successfully.\n")
        db.commit()
        
        
def search_for_contact(db: sqlite3.Connection):
    search = input("Please enter the search string: ")
    if len(search) == 0:
        print("Please enter valid string: ")
        return
    else:
        try:
            cursor = db.execute("SELECT * FROM contacts WHERE name LIKE ?", (f"%{search}%",))
            all_contacts = cursor.fetchall()
            print("Found {} contacts with matching {}".format(len(all_contacts), search))
            for name, number in all_contacts:
                print(name, '\t', number)
            cursor.close()
        except sqlite3.Error:
            print("Failed to search contacts")
    print()
    

if __name__ == "__main__":
    try:
        db = initialize_contacts_db()
        start_program(db)
    except sqlite3.Error:
        print("Sqlite 3 error occurred")
    finally:
        db.close()
