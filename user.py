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

    def delete_contact(self):
        '''
        method deletes a saved contact from the user_list
        '''
        User.user_list.remove(self)
