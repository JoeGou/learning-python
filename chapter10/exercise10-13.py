from pathlib import Path
import json

def get_stored_userinfo(path):
    '''如果存储了用户名，就读取他'''
    if path.exists():
        contents = path.read_text()
        userinfo = json.loads(contents)
        return userinfo
    else:
            return None

def get_new_userinfo(path):
    '''提示用户输入用户信息'''
    username = input("What is your name? ")
    user_hobby = input("What is you hobby? ")
    user_motto = input("What is your mottor? ")
    user = {
         'username': username,
         'userhonny':user_hobby,
         'usermottor': user_motto
    }
    contents = json.dumps(user)
    path.write_text(contents)
    return user
     
def greeter_user():
    '''问候用户， 并指出其名字'''
    path = Path("userinfo.json")
    userinfo = get_stored_userinfo(path)
    if userinfo:
        print(f"Hello, Are you {userinfo['username']}: ")
        if input("yes/no:") == 'yes':
            for key, value in userinfo.items():
                print(f"{key} : {value}")
        else:
            userinfo = get_new_userinfo(path)
            print(f"We'll remember you when you come back, {userinfo['username']}")
    else:
        userinfo = get_new_userinfo(path)
        print(f"We'll remember you when you come back, {userinfo['username']}")
greeter_user()

