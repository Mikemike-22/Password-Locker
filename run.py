#!/usr/bin/env python3.6
from user import User
def create_user(platform,user_name,password):
    '''
    function to create a new user
    '''
    new_user = Details(platform,user_name,password)
    return new_user
def save_users(user):
    '''
    Function to save_user
    '''
    user.save_user()
def save_details
def delete_user(user):
    '''
    function to delete a user
    '''
    user.delete_user()
def find_user(user):
    '''
    function to find user by platform
    '''
    return User.find_by_platform(paltform)
def display_users():
    '''
    function that returns all saved contacts
    '''
    return User.display_users()

def main():
    print("Hello welcome to password locker application?")
    user_name=input()
    print(f"Hello {user_name}. what would you like to do?)
    print('\n')
    while True:
        print("Use these short codes : cc- create a new user, dc -display user, fc -find a user,ex -exit the user list")
                short_code = input().lower()

                if short_code == 'cc':

                        print("New Contact")
                        print("-"*10)

                        print("Platform")
                        platform = input()

                        print("Password")
                        password = input()

                        save_users(create_user(platform,user_name,password))

                        print('\n')
                        print(f"New User {platform} {user_name}created")

                        print('\n')
                    elif short_code == 'dc':

                        if display_users():
                            print("Here is a list of all your users")
                            print('\n')
                            for user in display_users():
                                print("{user.user_name} {user.platform}...{user.password}")
                                print('\n')
                            else:
                                print('\n')
                                print("You dont seem to have any contacts saved yet")
                                print('\n')
                                elfif short_code == 'fc':
                                print("Enter the user_name you want to search for ")
                                search_user = input()
                                if check_existing_contacts(search_user):
                                print("{searcsearch_user.user_name}{search_user.platform}")
                                print('-'*20)
                                print("platform.... {search_user.platform}")
                                print("user_name....{search_user.user_name}")
                            else:
                                print("User doesnt exist")

                            elif short_code == "ex":
                                print("Bye...")
                                break
                            else:
                                print("Please use short codes")
