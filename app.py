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
@app.route('/api/searchfoodbyimage/', methods=['POST'])
def search_image():
    return jsonify(searchFoodByImage())

@app.route('/api/searchfoodbytext/', methods=['GET'])
def search_text():
    return jsonify(searchFoodByText())

@app.route('/api/getallfoods/', methods=['GET'])
def get_all():
    return jsonify(getAllFoods())

@app.route('/api/getfooddetail/', methods=['GET'])
def get_detail():
    return jsonify(getFoodDetail())

@app.route('/api/getfoodstores/', methods=['GET'])
def get_store():
    return jsonify(getFoodStores())


# Main
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
