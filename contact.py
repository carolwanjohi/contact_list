class Contact:
    """
    class that generates new instances of contacts
    """

    contact_list = [] # empty contact list

    def __init__(self,first_name,last_name,phone_number,email):

        '''
        __init__ method that helps define properties for our objects

        Args:
            first_name:new contact first name
            last_name:new contact last name
            phone_number:new contact phone number
            email:new contact email address
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list

        '''
        Contact.contact_list.append(self)

    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact list
        '''

        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls, number):

        '''
        method that takes in a number and returns a contact that matches that number

        Args:
            number : phone number to search for

        Returns:
            Contact of person that matches the number
        '''

        for contact in cls.contact_list: 
            if contact.phone_number == number:
                return contact




