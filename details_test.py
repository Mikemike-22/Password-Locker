import unittest
from details import Details

class TestDetails(unittest.TestCase):
    '''
    Test class that defines test cases for details behaviours
    '''
    def setUp(self):
        self.new_details = Details("mike","korir","123@gmail.com")
    def tearDown(self):
        '''
        method allows cleanup after each tst has run
        '''
        Details.details_list =[]

    def test_init(self):
        '''
        test to check if object is initialised properly
        '''
        self.assertEqual(self.new_details.first_name,"mike")
        self.assertEqual(self.new_details.last_name,"korir")
        self.assertEqual(self.new_details.email,"123@gmail.com")
    def test_save_details(self):
        '''
        test case to test if the details object is saved
        '''
        self.new_details.save_details() # saving the new contact
        self.assertEqual(len(Details.details_list),1)

    def test_save_multiple_details(self):
        '''
        test to check if we can save multiple details
        '''
        self.new_details.save_details()
        test_details = Details("mike","korir","123@mail.com")
        test_details.save_details()
        self.assertEqual(len(Details.details_list),2)

    def test_delete_contact(self):
        '''
        tests if we can remove a detail from our details_list
        '''
        self.new_details.save_details()
        test_details = Details("mike","korir","123@gmail.com")
        test_details.save_details()
        self.new_details.delete_details()
        self.assertEqual(len(Details.details_list),1)



if __name__ =='__main__':
    unittest.main()
