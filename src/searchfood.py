# Source: https://cloud.google.com/firestore/docs/quickstart-servers#python
from re import search
from google.cloud import firestore
db = firestore.Client()


def searchFoodByImage(img):
    """
    # 
    ---
    POST method
    formdata berisi image
    """

    # Initialize data
    data = {}

    # Run model then specify the name of food

    # Currently using dummy data
    result = {
            'success' : True,
            'message' : 'Some message',
            'data' : [
                {
                    'id': 0,
                    'name': 'Tahu',
                    'city': 'Jakarta',
                    'image': 'localhost'
                },
                {
                    'id': 0,
                    'name': 'Tahu',
                    'city': 'Jakarta',
                    'image': 'localhost'
                }
            ]
        }

    if not result:
        return {'success' : False,
                'message' : 'Image doesnt match any object.'}
    data = result

    return data


def searchFoodByText(query):
    """
    # 
    ---
    GET method
    pake query
    """

    # Do querying
    users_ref = db.collection(u'food')
    docs = users_ref.stream()
    
    # Assign the query to local variable
    real_dict = {}
    send_dict = []
    for el in docs:
        if not search('.*'+query.lower()+'.*', str(el.id).lower()):
            continue
        data = el.to_dict()
        real_dict['id']    = data['id']
        real_dict['name']  = el.id
        real_dict['city']  = data['city'] 
        real_dict['image'] = data['image']
        send_dict.append(real_dict)

    # Check for the result
    if not send_dict:
        return {'success' : False,
                'message' : f'Query {query} doesnt match any object.'}

    # Return the result
    return {
            'success' : True,
            'message': 'BERHASIL BERHASIL BERHASIL HOREEEE',
            'data': send_dict
        }
