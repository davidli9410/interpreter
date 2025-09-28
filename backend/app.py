from flask import Flask, request, jsonify
from flask_cors import CORS

from interpreter.Parser import Parser
from interpreter.Interpreter import Interpreter

app = Flask(__name__)
CORS(app)

interpreter = Interpreter()


@app.route('/execute', methods=['POST'])
def main() :
    data = request.get_json()
    code = data.get('code',"")


    if not code:
        return jsonify({'error': 'No code'}), 400
    
    output = []

    try:
        parser = Parser()

        if code.startsWith('display') :
            result = interpreter.run(code)
            output.append(str(result))
        else :
            result = interpreter.run(code)
            output.append(str(result))
    except Exception as e :
        return jsonify({'error': 'str(e)'}),400


if __name__ == '__main__' :
    app.run(debug=True, port=5000)



    
