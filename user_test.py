import unittest # import unittest module
from user import User # import user class

class TestUser(unittest.TestCase):
    '''
    Test class defining the test case for user class behaviours
    Args:
        unittest.TestCase: helps in creating test cases
    '''

    def setUp(self):
        '''
        setup method to run before each test cases
        '''
        self.new_user = User("twitter","@Michael","12345678")
    def test_init(self):
        '''
        test if object is initialized properly
        '''
        self.assertEqual(self.new_user.platform,"twitter")
        self.assertEqual(self.new_user.user_name,"@Michael")
        self.assertEqual(self.new_user.password,"12345678")

    # test for saving contacts

    def test_save_contact(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()
