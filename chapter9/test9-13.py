from random import randint

class Die:
    
    def __init__(self, sides=6):
        
        self.sides = sides
        
    def roll_die(self):
        '''产生骰子随机数'''
        self.sides = randint(1, 6)
        print(f" -The point is {self.sides}\n")

# die_test = Die()    
# for i in range(10):
#     print(f"roll {i+1}:")
#     die_test.roll_die()
    
# die_test = Die(10)    
# for i in range(10):
#     print(f"roll {i+1}:")
#     die_test.roll_die()
    
die_test = Die(20)    
for i in range(10):
    print(f"roll {i+1}:")
    die_test.roll_die()    