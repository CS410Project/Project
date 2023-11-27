import logging

from datetime import datetime
from map_reduce_worker import MapReduceWorker
from mock_user_traffic import UserTraffic
from querier import SimpleVideoPlatformQuerier
from time import sleep

class UnifiedWorker:
    def __init__(self, k=10, num_calls=10000) -> None:
        self.querier = SimpleVideoPlatformQuerier()
        self.user_traffic = UserTraffic(num_calls=num_calls)
        self.map_reduce_worker = MapReduceWorker(k=k)

    def initiate_map_reduce(self):
        try:
            # Get video cache partitions
            video_cache_partitions = self.querier.get("video_cache")
            # MapReduce
            top_k_hitters = self.map_reduce_worker.map_reduce(video_cache_partitions)
            return top_k_hitters
        except Exception as e:
            logging.error(f"An error occurred in initiate_map_reduce: {e}")
            raise

    def generate_traffic(self):
        try:
            self.user_traffic.generate_traffic()
        except Exception as e:
            logging.error(f"An error occurred in generate_traffic: {e}")
            raise

    def run_pipeline(self):
        try:
            # Generate traffic
            self.generate_traffic()
            # MapReduce
            top_k_hitters = self.initiate_map_reduce()
            # Update top-k hitters
            return self.querier.post("top_k_hitters", data=top_k_hitters)
        except Exception as e:
            logging.error(f"An error occurred in run_pipeline: {e}")
            raise

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unified_worker = UnifiedWorker(k=10, num_calls=1000)
    # run pipeline every minute
    while True:
        unified_worker.run_pipeline()
        logging.info(f"Pipeline run at {datetime.now()}")
        sleep(60)
