from pathlib import Path

path = Path('guest_book.txt')

flag = True
users = ''

while flag:
    
    user_name = input('Please enter your name(enter quit to end): ')
    if user_name != 'quit':
        users += f"{user_name}\n" 
        path.write_text(users)
    else:
        flag = False