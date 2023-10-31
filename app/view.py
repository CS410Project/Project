from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


# define a sample GET endpoint printing the parameter passed in the URL
@app.route('/sample_get', methods=['GET'])
def sample_get():
    request_data = request.args
    return f"Request args: {request_data['name']}"


@app.route('/sample_post', methods=['POST'])
def sample_post():
    request_data = request.form
    return f"Request form: {request_data['name']}"


if __name__ == '__main__':
    app.run()
