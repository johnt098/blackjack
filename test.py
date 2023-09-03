import unittest
import main

class TestFunc(unittest.TestCase):

    def test_pop(self):
        deck = main.DECK
        result = main.pop(deck)
        self.assertEqual(result, '2 (Spades)')
        self.assertFalse(len(deck) == main.DECK)

if __name__ == '__main__':
    unittest.main()