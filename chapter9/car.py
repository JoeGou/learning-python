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
    
my_new_car = Car('adui', 'R8', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

