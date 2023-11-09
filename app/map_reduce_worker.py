from collections import defaultdict
import threading
from typing import Dict

class MapReduceWorker:
    def __init__(self, k) -> None:
        self.mapper_output = defaultdict(list)
        self.output = defaultdict(int)
        self.k = k

    def map_reduce(self, video_cache_partitions: Dict[str, Dict[str, int]]):
        # Map
        # Parse the input dictionary into (key, video_cache) pairs for each cache partition
        key_value = defaultdict(list)
        time_keys = video_cache_partitions.keys()

        # Create a list to store threads
        mapper_threads = []

        for key in time_keys:
            video_cache = video_cache_partitions[key]
            # Create a thread for each mapper task
            thread = threading.Thread(target=self.mapper, args=(video_cache,))
            mapper_threads.append(thread)
            thread.start()

        # Wait for all mapper threads to finish
        for thread in mapper_threads:
            thread.join()

        # Reduce
        # Create a list to store threads
        reducer_threads = []

        for video_id in self.mapper_output.keys():
            # Create a thread for each reducer task
            thread = threading.Thread(target=self.reduce, args=(video_id,))
            reducer_threads.append(thread)
            thread.start()

        # Wait for all reducer threads to finish
        for thread in reducer_threads:
            thread.join()

        # Get the top-k hitters
        top_k_hitters = self.get_top_k_hitters(self.output, self.k)
        return top_k_hitters
    
    def mapper(self, video_cache):
        # Add hit count at a certain time for video_id
        for video_id, hit_count in video_cache.items():
            self.mapper_output[video_id].append(hit_count)

    def reduce(self, video_id):
        # Sum hit count for video_id
        self.output[video_id] = sum(self.mapper_output[video_id])

    def get_top_k_hitters(self, data, k):
        # Sort the data by hit count in descending order and get the top-k hitters
        sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
        return sorted_data[:k]