from flask import Flask, jsonify, request
from flask_cors import CORS

NUMBERS = []

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/numbers', methods=['GET'])
def get_result():
    global NUMBERS
    response_object = {'status': 'success'}
    response_object['numbers'] = NUMBERS
    return jsonify(response_object)

@app.route('/numbers', methods=['POST'])
def post_numbers():
    post_data = request.get_json()
    numbers = post_data
    global NUMBERS
    NUMBERS = post_data.get('numbers')
    return jsonify(numbers)

if __name__ == '__main__':
    app.run()