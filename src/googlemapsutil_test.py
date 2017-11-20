import unittest
from googlemapsutil import googlemapsutil

class googlemapsutil_test(unittest.TestCase):
        
    def setUp(self):
        self.gmap = googlemapsutil(api_key='AIzaSyBhKgTnSKK_miAwAWc7UcStjl8-Yh6vy3s')
        self.points = (
            #(origin, destination)
            ({'lat':10.321312, 'lng':10.321312}, {'lat':20.321312, 'lng':20.321312}),
        )
    
    def tearDown(self):
        pass


    ########################################

    def test_parameterTypes(self):
        for origin,destination in self.points:
            self.assertEqual( type(origin) , dict)
            self.assertEqual( type(origin['lat']) , float)
            self.assertEqual( type(origin['lng']) , float)

            self.assertEqual( type(destination) , dict)
            self.assertEqual( type(destination['lat']) , float)
            self.assertEqual( type(destination['lng']) , float)

    def test_returnType(self):
        for origin,destination in self.points:
            self.assertEqual( type(self.gmap.get_distance_matrix(origin, destination)) , dict )

    def test_parameterValues(self):
        for origin,destination in self.points:
            self.assertTrue( origin['lat'] >= -90 )
            self.assertTrue( origin['lat'] <= 90 )
            self.assertTrue( origin['lng'] >= -180 )
            self.assertTrue( origin['lng'] <= 180 )
            
            self.assertTrue( destination['lat'] >= -90 )
            self.assertTrue( destination['lat'] <= 90 )
            self.assertTrue( destination['lng'] >= -180 )
            self.assertTrue( destination['lng'] <= 180 )



if __name__ == '__main__':
    unittest.main()