# integrations/trello.py

import os
import requests


class TrelloClient:
    def __init__(self):
        self.api_key = os.getenv("TRELLO_API_KEY")
        self.token = os.getenv("TRELLO_TOKEN")
        self.list_id = os.getenv("TRELLO_LIST_ID")

        if not all([self.api_key, self.token, self.list_id]):
            raise EnvironmentError("Trello environment variables not set")

    def create_card(self, name: str, description: str = ""):
        url = "https://api.trello.com/1/cards"

        params = {
            "key": self.api_key,
            "token": self.token,
            "idList": self.list_id,
            "name": name,
            "desc": description
        }

        response = requests.post(url, params=params)
        response.raise_for_status()

        return response.json()["id"]
