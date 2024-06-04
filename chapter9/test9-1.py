class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        
    def describe_restaurant(self):
        '''print restaurant info'''
        print(f"The restaurant's name is {self.name.title()}!")
        print(f"The restaurant's type is {self.type.title()}!")

    def open_restaurant(self):
        '''Indicate whether the restaurant is open or not'''
        print("The restaurant is open")
        
        
restaurant = Restaurant('banv', 'hot pot') 
print(f"The restaurant's name is {restaurant.name}")
print(f"The restaurant's type is {restaurant.type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()  

print("\n")
restaurant2 = Restaurant('xibei', 'NorthWest chinese cuisine')
restaurant2.describe_restaurant()

print("\n")
restaurant3 = Restaurant('hema', 'fresh food supermarket')
restaurant3.describe_restaurant()