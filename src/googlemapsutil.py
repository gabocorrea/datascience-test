from os import path
import urllib3
import json

class googlemapsutil():

    base_url = 'https://maps.googleapis.com/maps/api'

    def __init__(self, api_key, base_url = base_url):
        self.api_key = api_key


    # Returns a dictionary that should contain the following keys:
    # 'distance','duration','duration_in_traffic'
    def get_distance_matrix(self, point_A, point_B, suburl='distancematrix', answer_type='json', mode='driving', departure_time='now'):
        url_params = (base_url, suburl, answer_type, point_A['lat'], point_A['lng'], point_B['lat'], point_B['lng'], mode, departure_time, self.api_key)
        url = '{}/{}/{}?origins={},{}&destinations={},{}&mode={}&departure_time={}&key={}'.format( url_params )
        ans = send_request(url, answer_type)
        return ans






    # Returns a dictionary that contains the information sent by the server
    def _send_request(url, answer_type='json'):
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        if answer_type == 'json':
            return json.loads(r.data.decode('utf-8'))
        elif answer_type == 'xml':
            return {'error': 'xml not yet supported'}   #TODO
        else
            return {'error': 'only json and xml supported'}


