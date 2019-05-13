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
    def tearDown(self):
        '''
        method that cleans up after each test case has run
        '''
        User.user_list=[]
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

    def test_save_multiple_users(self):
        '''
        test to check if we can save multiple user
        '''
        self.new_user.save_user()
        test_user = User("facebook","qwerty","0987654")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    def test_delete_user(self):
        '''
        tests if we can remove users form our user_list
        '''
        self.new_user.save_user()
        test_user = User("instagram","mike","345678")
        test_user.save_user()
        self.new_user.delete_user() # delete contact objects
        self.assertEqual(len(User.user_list),1)
    def test_find_user_by_platform(self):
        '''
        test to check if we can find a user by platform and display the informatiom
        '''
        self.new_user.save_user()
        test_user = User("github","mike","password")
        test_user.save_user()
        found_user = User.find_by_platform("github")
        self.assertEqual(found_user.user_name,test_user.user_name)

    def test_user_exists(self):
        '''
        test to check if we can return a boolean if we cannot find the contact
        '''
        self.new_user.save_user()
        test_user = User("linkedin","mike","password")
        test_user.save_user()
        user_exists = User.user_exist("mike")
        self.assertTrue(user_exists)
    def test_display_all_users(self):
        '''
        method that returns list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)




if __name__ == '__main__':
    unittest.main()
