class User:
    '''
    class that generates new instances of users
    '''
    user_list = []

    def __init__(self,platform,user_name,password):
        # method that defines properties for our objects

        self.platform = platform
        self.user_name = user_name
        self.password = password
