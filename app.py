from flask import Flask, jsonify
from data import get_random_response

app = Flask(__name__)

@app.route('/api/scan', methods=['GET'])
def example_api():
    response = get_random_response()
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)