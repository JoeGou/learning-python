from car import Car

my_new_car = Car('audi', 'r8', '2024')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading_rate = 23
my_new_car.read_odometer()