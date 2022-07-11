from random import randint
import  hashlib

class Player:
    def __init__(self, username):
        self.username = username
        self.password = ''
    def create_pw(self, word):
        user_seg = len(self.username)
        newpw  = hashlib.sha256(str(word + str(user_seg)).encode('utf-8')).hexdigest()
        self.password = str(newpw)

def verify_pw(user, pw):
    user_seg = len(user.username)
    test_pw  = hashlib.sha256(str(pw + str(user_seg)).encode('utf-8')).hexdigest()
    if (test_pw == user.password):
        return 1
    else:
        return 2

# program starts here

users_list = []

with open('users.txt', encoding='utf-8') as file:
    for line in file:
        new_user = Player(line.split(' ')[0])
        new_user.password = (line.split(' ')[1]).strip()
        users_list.append(new_user)
    file.close()

print("1. Sign in \n2. Sign up")

while(True):
    user_selection = input()

    if (user_selection == '1' or user_selection == '2'):
        break

if (user_selection == '1'):
    sign_in_success = 0

    while (sign_in_success == 0):
        username_attempt = input("User name: ")
        pwd_attempt = input("Password: ")
        
        user_exists = 0
        for user in users_list:
            if user.username == username_attempt:
                if verify_pw(user, pwd_attempt) == 1:
                    print("sign in successful")
                    sign_in_success = 1
                else:
                    print("password incorrect. Please try again.")
                user_exists = 1
        
        if (user_exists == 0):
            print("username does not exist. Please try again.")

if (user_selection == '2'):
    username_is_unique = 0
    while (username_is_unique == 0):
        new_username = input("username: ")
        for user in users_list:
            if user.username == new_username:
                print("username taken. Please try another username")
                username_is_unique = 0
                break
            else:
                username_is_unique = 1


    new_pwd = input("password: ")

    new_user = Player(new_username)
    new_user.create_pw(new_pwd)

    with open('users.txt', 'a', encoding='utf-8') as file:
        file.write("\n" + new_user.username + " " + new_user.password)
        file.close()