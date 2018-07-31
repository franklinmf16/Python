# from the_car_class import Car
import the_car_class as car

my_tesla = car.ElectricalCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.update_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()