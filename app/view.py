from collections import defaultdict
from flask import Flask, jsonify, request
from datetime import datetime
from typing import Dict

app = Flask(__name__)

# simple cache for video play counts
# {
#   "video_url_1": 1,
#   "video_url_2": 2,
#   ....
# }
video_cache: Dict[str, int] = defaultdict(int)

# partitioned video_cache for each time lapse
# {
#   "2020-01-01 00:00:00": {
#     "video_url_1": 1,
#     "video_url_2": 2,
#     ....
#   },
#   "2020-01-01 01:00:00": {
#     "video_url_1": 1,
#     "video_url_2": 2,
#     ....
#   },
#  ....
# }
video_cache_partitions: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))


@app.route('/')
def root_url():
    return 'Simple Video Platform Root'


#=================================================Sample Showcases==========================================================
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
#=======================================================================================================================



# A simple GET route simulating user hit video play button
@app.route('/play/<str:video_id>', methods=['GET'])
def play_video(video_id:str):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:00:00')
    video_cache_partitions[timestamp][video_id] += 1


# TODO: define a simple GET route to return video play count for a given time lapse
# Usage: curl http://localhost:5000/play_count?start_time=2020-01-01%2000:00:00&end_time=2020-01-01%2012:00:00
@app.route('/play_count', methods=['GET'])
def get_video_play_count():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    if not start_time or not end_time:
        return jsonify({'error': 'Invalid start_time or end_time'}), 400
    raise NotImplementedError("TODO: implement this route")


# fetch video cache partions
@app.route('/video_cache', methods=['GET'])
def get_video_cache():
    return jsonify(video_cache_partitions)


# clear global cache resetting video play count
def initialize_video_count_cache():
    video_cache_partitions.clear()


if __name__ == '__main__':
    initialize_video_count_cache()
    app.run()
