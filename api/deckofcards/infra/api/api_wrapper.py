# import requests
#
#
# class APIWrapper:
#     def __init__(self):
#         self.base_url = "https://deckofcardsapi.com/api/deck"
#
#     def create_new_deck(self, shuffle=True):
#         endpoint = 'new'
#         if shuffle:
#             endpoint += '/shuffle/'
#         return self._get(endpoint)
#
#     def shuffle_existing_deck(self, deck_id):
#         endpoint = f'{deck_id}/shuffle/'
#         return self._get(endpoint)
#
#     def draw_cards(self, deck_id, count=1):
#         endpoint = f'{deck_id}/draw/'
#         params = {'count': count}
#         return self._get(endpoint, params=params)
#
#     def reshuffle_deck(self, deck_id):
#         endpoint = f'{deck_id}/shuffle/'
#         return self._get(endpoint)
#
#     def add_to_pile(self, deck_id, pile_name, cards):
#         endpoint = f'{deck_id}/pile/{pile_name}/add/'
#         params = {'cards': ','.join(cards)}
#         return self._get(endpoint, params=params)
#
#     def draw_from_pile(self, deck_id, pile_name, count=1):
#         endpoint = f'{deck_id}/pile/{pile_name}/draw/'
#         params = {'count': count}
#         return self._get(endpoint, params=params)
#
#     def list_piles(self, deck_id):
#         endpoint = f'{deck_id}/pile/'
#         return self._get(endpoint)
#
#     def _get(self, endpoint, params=None):
#         url = f"{self.base_url}/{endpoint}"
#         try:
#             response = requests.get(url, params=params)
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.HTTPError as http_err:
#             print(f"HTTP error occurred: {http_err}")
#         except Exception as err:
#             print(f"Other error occurred: {err}")


import requests
from api.deckofcards.infra.config_provider import ConfigProvider


class APIWrapper:

    def __init__(self):
        self._request = None

    def get_request(self, url, body=None):
        return requests.get(url, json=body)
