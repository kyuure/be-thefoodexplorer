# Source: https://cloud.google.com/firestore/docs/quickstart-servers#python
from google.cloud import firestore
db = firestore.Client()

import requests
api_file = open("/app/api-key.txt", "r")
api_key = api_file.read()
api_file.close()


def getFoodDetail(food_id):
    """
    # 
    ---
    GET method
    pake path berupa id-nya food
    """

    # Do querying
    users_ref = db.collection(u'food')
    docs = users_ref.where(u'id', u'==', food_id).stream()

    # Check for the result
    data = {}
    for el in docs:
        data = el.to_dict()
    if not data:
        return {'success' : False,
                'data'    : [],
                'message' : f'Data id {food_id} tidak ditemukan'}
    
    # Assign the query to local variable
    send_dict = {}
    send_dict['description'] = data['description']
    send_dict['ingredient']  = list(data['ingredients'].values())
    send_dict['taste']       = list(data['taste'].values())

    # Return the result
    return {
            'success' : True,
            'message': 'BERHASIL BERHASIL BERHASIL HOREEEE',
            'data': send_dict
        }


def getFoodStores(food_id, lat, lng):
    """
    # 
    ---
    GET method
    pake path berupa id-nya food
    """
    # Use Google Maps API for search store (Places)
    # Refer to the docs here
    # Set up console : https://developers.google.com/maps/documentation/places/web-service/cloud-setup
    # Places IDs  : https://developers.google.com/maps/documentation/places/web-service/place-id
    # Places types: https://developers.google.com/maps/documentation/places/web-service/supported_types
    # 
    # If use cmd, use this
    # example: https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY
    # example link cased on geolocation:
    #   https://www.google.com/maps/search/?api=1&query={lat},{lng}

    # Do querying and check for the result
    docs = db.collection(u'food').where(u'id', u'==', food_id).stream()
    query = ''
    for el in docs:
        query = el.id
    if not query:
        return {'success' : False,
                'data'    : [],
                'message' : f'Data id {food_id} tidak ditemukan'}

    # Get data from Google Maps API
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    r = requests.get(
            url
            + 'location=' + str(lat) + ',' + str(lng)
            + '&radius=' + str(1500)
            + '&type=' + 'restaurant' #bakery,cafe,meal_delivery,meal_takeaway,restaurant,tourist_attraction'
            + '&keyword=' + query
            + '&key=' + api_key
        )

    # Assign the query to local variable
    r = r.json()['results']
    send_dict = []
    for result in r:
        real_dict = {}
        real_dict['name']    = result['name']
        real_dict['address'] = result['vicinity'] 
        real_dict['map_url'] = 'https://www.google.com/maps/search/' \
                        + '?api=1&query={},{}'.format(
                                result['geometry']['location']['lat'],
                                result['geometry']['location']['lng']
                            ) \
                        + '&query_place_id=' + result['place_id']
        send_dict.append(real_dict)

    # Return the result
    return {
            'success' : True,
            'message': 'BERHASIL BERHASIL BERHASIL HOREEEE',
            'data': send_dict
        }
