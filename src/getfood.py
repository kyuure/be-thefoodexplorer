from google.cloud import firestore
db = firestore.Client()


def getFoodDetail(food_id):
    """
    # 
    ---
    GET method
    pake path berupa id-nya food
    """

    # Initialize data
    data = {}
    users_ref = db.collection(u'food')
    docs = users_ref.where(u'id', u'==', food_id).stream()


    # Do querying and check for the result
    # Currently using dummy data
    result = {
            'success' : True,
            'message' : 'Some message',
            'data' : {
                'description' : 'Loren ipsum',
                'ingredient'  : ['Nasi', 'Tahu'],
                'taste' : ['Pedas'],
            }
        }

    if not result:
        return {'success' : False,
                'message' : f'Data id {food_id} tidak ditemukan'}
   
    for el in docs:
        data = el.to_dict()
    
    #data = { el.id: el.to_dict() for el in docs }
    real_data = data
    send_dict = {}
    
    send_dict['description'] = real_data['description']
    send_dict['ingredient'] = real_data['ingredients'] 
    send_dict['taste'] = real_data['taste']

    return {'success' : True,
                'message': 'BERHASIL BERHASIL BERHASIL HOREEEE',
                'data': send_dict
                }


def getFoodStores(food_id):
    """
    # 
    ---
    GET method
    pake path berupa id-nya food
    """

    # Initialize data
    data = {}

    # Use Google Maps API for search store (Places)
    # Refer to the docs here
# Set up console : https://developers.google.com/maps/documentation/places/web-service/cloud-setup
# Places IDs  : https://developers.google.com/maps/documentation/places/web-service/place-id
# Places types: https://developers.google.com/maps/documentation/places/web-service/supported_types

    # Currently using dummy data
    result = {
            'success' : True,
            'message' : 'Some message',
            'data' : {
                'description' : 'Loren ipsum',
                'ingredient'  : ['Nasi', 'Tahu'],
                'taste' : ['Pedas'],
            }
        }

    if not result:
        return {'success' : False,
                'message' : f'Data id {food_id} tidak ditemukan'}
    data = result

    return data
