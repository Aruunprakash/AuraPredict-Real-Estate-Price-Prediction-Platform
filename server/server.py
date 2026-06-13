from flask import Flask, request, jsonify
from flask_cors import CORS
import util
app = Flask(__name__)
CORS(app)

util.load_saved_artifacts()
@app.route('/get_location_names', methods=['GET', 'POST'])
def get_location_names():
    print("DEBUG locations:", util.get_location_names(), type(util.get_location_names()))
    response = jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_estimated_price', methods=['POST'])
def get_price():
    total_sqft = float(request.json['total_sqft'])
    location = request.json['location']
    bhk = int(request.json['bhk'])
    bath = int(request.json['bath'])

    response = jsonify({
        'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("starting py flask server for home price prediction")
    app.run()
