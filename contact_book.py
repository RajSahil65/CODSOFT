# contact_book.py


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {"phone_number": phone_number, "email": email, "address": address}

    def view_contacts(self):
        for name, contact in self.contacts.items():
            print(f"Name: {name}, Phone Number: {contact['phone_number']}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact found: {name}, Phone Number: {self.contacts[name]['phone_number']}")
        else:
            print("Contact not found")

    def update_contact(self, name, phone_number, email, address):
        if name in self.contacts:
            self.contacts[name] = {"phone_number": phone_number, "email": email, "address": address}
        else:
            print("Contact not found")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found")

def main():
    contact_book = ContactBook()

    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == "4":
            name = input("Enter name to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_book.update_contact(name, phone_number, email, address)
        elif choice == "5":
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()