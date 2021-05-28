# Dependencies
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np

from flask import (
        Flask,
        request,
        jsonify,
        make_response,
    )
app = Flask(__name__)


# The source
from src.help import (
        print_welcome,
        print_man,
    )
from src.searchfood import (
        searchFoodByImage,
        searchFoodByText,
    )
from src.getfood import (
        getFoodDetail,
        getFoodStores,
    )


# Man page
@app.route('/')
def home():
    return print_welcome()

@app.route('/api/v1/')
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
# Structure API: https://github.com/SaveVic/the-food-explorer/blob/master/docs/api.md
@app.route('/api/v1/food/', methods=['POST', 'GET'])
def search_image():
    if request.method == 'POST':
        # Search by image
        # Source: https://stackoverflow.com/questions/31010819/uploading-file-in-python-flask
        img = request.files['image']

        # Check image files
        if not img:
            return error_json('No image detected.', 400)
        if not allowed_filename(secure_filename(img.filename)):
            return error_json('File not supported.', 400)

        # Convert image to array
        img = np.array(Image.open(img))

        # Pass it to model
        return jsonify(searchFoodByImage(img))

    else:
        # Search by text
        query = str(request.args.get('q'))

        if not query:
            return error_json('No query detected.', 400)

        return jsonify(searchFoodByText(query))

# Source: https://stackoverflow.com/questions/28229668/python-flask-how-to-get-route-id-from-url
@app.route('/api/v1/food/<int:food_id>/detail/', methods=['GET'])
def get_detail(food_id):
    return jsonify(getFoodDetail(int(food_id)))

@app.route('/api/v1/food/<int:food_id>/location/', methods=['GET'])
def get_store(food_id):
    lat = str(request.args.get('latitude'))
    lng = str(request.args.get('longitude'))

    if not lat or lng:
        lat = '-6.1753924'
        lng = '106.8249641'

    return jsonify(getFoodStores(int(food_id), float(lat), float(lng)))


# Main
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
