class User:
    '''
    class that generates new instances of users
    '''


    def __init__(self,platform,user_name,password):
        # method that defines properties for our objects

        self.platform = platform
        self.user_name = user_name
        self.password = password
    user_list = []
    def save_user(self):
        '''
        method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_platform(cls,platform):
        '''
        method that takes a platform  returns a user_name matching the platform
        '''
        for user in cls.user_list:
            if user.platform == platform:
                return user

    @classmethod
    def user_exist(cls,user_name):
        '''
        method that checks if a user exists from the user_list
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return True
        return False
