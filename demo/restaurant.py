class Restaurant():
    def __init__ (self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name)
        print("The cuisine' type is "+ self.cuisine_type)
    
    def open_restaurant(self):
        print("The restaurant is opining")
    
    def update_number_served(self, update_number_served):
        self.number_served = update_number_served

    def increment_number_served(self, increment_number_served):
        self.number_served += increment_number_served

class IneCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, *flavors):
       super().__init__(name, cuisine_type)
       self.flavors = flavors
    
    def describe_restaurant(self):
        print("It is a " + self.restaurant_name + " with cuisine of " + self.cuisine_type + " and" , end = " ")
        for flavor in self.flavors:
            print(flavor, end = " ")
        print("flavors")
    



the_restaurant = Restaurant('Mac', 'Australia')
ice_stand = IneCreamStand('ice', 'icecream', 'tomato', 'chocolate')


# the_restaurant.describe_restaurant()
# the_restaurant.open_restaurant()
# the_restaurant.update_number_served(10)
# the_restaurant.increment_number_served(5)

ice_stand.describe_restaurant()


print("The are " + str(the_restaurant.number_served) + " been to this restaurant")


