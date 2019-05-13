#!/usr/bin/env python3.6
from user import User
def create_user(platform,user_name,password):
    '''
    function to create a new user
    '''
    new_user = Details(platform,user_name,password)
    return new_user
    
