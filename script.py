from random import randint
import  hashlib
m = hashlib.sha256

class Player:
    def __init__(self, username):
        self.username = username
        self.password = ''
    def create_pw(self, word):
        user_seg = len(self.username)
        stringtohash = word
        newpw  = hashlib.sha256(str(stringtohash + str(user_seg)).encode('utf-8')).hexdigest()
        self.password = str(newpw)

def verify_pw(user, pw):
    user_seg = len(user.username)
    stringtohash = pw
    testpw  = hashlib.sha256(str(stringtohash + str(user_seg)).encode('utf-8')).hexdigest()
    if (testpw == user.password):
        return 1
    else:
        return 2

# program starts here

users_list = []

with open('users.txt', encoding='utf-8') as file:
    for line in file:
        newuser = Player(line.split(' ')[0])
        newuser.password = (line.split(' ')[1]).strip()
        users_list.append(newuser)
    file.close()

print("1. Sign in \n2. Sign up")

user_selection = input()

if (user_selection == '1'):
    username_attempt = input("User name: ")
    pwd_attempt = input("Password: ")
    
    user_exists = 0
    for user in users_list:
        if user.username == username_attempt:
            if verify_pw(user, pwd_attempt) == 1:
                print("sign in successful")
            else:
                print("password incorrect")
            user_exists = 1
    
    if (user_exists == 0):
        print("username does not exist")

if (user_selection == '2'):
    newusername = input("username: ")
    newpwd = input("pwd: ")

    new_user = Player(newusername)
    new_user.create_pw(newpwd)

    with open('users.txt', 'a', encoding='utf-8') as file:
        file.write("\n" + new_user.username + " " + new_user.password)
        file.close()