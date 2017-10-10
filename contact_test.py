import unittest 
from contact import Contact 
import pyperclip

class TestContact(unittest.TestCase):

    '''
    test class that defines test cases for the contact class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases 
    '''

    def setUp(self):

        '''
        set up method to run before each test cases
        '''

        # create contact object
        self.new_contact = Contact("James", "Muriuki", "0712345678", "james@ms.com") 

    def tearDown(self):

        '''
        tearDown method that does clean up after each test case has run
        '''

        Contact.contact_list = []


    # Check if contact object is initialized    
    def test_init(self):

        '''
        test_init Test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"James")
        self.assertEqual(self.new_contact.last_name,"Muriuki")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"james@ms.com")

    # Check if one contact is saved
    def test_save_contact(self):

        '''
        test_save_contact test case to test if the contact object is saved into the contact list
        '''

        self.new_contact.save_contact() #saving the new contact

        self.assertEqual(len(Contact.contact_list),1)

    # Check if multiple contacts are saved
    def test_save_multiple_contact(self):

        '''
        test_save_multiple to check if you can save multiple contact objects to our contact_list
        '''

        self.new_contact.save_contact()

        # create new contact
        test_contact = Contact("test","user","07876654321","test@user.com")

        # save the new contact
        test_contact.save_contact()

        self.assertEqual(len(Contact.contact_list),2)

    # check if contact is deleted
    def test_delete_contact(self):

        '''
        test_delete_contact to test if we can remove a contact from a contact list
        '''

        self.new_contact.save_contact()

        # create new contact
        test_contact = Contact("test","user","07876654321","test@user.com")

        # save the new contact
        test_contact.save_contact()

        # deleting a contact object
        self.new_contact.delete_contact()

        self.assertEqual(len(Contact.contact_list),1)

    # check if the contact object is equal to the saved contact
    def test_find_contact_by_number(self):

        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_contact.save_contact()

        # create new contact
        test_contact = Contact("test","user","07876654321","test@user.com")

        # save the new contact
        test_contact.save_contact()

        # use find by contact method
        found_contact = Contact.find_by_number("07876654321")

        self.assertEqual(found_contact.email,test_contact.email)
        
    # check if contact object exists
    def test_contact_exists(self):
        
        '''
        test to check if we can return a boolean if we can't find the contact
        '''

        self.new_contact.save_contact()

        # create new contact
        test_contact = Contact("test","user","07876654321","test@user.com")

        # save the new contact
        test_contact.save_contact()
        
        # use contact exist method
        contact_exists = Contact.contact_exist("07876654321")
        
        self.assertTrue(contact_exists)
        
    # check if contact object exists
    def test_contact_does_not_exists(self):
        
        '''
        test to check if we can return a boolean if we can't find the contact
        '''

        self.new_contact.save_contact()

        # create new contact
        test_contact = Contact("test","user","07876654321","test@user.com")

        # save the new contact
        test_contact.save_contact()
        
        # use contact exist method
        contact_exists = Contact.contact_exist("07876654320")
        
        self.assertFalse(contact_exists)
        
    # check if all the contacts are displayed
    def test_display_all_contacts(self):
        
        '''
        Mehtod that returns a list of all contacts saved
        '''
        
        self.assertEqual(Contact.display_contacts(),Contact.contact_list)
        
    # Check if we can copy and paste contact
    def test_copy_email(self):
        
        '''
        Test to confirm that we are copying the email address from a found contact 
        '''

        self.new_contact.save_contact()
        
        Contact.copy_email("0712345678")
        
        self.assertEqual(self.new_contact.email,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()

