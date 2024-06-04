class User:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self):
        print(f"The guest's name is {self.first_name.title()} {self.last_name.title()}")
        
    def greeter_user(self):
        print(f"Let's welcome {self.first_name.title()} {self.last_name.title()}")
        
user1 = User('Zhuang', 'Gou')
user2 = User('M', 'JL')
user3 = User('Jack', 'Zhang')

user1.describe_user()
user1.greeter_user()
print("\n")

user2.describe_user()
user2.greeter_user()
print("\n")

user3.describe_user()
user3.greeter_user()
