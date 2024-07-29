from random import randint

class Die:
    '''定义一个骰子的类'''

    def __init__(self, num_sides=6):
        '''骰子默认是6面的'''
        self.num_sides = num_sides

    def roll(self):
        '''返回一个介于1和骰子面数之间的值'''
        return randint(1, self.num_sides)