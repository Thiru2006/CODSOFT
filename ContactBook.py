contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    keyword = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
    if not found:
        print("No contact found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave field blank to keep existing value.")
            new_name = input(f"Enter new name [{contact['name']}]: ") or contact['name']
            new_phone = input(f"Enter new phone [{contact['phone']}]: ") or contact['phone']
            new_email = input(f"Enter new email [{contact['email']}]: ") or contact['email']
            new_address = input(f"Enter new address [{contact['address']}]: ") or contact['address']
            
            contact.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name:
            confirm = input(f"Are you sure you want to delete {contact['name']}? (Y/N): ")
            if confirm.lower() == 'y':
                contacts.pop(i)
                print("Contact deleted successfully!\n")
                return
            else:
                print("Delete cancelled.\n")
                return
    print("Contact not found.\n")

def contact_book():
    while True:
        print("=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            update_contact()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

contact_book()
