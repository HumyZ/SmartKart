import requests
import googlemaps as gmaps

API_KEY = "API_KEY" # Replace with Google Map API Key

def get_closest_store(postal_code, store_name="No Frills"):
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': postal_code,
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
    return name, place
if __name__ == '__main__':
    #given a postal code, return the nearest location
    name, address_info = get_closest_store("L5L1C6")
    print(name)
    print(address_info)
