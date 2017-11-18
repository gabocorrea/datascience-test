import unittest

class googlemapsutil_test(unittest.TestCase):
        
        def test_return_type():
            gmap = googlemapsutil(api_key='AIzaSyBhKgTnSKK_miAwAWc7UcStjl8-Yh6vy3s')
            point_A = 10.321312
            point_B = 10.321312
            val = type(gmap.get_distance_matrix(point_A, point_B))
            self.assertEqual(val, type({}))


if __name__ == '__main__':
    unittest.main()