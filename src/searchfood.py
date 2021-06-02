# Source: https://cloud.google.com/firestore/docs/quickstart-servers#python
from re import search
import requests
from PIL import Image
import numpy as np
import json
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


def predict(img):
    """
    Function to predict a single input image, image must be in 150 x 150 resolution
    Output will be the prediction string out of class indicies
    """
    class_indicies = ['bakso', 'bika ambon', 'martabak manis', 'nasi goreng', 'rendang', 'sate', 'soto ayam']
    # image must be 150 x 150
    x=np.expand_dims(img, axis=0)
    images = np.vstack([x])
    images = images/255.0
    data = json.dumps({"signature_name": "serving_default", "instances": images.tolist()})
    # print(data)
    headers = {"content-type": "application/json"}
    json_response = requests.post('http://34.101.133.114:8503/v1/models/food_model:predict', data=data, headers=headers)
    # print(json_response.text)
    predictions = json.loads(json_response.text)['predictions']
    return class_indicies[np.argmax(predictions[0])]

def searchFoodByImage(img):
    """
    # 
    ---
    POST method
    formdata berisi image
    """
    # Retrive the image
    img = Image.open(img)
    # Convert image to array, resize, and remove alpha channel
    img = img.resize((150,150))
    img = np.array(img)
    img = img[:,:,:3]
    # Predict it
    query = str(predict(img))

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
    
    if not send_dict:
        return {'success' : False,
                'data'    : {},
                'message' : f'Query {query} doesnt match any object.'}
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
                'data'    : {},
                'message' : f'Query {query} doesnt match any object.'}

    # Return the result
    return {
            'success' : True,
            'message': 'BERHASIL BERHASIL BERHASIL HOREEEE',
            'data': send_dict
        }
