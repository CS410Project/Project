import threading
import random
import time
# List of 100 videos
videos = list(range(1, 101))
def open_random_video(user_id):
   video_id = random.choice(videos)
   # Simulate some processing time for watching the video
   time.sleep(random.uniform(1, 5))
# Number of users
num_users = 10000
# Create threads for each user
threads = [threading.Thread(target=open_random_video, args=(i,)) for i in range(num_users)]
# Start the threads
for thread in threads:
   thread.start()
# Wait for all threads to finish
for thread in threads:
   thread.join()
