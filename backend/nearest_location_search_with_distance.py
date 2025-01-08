import requests
from googleplaces import GooglePlaces
import googlemaps as gmaps

API_KEY = "API_KEY" # Replace with Google Map API Key


def get_closest_store(postal_code, store_name="No Frills", travel_mode='driving'):
    """
    Returns the name of the closest store, the address, and the distance to that store when given home postal code

    Parameters
    ----------------
    postal_code : str
        The home or origin postal code
    store_name: str
        The name of the store that you would like directions to
    travel_mode: str
        The method of transportation. Must be one of the values in the following list: [driving, walking, transit, bicycling]

    Returns
    -------------------
    str, str, str
        Returns 3 values, 1st value is the name of the closest store, 2nd is the address, and third is the distance to store
    """
    lat = 0
    lng = 0
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': f'{postal_code}',
        'key': API_KEY
    }


    try:
      response = requests.get(base_url, params)
      lat = response.json()['results'][0]['geometry']['location']['lat']
      lng = response.json()['results'][0]['geometry']['location']['lng']


    except Exception as err:
      print(f'Error occured: {err}')

    googlemaps = gmaps.Client(key=API_KEY)
    query_result = googlemaps.places_nearby(
        #lat_lng={'lat': lat, 'lng': lng},
        location=(lat, lng),
        rank_by="distance",
        name=store_name,
        type="grocery"
        )

    closest_store_results = query_result['results'][0]
    name = closest_store_results['name']
    place = closest_store_results['vicinity']
    origin=(lat,lng)
    dest = place
    distance_km, distance_time = get_distance(origin, dest, travel_mode)
    return name, place, distance_km, distance_time

#origin and dest must be pair of latitudes and longitudes
def get_distance(origin, destination, travel_mode='driving'):

    googlemaps = gmaps.Client(key=API_KEY)
    query_result = googlemaps.distance_matrix(
    origins=origin,
    destinations=destination,
    mode=travel_mode
    )
    distance_km = query_result['rows'][0]['elements'][0]['distance']['text']
    distance_time = query_result['rows'][0]['elements'][0]['duration']['text']
    return distance_km, distance_time


if __name__ == '__main__':
    #given a postal code, return the nearest location
    name, address_info, distance = get_closest_store("L5L1C6")
    print(name)
    print(address_info)
    print(distance)
