from multiprocessing import Pool
from collections import defaultdict

class MapReduceWorker:
    def __init__(self) -> None:
        self.mapper_output = defaultdict(list)
        self.output = defaultdict(int)

    def configure_args(self):
        super(MapReduceWorker, self).configure_args()
        self.add_passthru_arg('--k', type=int, help='Number of top hitters to find')

    def map_reduce(self, video_cache_partitions):
        # Map
        # Parse the input dictionary into (key, video_cache) pairs for each cache partition
        key_value = defaultdict(list)
        time_keys = video_cache_partitions.keys()
        mappool =  Pool(len(time_keys))
        for key in time_keys:
            video_cache = video_cache_partitions[key]
            # parallel mapper
            mappool.map(self.mapper, video_cache)
        mappool.close() 
        mappool.join()# map finish
        # Reduce
        reducepool = Pool(len(self.mapper_output.keys()))
        for video_id in self.mapper_output.keys():
            # parallel reduce
            reducepool.map(self.reduce, video_id)
        reducepool.close()
        reducepool.join()# reduce finish
        return 
    
    def mapper(self, video_cache):
        # Add hit count at certain time for video_id 
        for video_id, hit_count in video_cache.items():
            self.mapper_output[video_id].append(hit_count)
        return 
    
    def reduce(self, video_id):
        # Sum hit count for video_id
        self.output[video_id] = sum(self.mapper_output[video_id])
        return

