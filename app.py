# Dependencies
from flask import Flask, request, jsonify, make_response
app = Flask(__name__)


# The source
from scr.help import (
        print_welcome,
        print_man
    )
from scr.searchfood import (
        searchFoodByImage,
        searchFoodByText
    )
from scr.getfood import (
        getAllFoods,
        getFoodDetail,
        getFoodStores
    )


# Man page
@app.route('/')
def home():
    return print_welcome()

@app.route('/api/')
def help():
    return print_man()

def error_json(message, status_code):
    # Source: https://stackoverflow.com/questions/55081497/cannot-return-404-error-as-json-instead-of-html-from-a-flask-restful-app
    return make_response(jsonify(message), status_code)


# the API
@app.route('/api/searchfoodbyimage/')
def search_image():
    if request.method != 'POST':
        return error_json('It has to be POST method.', 404)

    return jsonify(searchFoodByImage())

@app.route('/api/searchfoodbytext/')
def search_text():
    if request.method != 'GET':
        return error_json('It has to be GET method.', 404)

    return jsonify(searchFoodByText())

@app.route('/api/getallfoods/')
def get_all():
    if request.method != 'GET':
        return error_json('It has to be GET method.', 404)

    return jsonify(getAllFoods())

@app.route('/api/getfooddetail/')
def get_detail():
    if request.method != 'GET':
        return error_json('It has to be GET method.', 404)

    return jsonify(getFoodDetail())

@app.route('/api/getfoodstores/')
def get_store():
    if request.method != 'GET':
        return error_json('It has to be GET method.', 404)

    return jsonify(getFoodStores())


# Main
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
