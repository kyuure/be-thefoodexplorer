# Source: https://cloud.google.com/firestore/docs/quickstart-servers#python
from google.cloud import firestore
db = firestore.Client()


def searchFoodByImage(img, img_name):
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
                'message' : f'Image {img_name} doesnt match any object.'}
    data = result

    return data


def searchFoodByText(query):
    """
    # 
    ---
    GET method
    pake query
    """
    # Initialize data
    data = {}

    # Do querying and check for the result
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
                'message' : f'Query {query} doesnt match any object.'}
    data = result

    return data
