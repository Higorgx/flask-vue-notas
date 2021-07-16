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
    NUMBERS = post_data.get("numbers")

    soma = 0
    for i in range(0,len(NUMBERS)):
        soma = soma + NUMBERS[i]
    
    media = soma/len(NUMBERS)

    

    response_object = {'Qtd. Números':len(NUMBERS), 'Ordem':NUMBERS, 
    'Ordem Inversa':list(reversed(NUMBERS)), 'Soma dos Números':soma, 'Média dos Números': media }


    
    return jsonify(response_object)



if __name__ == '__main__':
    app.run()