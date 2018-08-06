def city_country_connect(city, country, population = ''):
    
    
    if population:
        connect = city + ', ' + country + ' - ' + population
    else:
        connect = city + ', ' + country
    return connect.title()

# print(city_country_connect('beijing', 'china', '3000000'))
# print(city_country_connect('beijing', 'china'))