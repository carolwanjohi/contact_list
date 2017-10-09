import unittest 
from contact import Contact 

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
        





if __name__ == '__main__':
    unittest.main()

