import unittest
from api.deckofcards.infra.api.api_wrapper import APIWrapper
from api.deckofcards.logic.api.deck_of_cards_api import APIDeckOfCards


class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        self.api = APIDeckOfCards(APIWrapper())

    def test_create_new_deck(self):
        response = self.api.create_new_deck()
        self.assertEqual(52, response.json()['remaining'])

    def test_draw_cards(self):
        deck = self.api.create_new_deck().json()
        number_before = deck['remaining']
        deck = self.api.draw_cards(deck['deck_id'], count=2).json()
        number_after = deck['remaining']
        self.assertEqual(number_before - 2, number_after)





