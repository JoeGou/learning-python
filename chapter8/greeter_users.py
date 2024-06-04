def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!\n"
        print(msg)
        
usernames = ['Jack', 'John', 'Lucy']
greet_users(usernames)