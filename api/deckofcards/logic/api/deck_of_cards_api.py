from api.deckofcards.infra.api.api_wrapper import APIWrapper
from api.deckofcards.infra.api.config_provider import ConfigProvider


class APIDeckOfCards:

    config = ConfigProvider.load_from_file()
    url = config['url']

    def __init__(self, request: APIWrapper):
        self._request = request

    def create_new_deck(self):
        endpoint = 'new'
        return self._request.get_request(self.url + endpoint)

    def shuffle_existing_deck(self, deck_id):
        endpoint = f'{deck_id}/shuffle/'
        return self._request.get_request(self.url + endpoint)

    def draw_cards(self, deck_id, count=1):
        endpoint = f'{deck_id}/draw/'
        params = {'count': count}
        return self._request.get_request(self.url + endpoint, params=params)

    # def add_to_pile(self, deck_id, pile_name, cards):
    #     endpoint = f'{deck_id}/pile/{pile_name}/add/'
    #     params = {'cards': ','.join(cards)}
    #     return self._request.get_request(self.url + endpoint, params=params)
    #
    # def shuffle_piles(self, deck_id,pile_name):
    #     endpoint = f'{deck_id}/pile/{pile_name}/shuffle/'
    #     return self._request.get_request(self.url + endpoint)
    #
    # def list_Cards_in_pile(self, deck_id, pile_name):
    #     endpoint = f'{deck_id}/pile/{pile_name}/list/'
    #     return self._request.get_request(self.url + endpoint)
    #
    # def draw_from_pile(self, deck_id, pile_name, count=1):
    #     endpoint = f'{deck_id}/pile/{pile_name}/draw/'
    #     params = {'count': count}
    #     return self._request.get_request(self.url + endpoint, params=params)
    #
    # def draw_from_piles_random(self,deck_id):
    #     endpoint = f'{deck_id}/draw/random/'
    #     return self._request.get_request(self.url + endpoint)
