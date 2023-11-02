from threading import Thread
import random
import time

# Randomly generate user traffic
class Mock:
    def __init__(self) -> None:
        self.main_thread = Thread(target=self.run)

    def generate(self) -> int:
        return random.randint(1, 100)

    # a function to spawn random threads and request traffic to localhost
    def run(self) -> None:
        while True:
            time.sleep(1)
            Thread(target=self.generate).start()
