# import unittest
# from api.deckofcards.infra.api.api_wrapper import APIWrapper
#
#
# class TestDeckOfCardsAPIWrapper(unittest.TestCase):
#     def setUp(self):
#         self.api = APIWrapper()
#
#     def test_create_new_deck(self):
#         response = self.api.create_new_deck()
#         self.assertIn('deck_id', response)
#
#     def test_draw_cards(self):
#         deck = self.api.create_new_deck()
#         response = self.api.draw_cards(deck['deck_id'], count=2)
#         self.assertEqual(len(response['cards']), 2)
#
# # More tests for other methods...


import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.api_houses import APIHouses


class TestAPIHarryPotter(unittest.TestCase):

    def test_check_house_by_id(self):
        api_request = APIWrapper()
        api_house = APIHouses(api_request)
        result = api_house.get_houses_by_id("0367baf3-1cb6-4baf-bede-48e17e1cd005")
        # result = api_house.get_houses_by_id("f{config}" / ENUM)
        body = result.json()

        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["name"], "Gryffindor")

response = self.api.create_new_deck()