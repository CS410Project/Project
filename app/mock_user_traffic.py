import logging
import threading
import random

from querier import SimpleVideoPlatformQuerier

class UserTraffic:
   def __init__(self, num_calls=1000) -> None:
      self.lock = threading.Lock()
      self.querier = SimpleVideoPlatformQuerier()
      self.base_url = "play/"
      self.videos = list(range(1, 101))
      self.num_calls = num_calls
   
   def open_random_video(self, params=None):
      video_id = random.choice(self.videos)
      response = self.querier.get(f"{self.base_url}{video_id}", params=params)
      logging.debug(f"Opened video {video_id} with params {params}")
      return response

   # generate nums_calls threads to call open_random_video
   def generate_traffic(self):
      try:
         threads = []
         for _ in range(self.num_calls):
            thread = threading.Thread(target=self.open_random_video)
            threads.append(thread)
            thread.start()
         
         for thread in threads:
            thread.join()
      except Exception as e:
         logging.error(f"An error occurred in generate_traffic: {e}")
         raise

# Sample usage
"""
if __name__ == "__main__":
   logging.basicConfig(level=logging.DEBUG)
   user_traffic = UserTraffic(num_calls=100)
   user_traffic.generate_traffic()
"""
