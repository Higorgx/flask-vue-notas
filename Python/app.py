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
    soma = getSum()
    return jsonify(numbers)


def getSum():
    valor = 0
    soma = 0
    global NUMBERS
    print(len(NUMBERS))
    while valor < len(NUMBERS):
        print(NUMBERS)
        soma = NUMBERS[valor] + soma
        valor = valor + 1 
    print(soma)
    

if __name__ == '__main__':
    app.run()