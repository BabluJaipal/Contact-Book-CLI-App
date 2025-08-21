# Contact-Book-CLI-App
A simple Command-Line Interface (CLI) based Contact Book application written in Python. It allows you to Add, View, Search, Update, and Delete contact details and saves them in a JSON file for persistence.

🚀 Features

Add a new contact (Name, Phone, Email)

View all saved contacts

Search contacts by name

Update existing contact details

Delete a contact

Persistent storage using JSON file

🛠️ Tech Stack

Language: Python 3.x

IDE/Editor: VS Code (or any Python IDE)

Storage: JSON file (contacts.json)

📂 Project Structure
ContactBook/
│-- contact_book.py   # Main program file
│-- contacts.json     # Auto-generated file to store contacts
│-- README.md         # Documentation

📥 Installation & Setup

Clone or Download the Project

Or just create a folder manually and add contact_book.py.

Install Python

Make sure Python 3.x is installed.

Check version:

python --version


or

python3 --version


Run the Program

python contact_book.py


or (Linux/Mac users):

python3 contact_book.py

🎮 Usage (Menu Options)

When you run the program, you’ll see a menu like this:

===== Contact Book CLI =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Example:

Choose 1 → Enter name, phone, email → Contact saved.

Choose 2 → View all saved contacts.

Choose 3 → Search by name (partial match supported).

Choose 4 → Update phone/email of an existing contact.

Choose 5 → Delete a contact by name.

Choose 6 → Exit safely.

🗂️ Data Storage

All contacts are stored in contacts.json (auto-created).

Example of stored data:

[
    {
        "name": "Alice",
        "phone": "9876543210",
        "email": "alice@example.com"
    },
    {
        "name": "Bob",
        "phone": "1234567890",
        "email": "bob@example.com"
    }
]

📌 Learning Outcomes

Hands-on practice with:

CRUD operations

Python data structures (lists, dictionaries)

File handling with JSON

CLI interaction with input()

🔮 Future Improvements

Add contact groups (Family, Friends, Work)

Export contacts to CSV/Excel

Add password protection

Build a GUI version (using Tkinter or PyQt)
