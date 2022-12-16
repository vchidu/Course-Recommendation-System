import json
from flask import Flask, request, jsonify
from predict import pred

app = Flask(__name__)

@app.route('/', methods=['GET'])
def query_records():
    title = 'Finance for Managers'
    n=5
    
    return jsonify(pred(title,n))

if __name__ == '__main__':
    app.run()

app.run(debug=True)