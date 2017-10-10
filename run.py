#!/usr/bin/env python3.6

from contact import Contact
import pyperclip

# Create a contact
def create_contact(first_name, last_name, phone_number, email):
    
    '''
    function to create a new contact
    '''
    new_contact = Contact(first_name, last_name, phone_number, email)
    return new_contact

# Save contacts
def save_contacts(contact):
    
    '''
    function to save contact
    '''
    
    contact.save_contact()
    
# Delete contact
def delete_contact(contact):
    
    '''
    function to delete a contact
    '''
    
    contact.delete_contact()
    
# Finding a contact
def find_contact(number):
    
    '''
    Function that finds contact by number and returns the contact
    '''
    
    return Contact.find_by_number(number)

# Check if a contact exists
def check_existing_contacts(number):
    
    '''
    Function that checks if a contact exists with that number and returns a boolean
    '''
    
    return Contact.contact_exist(number)

# Display all contacts
def display_contacts():
    
    '''
    Function that returns all the saved contacts
    '''
    
    return Contact.display_contacts()

# Copying a contacts email address
def copy_existing_email(number):
    
    '''
    Function that copys the email address of a contact to the machine
    '''
    
    return Contact.copy_email(number)

# CAlling the functions that implement the above behaivours 
def main():
    print("Hello wlecome to your contact list. What is your name?")
    
    user_name = input()
    
    print(f"Hello {user_name}. What would you like to do?")
    
    print("\n")
    
    while True:
        print("Use these short codes: cc - create a new contact, dc - display contact, fc - find a contact, del - delete contact , ce - copy email, ex - exist the contact list")
        
        short_code = input().lower()
        
        if short_code == 'cc':
            print("New Contact")
            print("-"*10)
            
            print("First name .....")
            first_name = input()
            
            print("Last name .....")
            last_name = input()
            
            print("Phone number .....")
            phone_number = input()
            
            print("Email address .......")
            email = input()
            
            # Create and save new contact
            save_contacts(create_contact(first_name, last_name, phone_number, email))
            
            print("\n")
            
            print(f"New Contact {first_name} {last_name} created")
            
            print("\n")
            
        elif short_code == 'dc':
            
            if display_contacts():
                
                print("Here is a list of all your contacts")
                
                print("\n")
                
                for contact in display_contacts():
                    
                    print(f"{contact.first_name} {contact.last_name} .............{contact.phone_number}")
                    
                print("\n")
                
            else:
                print("\n")
                
                print("You don't seem to have any contacts saved yet")
                
                print("\n")
                
        elif short_code == 'fc':
            
            print("Enter the number you want to search for")
            
            search_number = input()
            
            if check_existing_contacts(search_number):
                
                search_contact = find_contact(search_number)
                
                print(f"{search_contact.first_name} {search_contact.last_name}")
                
                print('-'*20)
                
                print(f"Phone number .....{search_contact.phone_number}")
                
                print(f"Email ......{search_contact.email}")
                
            else:
                print("That contact does not exist")
                
        elif short_code == 'del':
            
            print("Enter the number you want to delete")
            
            delete_number = input()
            
            if check_existing_contacts(delete_number):
                
                search_delete_contact = find_contact(delete_number)
                
                print(f"You have deleted {search_delete_contact.first_name} {search_delete_contact.last_name}\'s contact information")
                
                delete_contact(search_delete_contact)
                
            else:
                print("That contact does not exist")
                
        elif short_code == 'ce':
            
            print("Enter the number for the email you want to copy")
            
            search_number_for_email = input()
            
            if check_existing_contacts(search_number_for_email):
                
                contact_found = find_contact(search_number_for_email)
                
                contact_email = copy_existing_email(search_number_for_email)
                
                paste_contact_email = pyperclip.paste()
                
                print(f"{ pyperclip.paste()} belongs to {contact_found.first_name} {contact_found.last_name}")
            
            else:
                
                print("The contact does not exist")
            
        elif short_code == 'ex':
            
            print("Bye .........")
            
            break
        
        else:
            
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        