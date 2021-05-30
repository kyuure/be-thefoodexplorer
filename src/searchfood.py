# Source: https://cloud.google.com/firestore/docs/quickstart-servers#python
from re import search

import requests
from google.cloud import firestore
db = firestore.Client()


def getFoodAll():
    """
    # 
    ---
    GET method
    ambil semua data
    """

    # Do querying
    users_ref = db.collection(u'food')
    docs = users_ref.stream()

    # Assign the query to local variable
    send_dict = []
    for el in docs:
        data = el.to_dict()
        real_dict = {}
        real_dict['id']    = data['id']
        real_dict['name']  = el.id
        real_dict['city']  = data['city']
        real_dict['image'] = data['image']
        send_dict.append(real_dict)

    # Return the result
    return {
            'success' : True,
            'message': 'BERHASIL BERHASIL BERHASIL HOREEEE',
            'data': send_dict
        }


def searchFoodByImage(img):
    """
    # 
    ---
    POST method
    formdata berisi image
    """

    # Run model then specify the name of food
    ip_model   = '0.0.0.0'
    port_model = '8503'
    r = requests.post(
            'http://'
            + ip_model + ':'
            + port_model + '/',
        data=img,
        headers={'content-type': 'application/json'}
    )

    # Do querying
    users_ref = db.collection(u'food')
    docs = users_ref.stream()

    # Assign the query to local variable
    send_dict = []
    for el in docs:
        if r.text != str(el.id):
            continue
        data = el.to_dict()
        real_dict = {}
        real_dict['id']    = data['id']
        real_dict['name']  = el.id
        real_dict['city']  = data['city']
        real_dict['image'] = data['image']
        send_dict.append(real_dict)

    # Return the result
    return {
            'success' : True,
            'message': 'BERHASIL BERHASIL BERHASIL HOREEEE',
            'data': send_dict
        }


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
    send_dict = []
    for el in docs:
        if not search(
                '.*' + query.lower().replace(' ', '.*') + '.*',
                str(el.id).lower()):
            continue
        data = el.to_dict()
        real_dict = {}
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
