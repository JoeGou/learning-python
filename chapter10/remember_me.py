from pathlib import Path
import json

def get_stored_username(path):
    '''如果存储了用户名，就读取他'''
    if path.exists():
        contens = path.read_text()
        username = json.loads(contens)
        return username
    else:
            return None

def get_new_username(path):
    '''提示用户输入用户名'''
    username = input("What is your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    return username
     
def greeter_user():
    '''问候用户， 并指出其名字'''
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
         print(f"welcome back ! {username}")
    else:
        get_new_username(path)
        print(f"We'll remember you when you come back, {username}")

greeter_user()

