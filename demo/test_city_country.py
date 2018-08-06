import unittest
from city_country import city_country_connect


class CityCountryConnectTest(unittest.TestCase):


    def test_city_country_connect(self):
        get_connect = city_country_connect('beijing', 'china')
        self.assertEqual(get_connect, 'Beijing, China')

    def test_city_country_population_connect(self):
        get_connect = city_country_connect('beijing', 'china', '3000')
        self.assertEqual(get_connect, 'Beijing, China - 3000')

unittest.main()
