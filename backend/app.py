from flask import Flask, request, jsonify
from flask_cors import CORS

from interpreter.Parser import Parser
from interpreter.Evaluator import Evaluator

app = Flask(__name__)
CORS(app)

evaluator = Evaluator()


@app.route('/execute', methods=['POST'])
def main() :
    json = request.get_json()
    
