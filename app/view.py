from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


# Define a route for handling GET requests
# Usage: Open in browser http://localhost:5000/data
@app.route('/data', methods=['GET'])
def get_data():
    data = {
        'message': 'This is a GET request example',
        'method': 'GET',
    }
    return jsonify(data)


# Define a route with URL templating for handling GET requests
# Usage: Open in browser http://localhost:5000/data/1
@app.route('/data/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # the user_id is expected to be an integer
    user_info = {
        'user_id': user_id,
        'name': 'John Doe',
        'email': 'john@example.com',
    }
    return jsonify(user_info)


# Define a route for handling POST requests
# Usage: curl -X POST -H "Content-Type: application/json" -d '{"key": "value", "another_key": "another_value"}' http://localhost:5000/data
@app.route('/data', methods=['POST'])
def post_data():
    if request.is_json:
        data = request.get_json()
        response_data = {
            'message': 'This is a POST request example',
            'method': 'POST',
            'received_data': data
        }
        return jsonify(response_data), 201  # Respond with 201 Created status
    else:
        return jsonify({'error': 'Invalid JSON data'}), 400  # Respond with 400 Bad Request status


if __name__ == '__main__':
    app.run()
