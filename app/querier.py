import requests

from typing import Dict

class SimpleVideoPlatformQuerier:
    def __init__(self) -> None:
        self.url = "http://127.0.0.1:5000"

    def get(self, query_url:str, params=None):
        response = requests.get(
            url=f"{self.url}/{query_url}",
            params=params,
        )
        return response.json()

    def post(self, query_url:str, data:Dict=None):
        response = requests.post(
            url=f"{self.url}/{query_url}",
            json=data,
        )
        return response.json()
