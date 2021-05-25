def getFoodDetail(food_id):
    """
    # 
    ---
    GET method
    pake path berupa id-nya food
    """

    # Initialize data
    data = {}

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
    data = result

    return data


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
