# Dependencies
from werkzeug.utils import secure_filename

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

def allowed_filename(filename):
    return '.' in filename \
            and filename.rsplit('.', 1)[1] in \
            ['jpeg', 'jpg', 'png']


# the API
@app.route('/api/search/image/', methods=['POST'])
def search_image():
    img = request.files['image']

    if not img:
        return error_json('No image detected.', 400)

    img_name = secure_filename(img.filename)
    mimetype = img.mimetype

    if allowed_filename(img_name):
        # Upload image to db
        # and pass it to model
        pass

    return jsonify(searchFoodByImage())

@app.route('/api/search/<str:name>/', methods=['GET'])
def search_text():
    return jsonify(searchFoodByText())

@app.route('/api/food/', methods=['GET'])
def get_all():
    return jsonify(getAllFoods())

# Source: https://stackoverflow.com/questions/28229668/python-flask-how-to-get-route-id-from-url
@app.route('/api/food/<int:id>/', methods=['GET'])
def get_detail(id):
    return jsonify(getFoodDetail(id))

@app.route('/api/food/store/<int:id>/', methods=['GET'])
def get_store(id):
    return jsonify(getFoodStores(id))


# Main
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
