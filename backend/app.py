import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, request, jsonify
from flask_cors import CORS

from interpreter.Parser import Parser
from interpreter.Interpreter import Interpreter

app = Flask(__name__)
CORS(app)

interpreter = Interpreter()

@app.route('/execute', methods=['POST'])
def main():
    data = request.get_json()
    code = data.get('code', "")

    if not code:
        return jsonify({'error': 'No code provided'}), 400
    
    output = []

    try:
        parser = Parser()
        lines = [line.strip() for line in code.split('\n') if line.strip()]
        for line in lines:
            if line.startswith('display'):
                result = interpreter.run(line)
                if isinstance(result, bool):
                    output.append(str(result).lower())
                else:
                    output.append(str(result))
            else:
                result = interpreter.run(line)
            
        return jsonify({'result': '\n'.join(output)})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)