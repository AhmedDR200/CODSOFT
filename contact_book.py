contacts = []

def add_contact(name, phone, email, address):
    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['Name']} - {contact['Phone']}")

def search_contact(query):
    results = []
    for contact in contacts:
        if query.lower() in contact['Name'].lower() or query in contact['Phone']:
            results.append(contact)
    if not results:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for idx, contact in enumerate(results, start=1):
            print(f"{idx}. {contact['Name']} - {contact['Phone']}")

def update_contact(index, name, phone, email, address):
    if 0 <= index < len(contacts):
        contacts[index]['Name'] = name
        contacts[index]['Phone'] = phone
        contacts[index]['Email'] = email
        contacts[index]['Address'] = address
        print("Contact updated successfully!")
    else:
        print("Invalid contact index.")

def delete_contact(index):
    if 0 <= index < len(contacts):
        del contacts[index]
        print("Contact deleted successfully!")
    else:
        print("Invalid contact index.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            add_contact(name, phone, email, address)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            query = input("Enter Name or Phone to search: ")
            search_contact(query)
        elif choice == "4":
            index = int(input("Enter Contact Index to update: ")) - 1
            name = input("Enter New Name: ")
            phone = input("Enter New Phone: ")
            email = input("Enter New Email: ")
            address = input("Enter New Address: ")
            update_contact(index, name, phone, email, address)
        elif choice == "5":
            index = int(input("Enter Contact Index to delete: ")) - 1
            delete_contact(index)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
