def make_car(brand, model, **additional_info):
    car_info = {}
    car_info['brand'] = brand
    car_info['model'] = model
    for key, value in additional_info.items():
        car_info[key] = value
    return car_info


my_car = make_car('ford', 'seden', location = 'Sydney', color = 'blue')
print(my_car)


