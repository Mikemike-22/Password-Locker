class Details:
    '''
    class generating new instances of Details
    '''


    def __init__(self,first_name,last_name,email):
    # properties for the objects
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    details_list=[]
    def save_details(self):
        """
        method saves contact objects into details_list
        """
        Details.details_list.append(self)
    def delete_details(self):
        """
        delete method deletes a saved detail
        """
        Details.details_list.remove(self)
    @classmethod
    def find_by_first_name(cls,first_name):
        '''
        method that takes in first name and returns an email
        '''
        for details in cls.details_list:
            if details.first_name == first_name:
                return details
