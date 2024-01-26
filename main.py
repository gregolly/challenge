def add_contact(contacts, contact_name, contact_phone, contact_email):
        contact = { 
                "name": contact_name, 
                "phone": contact_phone, 
                "email": contact_email, 
                "favorite": False }
        contacts.append(contact)
        print(f"Contact {contact_name} has been added")
        return

def show_contacts(contacts):
        print("Contact list:")
        for index, contact in enumerate(contacts, start=1):
                favorite = "★" if contact["favorite"] else " "
                contact_name = contact["name"]
                contact_phone = contact["phone"]
                contact_email = contact["email"]
                print(f"{index}. {favorite} Name: {contact_name} \nPhone: {contact_phone} \nE-mail: {contact_email}")
        return

def update_contact(
    contacts, 
    contact_index, 
    new_contact_name, 
    new_contact_phone, 
    new_contact_email
):
    contact_index_adjusted = int(contact_index) - 1
    if contact_index_adjusted >= 0 and contact_index_adjusted < len(contacts):
            contacts[contact_index_adjusted]["name"] = new_contact_name
            contacts[contact_index_adjusted]["phone"] = new_contact_phone
            contacts[contact_index_adjusted]["email"] = new_contact_email
            print(f"Contact {contact_index} has been updated for {new_contact_name} {new_contact_phone} {new_contact_email}")
    else:
        print("Task index invalid.")
    return

def favorite_contact(contacts, contact_index):
        contact_index_adjusted = int(contact_index) - 1
        if contact_index_adjusted >= 0 and contact_index_adjusted < len(contacts):
            contacts[contact_index_adjusted]["favorite"] = True
            print(f"Contact has been favorited")
        else:
            print("Contact index do not exist!")
        return

def show_favorite_contacts(contacts):
       for contact in contacts:
              if contact["favorite"] and len(contact["favorite"]) > 0:
                print("\nFavorite contact list")
                print("★ " + contact["name"])
              else:
                print("Empty list!")          
       return

def delete_contact(contacts, contact_index):
        contact_index_adjusted = int(contact_index) - 1

        if 0 <= contact_index_adjusted < len(contacts):
                deleted_contact = contacts.pop(contact_index_adjusted)
                print(f"Contact {deleted_contact['name']} has been deleted")
        else:
                print("Contact index is invalid")
        return

contacts = []

while True:
        print("\nContact list: ")
        print("1. Add a contact")
        print("2. Show contacts")
        print("3. Update a contact")
        print("4. favorite a contact")
        print("5. Show all favorites contacts")
        print("6. Delete a contact")
        print("7. Exit")

        select = input("Select a menu above: ")

        if select == "1":
                contact_name = input("Contact name: ")
                contact_phone = input("Contact phone: ")
                contact_email = input("Contact email: ")
                add_contact(contacts, contact_name, contact_phone, contact_email)
        elif select == "2":
                show_contacts(contacts)
        elif select == "3":
                show_contacts(contacts)
                contact_index = input("Type the contact number that you want to update: ")
                new_contact_name = input("Type the new contact name: ")
                new_contact_phone = input("Type the new contact phone: ")
                new_contact_email = input("Type the new contact e-mail: ")
                update_contact(contacts, contact_index, new_contact_name, new_contact_phone, new_contact_email)
        elif select == "4":
                contact_index = input("Type the contact number that you want to complete: ")
                favorite_contact(contacts, contact_index)
        elif select == "5":
               show_favorite_contacts(contacts)
        elif select == "6":
                contact_index = input("Type the contact number that you want to delete: ")
                delete_contact(contacts, contact_index)
        elif select == "7":
                break

print("Contact list has been finished!")