import logging
import threading

from collections import defaultdict
from typing import Dict


class MapReduceWorker:
    def __init__(self, k) -> None:
        self.mapper_output = defaultdict(list)
        self.output = defaultdict(int)
        self.k = k
        self.lock = threading.Lock()

    def map_reduce(self, video_cache_partitions: Dict[str, Dict[str, int]]):
            try:
                # Map
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
            except Exception as e:
                logging.error(f"An error occurred in map_reduce: {e}")
                raise

    def mapper(self, video_cache):
        try:
            # Create a local output for each mapper
            local_output = defaultdict(list)

            # Add hit count at a certain time for video_id
            for video_id, hit_count in video_cache.items():
                local_output[video_id].append(hit_count)

            with self.lock:
                # Merge local output to global output
                for video_id, hit_counts in local_output.items():
                    self.mapper_output[video_id].extend(hit_counts)

        except Exception as e:
            logging.error(f"An error occurred in mapper: {e}")
            raise

    def reduce(self, video_id):
        try:
            # Sum hit count for video_id
            with self.lock:
                self.output[video_id] = sum(self.mapper_output[video_id])        
        except Exception as e:
            logging.error(f"An error occurred in reduce: {e}")
            raise

    def get_top_k_hitters(self, data, k):
        try:
            # Sort the data by hit count in descending order and get the top-k hitters
            sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
            return sorted_data[:k]
        except Exception as e:
            logging.error(f"An error occurred in get_top_k_hitters: {e}")
            raise
