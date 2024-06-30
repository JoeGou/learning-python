from pathlib import Path
import json



def get_number(path):
    '''输入喜欢的数并存储'''
    number = input("Your favorite number:")
    contents = json.dumps(number)
    path.write_text(contents)
    return number

def get_stored_number(path):
    '''获取最喜欢的数'''
    contents = path.read_text()
    number = json.loads(contents)
    return number

def greeter_user():
    '''问候用户'''
    path = Path('favorite_numbers.json')

    if path.exists():
        number = get_stored_number(path)
        print(f"I know your favorite number! It is {number}")
    else:
        number = get_number(path)
        print(f"{number} is a nice number!")

greeter_user()