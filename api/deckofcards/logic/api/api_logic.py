# from api.deckofcards.infra.api.api_wrapper import APIWrapper
#
#
# class DeckService:
#     def __init__(self):
#         self.api_wrapper = APIWrapper()
#
#     def create_and_draw(self, shuffle=True, count=1):
#         deck = self.api_wrapper.create_new_deck(shuffle)
#         if 'deck_id' in deck:
#             return self.api_wrapper.draw_cards(deck['deck_id'], count)
#         else:
#             return None
#
#     def shuffle_and_draw(self, deck_id, count=1):
#         self.api_wrapper.shuffle_existing_deck(deck_id)
#         return self.api_wrapper.draw_cards(deck_id, count)
#
#     def add_cards_to_pile_and_draw(self, deck_id, pile_name, cards, draw_count=1):
#         self.api_wrapper.add_to_pile(deck_id, pile_name, cards)
#         return self.api_wrapper.draw_from_pile(deck_id, pile_name, draw_count)
#
#     def get_piles(self, deck_id):
#         return self.api_wrapper.list_piles(deck_id)

from api.deckofcards.infra.api.api_wrapper import APIWrapper


class APIHouses:
    from api.deckofcards.infra.config_provider import ConfigProvider
    url = ConfigProvider.load_from_file()['url']

    def __init__(self, request: APIWrapper):
        self._request = request

    def create_new_deck(self):
        endpoint = 'new'
        return self._request.get_request(self.url + endpoint)

    def shuffle_existing_deck(self, deck_id):
        endpoint = f'{deck_id}/shuffle/'
        return self._request.get_request(self.url + endpoint)
