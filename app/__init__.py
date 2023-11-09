import threading
from collections import defaultdict
from flask import Flask, jsonify, request
from datetime import datetime
from typing import Dict
from map_reduce_worker import MapReduceWorker

import random
video_cache_partitions: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
video_id = ["video_url_1", "video_url_2", "video_url_3", "video_url_4", "video_url_5"]
time_id = ["2020-01-01 00:00:00", "2020-01-01 00:01:00", "2020-01-01 00:02:00"]
for time in time_id:
    for video in video_id:
        value = random.randint(0, 20)
        temp = {video: value}
        video_cache_partitions[time].update(temp)

mapreduce = MapReduceWorker(k=5)
result = mapreduce.map_reduce(video_cache_partitions)
print(result)