import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"✅ Contact {name} added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\n📒 Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} | {contact['phone']} | {contact['email']}")

# Search contact by name
def search_contact(contacts):
    keyword = input("Enter name to search: ").strip().lower()
    results = [c for c in contacts if keyword in c['name'].lower()]

    if results:
        print("\n🔍 Search Results:")
        for contact in results:
            print(f"{contact['name']} | {contact['phone']} | {contact['email']}")
    else:
        print("No matching contact found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip().lower()
    new_contacts = [c for c in contacts if c['name'].lower() != name]

    if len(new_contacts) != len(contacts):
        save_contacts(new_contacts)
        print(f"🗑️ Contact '{name}' deleted successfully!")
        return new_contacts
    else:
        print("Contact not found.")
        return contacts

# Update a contact
def update_contact(contacts):
    name = input("Enter name to update: ").strip().lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave blank if you don’t want to change:")
            new_phone = input(f"New Phone ({contact['phone']}): ").strip()
            new_email = input(f"New Email ({contact['email']}): ").strip()

            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email

            save_contacts(contacts)
            print("✏️ Contact updated successfully!")
            return
    print("Contact not found.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n===== Contact Book CLI =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            contacts = delete_contact(contacts)
        elif choice == "6":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
