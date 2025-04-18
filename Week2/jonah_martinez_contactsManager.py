#Assignment: contactsManager.py 
#Class: DEV 128
#Date: 04/17/2025
#Author: Jonah Martinez
#Description: Program to manage a list of contacts

# Print the command menu for the program.
def command_menu():
    print("COMMAND MENU\n"
                    "\tlist - Display all contacts\n"
                    "\tview - View a contact\n"
                    "\tadd - Add a contact\n"
                    "\tdel - Delete a contact\n"
                    "\tfield - View a field for all contacts\n"
                    "\texit - Exit program")

# Lists the all the contacts in the dictionary.
def list(contacts):
    if not contacts:
        print("No contacts to show.")
        return
    
    # Enumerate the contacts to display them with an index.
    for index, contact in enumerate(contacts):
        print(f"\t{index + 1}. {contact}")

# Ask the user for a contact name and display the details of that contact.        
def view(contacts):
    name = input("Enter the name: ").strip().capitalize()
    if name not in contacts:
        print(f"No contact found for that name.")
        return
    
    # Extract the attributes of the contact and sort them for display.
    attributes = [key for key in contacts[name]]
    attributes.sort()
    print(f"Viewing contact for {name}")
    
    for attribute in attributes:
        print(f"{attribute}: {contacts[name][attribute]}")

# Add a new contact to the dictionary.     
def add(contacts):
    name = input("Enter the name for the new contact: ").strip().capitalize()
    if name in contacts:
        print(f"Contact for {name} already exists.")
        return
    
    # Prompt the user for the contact details.    
    address = input("Enter the address for the new contact: ").strip()
    mobile = input("Enter the mobile number for the new contact: ").strip()
    company = input("Enter the company for the new contact: ").strip()
    
    # Add the new contact to the dictionary.
    contacts[name] = {
        "address": address,
        "mobile": mobile,
        "company": company
    }

# Delete a contact from the dictionary.        
def delete(contacts):
    name = input("Enter the name: ").strip().capitalize()
    
    if name not in contacts:
        print(f"No contact found for that name.")
        return
    
    del contacts[name]
    print(f"Contact for {name} deleted.")

# Display a specific field for all contacts.    
def field(contacts):
    field = input("Please enter the field you want to view: ").strip().lower()
    
    if not contacts:
        print("No contact found with that field")
        return
    
    # Checks if the field exists in any of the contacts.
    # It will break the loop if it finds a contact with that field.
    # And set found to True.
    found = False
    for contact in contacts:
        try:
            contacts[contact][field]
            found = True
            break
        except  KeyError:
            continue
    
    # If no contact has the field, print a message and return.
    if not found:
        print(f"No contact found with that field")
     
    # Display the field for each contact.   
    for contact in contacts:
        print(f"{contact}\t: { contacts[contact][field] if contacts.get(contact).get(field) else "**No Data**"} ")

# Execute the command based on user input.   
def execute_command(command, contacts):
    match command:
        case "list":
            list(contacts)
        case "view":
            view(contacts)
        case "add":
            add(contacts)
        case "del":
            delete(contacts)
        case "field":
            field(contacts)
            
def main():

    contacts = {
        "Joel":
            {"address": "1500 Anystreet, San Francisco, 94110", "company":"A startup",
             "mobile": "555-555-1111"},
        "Anne":
            {"address": "1000 Somestreet, Fresno, CA 93704",
             "state": "California",
             "landline": "125-555-2222", "company": "Some Great Company"},
        "Sally":
            {"state": "Illinois", "landline":"217-555-1222", "company": "Illinois Technologies",
             "mobile": "217-333-2353"},
        "Ben":
            {"address": "1400 Another Street, Fresno CA 93704",
             "state": "California", "mobile": "125-555-4444"}             
    }

    print("Welcome to contacts manager program")
    
    # Main program loop.
    # It will keep asking for a command until the user enters "exit".
    command = ""
    while command != "exit":
        
        command_menu()
        while True:
            command = input("Please enter the command: ").lower().strip()
            if command in ["list", "view", "add", "del", "field", "exit"]:
                break
            else:
                print("Invalid command. Please try again.")
                
        execute_command(command, contacts)

    print("Good bye")

if (__name__ == "__main__"):
    main()

