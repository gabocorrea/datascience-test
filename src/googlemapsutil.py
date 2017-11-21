from os import path
import urllib3
import json

class googlemapsutil():

    base_url = 'https://maps.googleapis.com/maps/api'

    def __init__(self, api_key, base_url = base_url):
        self.api_key = api_key
        urllib3.disable_warnings()





    # Returns a dictionary that contains the information sent by the server
    def _send_request(self, url, answer_type='json'):
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        if answer_type == 'json':
            return json.loads(r.data.decode('utf-8'))
        elif answer_type == 'xml':
            return {'error': 'xml not yet supported'}   #TODO
        else:
            return {'error': 'only json and xml supported'}

    # Returns a dictionary that should contain the following keys:
    # 'distance','duration','duration_in_traffic'
    def get_distance_matrix(self, point_A, point_B, suburl='distancematrix', answer_type='json', mode='driving', departure_time='now'):
        url_params = [self.base_url, suburl, answer_type, point_A['lat'], point_A['lng'], point_B['lat'], point_B['lng'], mode, departure_time, self.api_key]
        url = '{0}/{1}/{2}?origins={3},{4}&destinations={5},{6}&mode={7}&departure_time={8}&key={9}'.format( *url_params )
        ans = self._send_request(url, answer_type)
        return ans


    # Returns seconds (int) of a google distance estimation.
    # The parameter dictionary should be what get_distance_matrix returns.
    def get_duration(self, dictionary):
        if 'rows' in dictionary:
            if len(dictionary['rows']) > 0:
                return dictionary['rows'][0]['elements'][0]['duration']['value']




def main():
    def _my_simple_test():
        api_key = 'AIzaSyBhKgTnSKK_miAwAWc7UcStjl8-Yh6vy3s'
        gmap = googlemapsutil( api_key )
        point_A = {'lat':-33.419432, 'lng':-70.598669}
        point_B = {'lat':-33.426655, 'lng':-70.616000}
        ans = gmap.get_distance_matrix(point_A,point_B)
        for key,val in ans.items():
            print('{}\t\t{}'.format(key,val))
        print('')
        print(ans['rows'][0]['elements'][0]['duration']['text'])
        print(gmap.get_duration(ans))

    _my_simple_test()



if __name__ == '__main__':
    main()