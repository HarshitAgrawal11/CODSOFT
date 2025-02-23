#Task3 : Contact Book

#Function to add contact 
def add_contact(contact_list):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact_list.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
    print("Contact Added Successfully!")

#Function to view contact list
def view_contacts(contact_list):
    if not contact_list:
        print("No contacts available.")
    else:
        for contact in contact_list:
            print(f"Name: {contact['Name']}, \n Phone: {contact['Phone']}")

#Function to search a contact

def search_contact(contact_list, search_term):
    found = False
    for contact in contact_list:
        if search_term.lower() in contact["Name"].lower() or search_term in contact["Phone"]:
            print(f"Found: {contact['Name']} - {contact['Phone']}")
            found = True
    if not found:
        print("Contact not found.")

#Funtion to Update a contact

def update_contact(contact_list, name):
    for contact in contact_list:
        if contact["Name"].lower() == name.lower():
            print(f"Updating contact for {contact['Name']}:")
            contact["Phone"] = input("Enter new phone number: ")
            contact["Email"] = input("Enter new email: ")
            contact["Address"] = input("Enter new address: ")
            print("Contact Updated Successfully!")
            return
    print("Contact not found.")

#Funtion to Delete a contact

def delete_contact(contact_list, name):
    for contact in contact_list:
        if contact["Name"].lower() == name.lower():
            contact_list.remove(contact)
            print(f"{name} has been deleted.")
            return
    print("Contact not found.")

#Funtion for building a CUI Based User Interface

def show_menu():
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contacts = []
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_contact(contacts, search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            update_contact(contacts, name)
        elif choice == '5':
            name = input ("Enter the name of the contact to delete: ")
            delete_contact(contacts, name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose again.")
        c = int(input("Do you want to continue? (Enter 1 for yes or any other number for no : "))
        if c != 1 :
           print ("Exiting...")
           break
main()
