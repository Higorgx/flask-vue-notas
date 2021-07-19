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
    VALABAIXO = []
    VALMEDIA = []
    post_data = request.get_json()
    numbers = post_data
    global NUMBERS
    NUMBERS = post_data.get("numbers")

    soma = 0
    for i in range(0,len(NUMBERS)):
        soma = soma + NUMBERS[i]
    
    media = soma/len(NUMBERS)
    print('oi',media)
    for i in range(0,len(NUMBERS)):
        if NUMBERS[i] > media:
            VALMEDIA.append(NUMBERS[i])
            print(VALMEDIA)

    for i in range(0,len(NUMBERS)):
        if NUMBERS[i] < 7:
            VALABAIXO.append(NUMBERS[i])
            print(VALABAIXO)

    

    response_object = {
        'qtd':len(NUMBERS),
        'ordem':NUMBERS,
        'inversa':list(reversed(NUMBERS)),
        'sum':soma,
        'media': media,
        'acimaMedia': VALMEDIA,
        'abaixo7': VALABAIXO
    }


    
    return jsonify(response_object)



if __name__ == '__main__':
    app.run()