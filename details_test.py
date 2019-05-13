import unittest
from details import Details

class TestDetails(unittest.TestCase):
    '''
    Test class that defines test cases for details behaviours
    '''
    def setUp(self):
        self.new_details = Details("mike","korir","123@gmail.com")
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


if __name__ =='__main__':
    unittest.main()
