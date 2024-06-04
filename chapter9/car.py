'''一个用来表示汽车的类'''
class Car:
    '''simulate car'''
    
    def __init__(self, make, model, year):
        '''attributes'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        '''return description'''
        formal_name = f"{self.year} {self.make} {self.model}"
        
        return formal_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

class Battery:
    '''一次模拟电动汽车的尝试'''
    
    def __init__(self, battery_size=40):
        '''初始化电池属性'''
        self.battery_size = battery_size
    
    def describe_battery(self):
        '''打印电池容量'''
        print(f"This battery has a {self.battery_size}-kwh battery")
        
    def get_range(self):
        '''打印续航里程'''
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge")  
    
class ElectricCar(Car):
    '''模拟电动汽车独特之处'''
    
    def __init__(self, make, model, year):
        '''先初始化父类属性，再初始化电动汽车独有属性'''
        
        super().__init__(make, model, year)
        self.battery = Battery()  
            
# my_new_car = Car('adui', 'R8', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

