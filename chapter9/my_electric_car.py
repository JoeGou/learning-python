from car import ElectricCar, Car, Battery

my_leaf = ElectricCar('nissian', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

my_panamera = Car('porsche', 'panamera', 2024)
print(my_panamera.get_descriptive_name())
